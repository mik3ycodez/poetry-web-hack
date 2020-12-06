from django.db import models
import uuid



class Genre(models.Model):
    genre = models.CharField(max_length=18)

    def __str__(self):
        return self.genre


# a model representing a poem within the application
class Poem(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=48, help_text="enter poem title")
    text = models.CharField(max_length=280, help_text="enter poem text")
    author = models.CharField(max_length=48, help_text="enter author")
    genres = models.ManyToManyField('Genre', blank=True)
    leftLink = models.ForeignKey('self', related_name="left_links", on_delete=models.CASCADE, blank=True, null=True)
    rightLink = models.ForeignKey('self', related_name="right_links", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/library/%i/' % self.pk


# a model representing a report from the user
class Report(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=400, help_text="describe why you are reporting this poem")
    poem = models.OneToOneField(
        Poem,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    REPORT_TYPE_CHOICES = [
        # use 4 letter keys
        ('nsfw', 'NSFW'),
        ('hrmt', 'HARASSMENT'),
        ('cprt', 'COPYRIGHT'),
        # and more
    ]
    type = models.CharField(
        max_length=4,
        choices=REPORT_TYPE_CHOICES,
        default='cprt',
    )
