from rest_framework import serializers
from .models import *

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'

class WelcomeSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WelcomeSection
        fields = '__all__'

class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'

class InformationCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformationCard
        fields = '__all__'

class BecomeoneofusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Becomeoneofus
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = '__all__'

class PhotoGaleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoGaleryImage
        fields = '__all__'

class PhotoGalerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoGalerie
        fields = '__all__'

class NumberofResidenentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumberofResidenent
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = '__all__'