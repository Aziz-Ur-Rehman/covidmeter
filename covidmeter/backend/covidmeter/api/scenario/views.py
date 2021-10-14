from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from .models import UserScenario
from .permissions import IsOwner
from .serializers import UserScenarioSerializer
from .services.hash_service import HashService


class UserScenarioViewSet(viewsets.ModelViewSet):
    """
    UserScenarioViewSet creates, retrieves, create, update and destroy
    entries in :model:`scenario.UserScenario`.
    """

    queryset = UserScenario.objects.filter(is_delete=False).prefetch_related(
        "scenario_hash"
    )
    serializer_class = UserScenarioSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def list(self, request, *args, **kwargs):
        """
        Lists entries in :model:`scenario.UserScenario` owned by request.user.
        """
        self.queryset = self.get_queryset().filter(user=request.user)
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Creates an entry in :model:`scenario.UserScenario` after creating its
        params' hash and result.
        """
        request.data["user"] = request.user.id
        serializer = self.get_serializer_class()(data=request.data)

        hash_service = HashService(request.data.get("scenario_hash", {}))
        hash = hash_service.get_or_create_hash()

        if serializer.is_valid():
            serializer.save(scenario_hash=hash)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        """
        Updates an entry in :model:`scenario.UserScenario` after updating its
        params' hash and result if params for the scenarios changes.
        """
        request.data["user"] = request.user.id

        instance = self.get_object()
        serializer = self.get_serializer_class()(instance, data=request.data)

        if request.data.get("scenario_hash", None):
            hash_service = HashService(request.data["scenario_hash"])
            request.data["scenario_hash"] = hash_service.get_or_create_hash()
        else:
            request.data["scenario_hash"] = instance.scenario_hash

        if serializer.is_valid():
            serializer.save(scenario_hash=request.data["scenario_hash"])
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        """
        Destroys an entry in :model:`scenario.UserScenario`.
        """
        instance = self.get_object()
        instance.is_delete = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
