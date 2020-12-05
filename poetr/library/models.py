from django.db import models


class Genre(models.Model):
    genre_title = models.CharField(max_length=18)

    def __str__(self):
        return self.genre_title


class Poem(models.Model):
    poem_timestamp = models.DateTimeField(auto_now_add=True)
    poem_title = models.CharField(max_length=48, help_text="enter poem title")
    poem_text = models.CharField(max_length=280, help_text="enter poem text")
    poetry_genres = models.ManyToManyField('Genre', blank=True)
    left_link = models.OneToOneField('Link')

    def __str__(self):
        return self.poem_title


class Link(models.Model):
    left_link = models.ForeignKey('poem', on_delete=models.CASCADE)
    right_link = models.ForeignKey('poem', on_delete=models.CASCADE)



class Report(models.Model):
    report_timestamp = models.DateTimeField(auto_now_add=True)
    report_text = models.CharField(max_length=400, help_text="describe why you are reporting this poem")
    report_poem = models.OneToOneField(
        Poem,
        on_delete=models.CASCADE,
        primary_key=True,
    )