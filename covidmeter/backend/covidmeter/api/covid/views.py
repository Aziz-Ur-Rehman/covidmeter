from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import ReportsFilterBackend
from .models import Continent, Country, DailyReport
from .serializers import ContinentSerializer, CountrySerializer, DailyReportSerializer
from .services.graph_service import GraphDataComputer


class ReportViewset(viewsets.ReadOnlyModelViewSet):
    """
    Lists and retrieves Daily reports from :model:`covid.DailyReports`.
    """

    queryset = DailyReport.objects.all().prefetch_related("country")
    serializer_class = DailyReportSerializer
    filter_backends = [
        ReportsFilterBackend,
    ]


class GraphApiView(APIView):
    """
    Computes and returns the data required for plotting graphs
    from :model:`covid.DailyReports`.
    """

    def get(self, request, continent=None, geoid=None):
        """
        Get method for graph data w.r.t country, continent
        or whole world (if both continent and country are none).
        """
        date = {
            "year": request.GET.get("year"),
            "month": request.GET.get("month"),
            "day": request.GET.get("day"),
        }

        if continent:
            try:
                Continent.objects.get(name__iexact=continent)
            except Continent.DoesNotExist:
                return Response("Continent not found", status=status.HTTP_404_NOT_FOUND)
        elif geoid:
            try:
                Country.objects.get(geoid__iexact=geoid)
            except Country.DoesNotExist:
                return Response("Country not found", status=status.HTTP_404_NOT_FOUND)

        graph_computer = GraphDataComputer(continent, geoid, date)
        return Response(graph_computer.eval_graph_data())


class CountryViewset(viewsets.ReadOnlyModelViewSet):
    """
    Lists and retrieves country from :model:`covid.Country`.
    """

    queryset = Country.objects.all().prefetch_related("continent")
    serializer_class = CountrySerializer
    pagination_class = None


class ContinentViewset(viewsets.ReadOnlyModelViewSet):
    """
    Lists and retrieves continents from :model:`covid.Continent`.
    """

    queryset = Continent.objects.all()
    serializer_class = ContinentSerializer
    pagination_class = None
