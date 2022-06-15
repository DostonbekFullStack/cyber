from django.urls import path
from .views import *

urlpatterns = [
    path('api/infoget/', InfoGET),
    path('api/tour/cs/', RandomizeCS),
    # path('api/tour/dota/', RandomizeDota),

]