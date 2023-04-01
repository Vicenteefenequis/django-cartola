from django.contrib import admin
from .models import Player, Team, MyTeam, Match
# Register your models here.


admin.site.register(Player)
admin.site.register(Team)
admin.site.register(MyTeam)
admin.site.register(Match)
