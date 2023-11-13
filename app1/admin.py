from django.contrib import admin
from .models import Movie,favorite
# Register your models here.
admin.site.register(Movie)
admin.site.register(favorite)