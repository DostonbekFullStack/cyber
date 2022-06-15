from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *
from rest_framework.decorators import api_view
import random

# Create your views here.

@api_view(['GET'])
def InfoGET(request):
    info = Info.objects.last()
    ser = InfoSerializer(info, many=False)
    return Response(ser.data)

@api_view(['GET'])
def WelcomeSectionGET(request):
    welcome = WelcomeSection.objects.last()
    ser = WelcomeSectionSerializer(welcome, many=False)
    return Response(ser.data)

@api_view(['GET'])
def InformationGET(request):
    information = Information.objects.last()
    ser = InformationSerializer(information, many=False)
    return Response(ser.data)

@api_view(['GET'])
def InformationCardGET(request):
    informationcard = InformationCard.objects.all().order_by('-id')[0:4]
    ser = InformationCardSerializer(informationcard, many=True)
    return Response(ser.data)

@api_view(['GET'])
def BecomeoneofusGET(request):
    becomeoneofus = Becomeoneofus.objects.last()
    ser = BecomeoneofusSerializer(becomeoneofus, many=False)
    return Response(ser.data)

@api_view(['GET'])
def GameGET(request):
    game = Game.objects.last()
    ser = GameSerializer(game, many=False)
    return Response(ser.data)

# @api_view(['GET'])
# def TournamentGET(request):
#     tour = Tournament.objects.all()
#     ser = TournamentSerializer(tour, many=True)
#     return Response(ser.data)

@api_view(['GET'])
def RandomizeCS(request):
    instance = Tournament.objects.get(id=2)
    teamtr1 = Team.objects.get(id=3)
    teamtr1.save()
    teamtr2 = Team.objects.get(id=4)
    teamtr2.save()
    instance.team.add(teamtr1, teamtr2)
    instance.save()
    return Response('smth')
    # cs = []
    # if len(teamtr) >= 4:
    #     for i in teamtr:
    #         cs.append(i)
    #     instance.team.add(cs)
    #     return Response('asd')
    
    # for i in teamtr:
    #     Tournament.objects.create(team=i)
    # return Response('sasd')
    
@api_view(['GET'])
def RandomizeDota(request):
    instance = Tournament.objects.all()
    teamtr = Team.objects.get(team=True)
    if len(teamtr) >= 4:
        for i in teamtr:
            


@api_view(['GET'])
def PhotoGalerieGET(request):
    photogalery = PhotoGalerie.objects.last()
    ser = PhotoGalerieSerializer(photogalery, many=False)
    return Response(ser.data)

@api_view(['GET'])
def NumberofResidenentGET(request):
    numberofresidents = NumberofResidenent.objects.all().order_by('-id')[0:4]
    ser = NumberofResidenentSerializer(numberofresidents, many=False)
    return Response(ser.data)

@api_view(['POST'])
def TeamPOST(request):
    try:
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        data = {
            'error': f"{err}"
        }
        return Response(data)

@api_view(['POST'])
def NewsletterPOST(request):
    try:
        serializer = NewsletterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        data = {
            'error': f"{err}"
        }
        return Response(data)