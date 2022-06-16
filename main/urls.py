from django.urls import path, include
from .views import *

urlpatterns = [
    path('infoget/', InfoGET),
    path('welcomeget/', WelcomeSectionGET),
    path('informationget/', InformationGET),
    path('informationcardget/', InformationCardGET),
    path('becomeonfusget/', BecomeoneofusGET),
    path('gameget/', GameGET),
    path('photogalaryget/', PhotoGalerieGET),
    path('numberofresidentsget/', NumberofResidenentGET),
    path('teampost/', TeamPOST),
    path('newsletterpost/', NewsletterPOST),
    path('generategroup/<int:pk>/', GenerateGroup),
    path('tour/<int:pk>/', TournamentPk),
    path('tournament/', TournamentsGET.as_view()),
    path('tournament/<int:pk>/', TournamentID.as_view()),
    # path('api/generateteam/<int:pk>/', GenerateTeam),
    # path('asd/', asd),
]