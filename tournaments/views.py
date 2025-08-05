from django.shortcuts import render
from rest_framework import generics
from .models import Tournament
from .serializers import TournamentSerializer
from django_filters.rest_framework import DjangoFilterBackend
import django_filters

class TournamentFilter(django_filters.FilterSet):
    sport = django_filters.CharFilter(field_name="sport", lookup_expr="iexact")
    level = django_filters.CharFilter(field_name="level", lookup_expr="iexact")
    start_date = django_filters.DateFilter(field_name="start_date", lookup_expr="gte")
    end_date = django_filters.DateFilter(field_name="end_date", lookup_expr="lte")

    class Meta:
        model = Tournament
        fields = ['sport', 'level', 'start_date', 'end_date']

class TournamentListAPIView(generics.ListAPIView):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TournamentFilter
