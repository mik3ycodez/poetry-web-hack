from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Genre, Poem


class Page(DetailView):
    model = Poem
    template_name = 'library/poem_detail.html'

    def get_context_data(self, **kwargs):
        poem = super().get_context_data(**kwargs)['object']
        context = {'title': poem.title,
                   'author': poem.author,
                   'timestamp': poem.timestamp,
                   'genres': poem.genres,
                   'text': poem.text,
                   'links': poem.links}

        return context

#class ReportSubmit()
# Create your views here.
