from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Genre, Poem
from .forms import NewPoemForm


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
            for text in genres_text:
                genres.append(Genre.objects.get_or_create(genre='genre'))

            poem = Poem(title=form.cleaned_data['title'],
                        text=form.cleaned_data['text'],
                        author=form.cleaned_data['author'],
                        )
            poem.genres.add(*genres)

            OldLinks = OldPoem.links.all()

            OldPoem.links.add(poem)
            OldPoem.links.add(OldLinks[1])
            OldPoem.save()

            poem.links.add(OldLinks[0])
            poem.links.add(Poem.objects.order_by('?'[:1][0]))
            poem.save()

            return redirect(poem)

        else:
            form = NewPoemForm()

        context = {
            'form': form,
        }

    return render(request, 'library/newPoem.html', context)

# Create your views here.
