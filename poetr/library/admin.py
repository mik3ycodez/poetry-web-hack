from django.contrib import admin
from .models import Genre, Poem, Report

admin.site.register(Report)
admin.site.register(Poem)
admin.site.register(Genre)
