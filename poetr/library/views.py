from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Genre, Poem, Report
from .forms import NewPoemForm, ReportForm
import random
r = random.Random()


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
                   'leftLink': poem.leftLink.get_absolute_url(),
                   'rightLink': poem.rightLink.get_absolute_url(),
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
                genre.poems.add(poem)

            oldLeftLink = OldPoem.leftLink

            OldPoem.leftLink = poem
            OldPoem.save()

            poem.leftLink = oldLeftLink
            poem.rightLink = Poem.objects.order_by('?')[:1][0]
            poem.save()

            try:
                poemGenre = r.choice(poem.genres.all())
                poemChoice = r.choice(poemGenre.poems.all())
                if r.randint(0, 10) < 7:
                    poem.rightLink = poemChoice
                    poem.save()
            except Exception as e:
                pass

            while poem.rightLink.pk == poem.pk:
                print("Poem picked itself")
                poem.rightLink = Poem.objects.order_by('?')[:1][0]
                poem.save()

            r.choice(Poem.objects.all()).rightLink = r.choice(Poem.objects.all())
            return redirect(poem)

    else:
        form = NewPoemForm()

    context = {
        'form': form,
    }
    r.choice(Poem.objects.all()).rightLink = r.choice(Poem.objects.all())
    return render(request, 'library/newPoem.html', context)

def NewReport(request, pk):
    poem = get_object_or_404(Poem, pk=pk)

    if request.method == "POST":
        form = ReportForm(request.POST)

        if form.is_valid():
            report = Report.objects.create(
                text=form.cleaned_data['reportText'],
                type=form.cleaned_data['type'],
                poem=poem
            )

            report.save()
            return redirect('/library/')

    else:
        form = ReportForm()

    context = {
        'form': form,
    }

    return render(request, 'library/report.html', context)
