from django.urls import path
from .views import TournamentListAPIView

urlpatterns = [
    path('tournaments/', TournamentListAPIView.as_view(), name='tournament-list'),
]