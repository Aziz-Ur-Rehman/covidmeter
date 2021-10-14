from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import (
    BlacklistedToken,
    OutstandingToken,
    RefreshToken,
)

from .permissions import IsSelfOrReadOnly
from .serializers import UserProfileSerializer, UserSerializer

User = get_user_model()


class UserProfileView(APIView):
    """
    UserProfileView returns serialized request.user instance.
    """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """
        Returns request.user.
        """

        serializer = UserProfileSerializer(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserListCreateView(generics.ListCreateAPIView):
    """
    UserListCreateView lists and creates
    entries in :model:`user.User`.
    """

    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer

    def create(self, request, format=None):
        """
        Override create method for user's set_password call.
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        instance.set_password(request.data.get("password"))
        instance.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    UserRetrieveUpdateDestroyView Retrieve, update and destroy
    entries in :model:`user.User`.
    """

    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    permission_classes = [IsSelfOrReadOnly]

    def update(self, request, *args, **kwargs):
        """
        Override update method for user's set_password call.
        """
        password = request.data.get("password")
        if password:
            instance = self.get_object()
            instance.set_password(password[0])
            instance.save()

        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Override destroy method for setting user is_active to false.
        """
        instance = self.get_object()
        instance.is_active = False
        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class LogoutView(APIView):
    """
    LogoutView blacklists the refresh token.
    """

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        """
        Post method blacklists the refresh token given in request body.
        """
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_205_RESET_CONTENT)


class LogoutFromAllDevicesView(APIView):
    """
    LogoutFromAllDevicesView blacklists all tokens for a user.
    """

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        """
        Post method blacklists all tokens for request.user
        """
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)
