from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Genre, Poem
from .forms import NewPoemForm, ReportForm
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


def NewPoem(request, pk):
    poem = get_object_or_404(Poem, pk=pk)

    if request.method == "POST":
        form = NewPoemForm(request.POST)

# Create your views here.
