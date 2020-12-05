from django.db import models


class Poem(models.Model):

    poem_timestamp = models.DateTimeField(auto_now_add=True);
    poem_title = models.CharField(max_length=48, help_text="enter poem title")
    poem_text = models.CharField(max_length=280, help_text="enter poem text")
    left_link = models.

    def __str__(self):
        return self.poem_title
