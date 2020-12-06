from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Genre, Poem, Report
from .forms import NewPoemForm, ReportForm
import uuid


def Random(request):
    page = Poem.objects.order_by('?')[:1][0]
    return redirect(page)


class Page(DetailView):
    model = Poem
    template_name = 'library/index.html'

    def get_context_data(self, **kwargs):
        poem = super().get_context_data(**kwargs)['object']
        context = {'title': poem.title,
                   'author': poem.author,
                   'timestamp': poem.timestamp,
                   'genres': poem.genres.all(),
                   'text': poem.text,
                   'leftLink': poem.leftLink,
                   'rightLink': poem.rightLink,
                   }

        return context


def NewPoem(request, pk):
    OldPoem = get_object_or_404(Poem, pk=pk)

    if request.method == "POST":
        form = NewPoemForm(request.POST)

        if form.is_valid():
            genres_text = form.clean_genres()
            genres = []
            for text in genres_text.split(", "):
                genre = Genre.objects.get_or_create(title="%s" % text)[0]
                genres.append(genre)

            poem = Poem.objects.create(title=form.cleaned_data['title'],
                                       text=form.cleaned_data['text'],
                                       author=form.cleaned_data['author'],
                                       )
            poem.save()
            for genre in genres:
                poem.genres.add(genre)

            oldLeftLink = OldPoem.leftLink

            OldPoem.leftLink = poem
            OldPoem.save()

            poem.leftLink = oldLeftLink
            poem.rightLink = Poem.objects.order_by('?')[:1][0]

            poem.save()

            return redirect(poem)

    else:
        form = NewPoemForm()

    context = {
        'form': form,
    }

    return render(request, 'library/newPoem.html', context)


def NewReport(request, pk):
    OldReport = get_object_or_404(Report, pk=pk)

    if request.method == "POST":
        form = ReportForm(request.POST)

        if form.is_valid():
            report = Report(
                text=form.cleaned_data['title'],
                type=form.cleaned_data['type'],
                poem=None  # TODO: pass poem into new report
            )

            report.save()
            return redirect(report)

    else:
        form = NewPoemForm()

    context = {
        'form': form,
    }

    return render(request, 'library/newReport.html', context)
