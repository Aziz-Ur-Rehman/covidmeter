from rest_framework import filters


class ReportsFilterBackend(filters.BaseFilterBackend):
    """
    Filter reports based on their country geoid
    """

    def filter_queryset(self, request, queryset, view):
        """
        Implements filter_queryset method for filtering daily reports
        based on the geoid provided in url query params.
        """
        geoid = request.GET.get("country_geoid")
        if geoid:
            queryset = queryset.filter(country__geoid__iexact=geoid)

        return queryset
