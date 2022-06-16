from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(SocialMedia)
admin.site.register(Info)
admin.site.register(WelcomeSection)
admin.site.register(Information)
admin.site.register(InformationCard)
admin.site.register(Becomeoneofus)
admin.site.register(Game)
# admin.site.register(Tournament)
@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ('game', 'teams_or_players')

admin.site.register(PhotoGaleryImage)
admin.site.register(PhotoGalerie)
admin.site.register(NumberofResidenent)
admin.site.register(Team)
admin.site.register(Newsletter)
admin.site.register(Group)