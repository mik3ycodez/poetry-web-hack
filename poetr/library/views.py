from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Genre, Poem


class Page(DetailView):
    model = Poem

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# Create your views here.
