from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import *
from rest_framework.generics import RetrieveAPIView, ListAPIView
from .serializer import *
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
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

@api_view(['GET'])
def GenerateGroup(request, pk):
    teamtr = Team.objects.all().filter(team=False, direction_id=pk)
    list = []
    for i in teamtr:
        list.append(i)
    a = Tournament.objects.create(game_id=pk)
    if len(list) < 2:
        return Response('kamandalar yetmayapti')
    else:
        randoming = random.sample(list, 2)
    a.team.set(randoming)
    a.save()
    data = {
        'players': f"{randoming}",
        'game':a.game.name,
    }
    return Response(data)

@api_view(['GET'])
def TournamentPk(request, pk):
    teamtr = Team.objects.all().filter(team=True, direction_id=pk, is_playing=False)
    list = []
    for i in teamtr:
        list.append(i)
    if len(list) < 2:
        return Response('kamandalar yetmayapti')
    else:
        randoming = random.sample(list, 2)
        for i in randoming:
            print(i.is_playing)
            i.is_playing = True
            i.save()
        a = Tournament.objects.create(game_id=pk)
        a.team.set(randoming)
        a.save()
        data = {
            'game':a.game.name,
            'teamlar': f"{randoming}"
        }
    return Response(data)

# @api_view(['GET'])
# def GenerateTeam(request, pk):
#     teamtr = Team.objects.all().filter(team=True, direction_id=pk)
#     list = []
#     for i in teamtr:
#         list.append(i)
#     a = Group.objects.create(game_id=pk)
#     randoming = random.sample(list, 1)
#     a.team.set(randoming)
#     a.save()
#     data = {
#         'komanda': f"{randoming}",
#         'msg':'Tasdiqlandi',
#         'game':a.game.name,
#     }
#     return Response(data)

# @api_view(['GET'])
# def asd(request, pk):
#     teamtr = Group.objects.filter(team_team=True, direction_id=pk)
#     list = []
#     for i in teamtr:
#         list.append(i)
#     a = Tournament.objects.create(game_id=pk)
#     randoming = random.sample(list, 2)
#     a.team.set(randoming)
#     a.save()
#     data = {
#         'game':a.game.name,
#         'teamlar': f"{randoming}"
#     }
#     return Response(data)

class TournamentsGET(ListAPIView):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

    def list(self, request):
        queryset = Tournament.objects.all().order_by('-id')[0:4]
        serializer = TournamentSerializer(queryset, many=True)
        return Response(serializer.data)

class TournamentID(RetrieveAPIView):

    def retrieve(self, request, pk):
        tournament = Tournament.objects.get(id=pk)
        ser = TournamentSerializer(tournament)
        return Response(ser.data)
    

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