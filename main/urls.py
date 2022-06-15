from django.urls import path
from .views import *

urlpatterns = [
    path('api/infoget/', InfoGET),
    path('api/tour/<int:pk>/', RandomizeTeam),
    path('api/tour/<int:pk>/', RandomizePk),

]