from django.contrib import admin
from movie.models import Movies, Season, Episode
# Register your models here.


admin.site.register(Movies)
admin.site.register(Season)
admin.site.register(Episode)