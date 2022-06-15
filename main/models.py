from django.db import models

# Create your models here.
class SocialMedia(models.Model):
    link = models.TextField()

class Info(models.Model):
    logo = models.ImageField(upload_to='logo/')
    links = models.ManyToManyField(SocialMedia)

class WelcomeSection(models.Model):
    title = models.CharField(max_length=255)
    bg = models.ImageField(upload_to='welcome/')

class Information(models.Model):
    bg = models.ImageField(upload_to='information/')
    title = models.CharField(max_length=255)

class InformationCard(models.Model):
    img = models.ImageField(upload_to='informationcards/')
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

class Becomeoneofus(models.Model):
    bg = models.ImageField(upload_to='becomeoneofus/')
    title = models.CharField(max_length=255)

class Game(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class PhotoGaleryImage(models.Model):
    image = models.ImageField(upload_to='photogalery/')

class PhotoGalerie(models.Model):
    images = models.ManyToManyField(PhotoGaleryImage)

class NumberofResidenent(models.Model):
    number = models.IntegerField()
    text = models.CharField(max_length=255)

class Team(models.Model):
    one_player = models.BooleanField(default=False)
    team = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()
    direction = models.ForeignKey(Game, on_delete=models.PROTECT)
    phone = models.IntegerField()
    experience_from = models.IntegerField(default=1)
    experience_to = models.IntegerField(default=2)
    team_member = models.IntegerField(default=1)
    img = models.ImageField(upload_to="Team/")

    def __str__(self):
        return self.name


class Tournament(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    team = models.ManyToManyField(Team, null=True, blank=True)

class Newsletter(models.Model):
    email = models.EmailField()