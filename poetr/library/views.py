from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Genre, Poem
import random
r = random.Random()


def Random(request):
    page = Poem.objects.order_by('?')[:1][0]
    return redirect(page)


class Page(DetailView):
    model = Poem
    template_name = 'library/poem_detail.html'

    def get_context_data(self, **kwargs):
        poem = super().get_context_data(**kwargs)['object']
        context = {'title': poem.title,
                   'author': poem.author,
                   'timestamp': poem.timestamp,
                   'genres': poem.genres.all(),
                   'text': poem.text,
                   'links': poem.links.all()}

        return context

#class ReportSubmit()
# Create your views here.
