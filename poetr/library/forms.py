from django import forms


class NewPoemForm(forms.Form):
    title = forms.CharField(max_length=48, label='A title for your thoughts?', required=False)
    text = forms.CharField(widget=forms.Textarea, max_length=280, label='Go ahead and scream:', required=False)
    author = forms.CharField(max_length=48, label="Who are you (not) really?", required=False)
    genres = forms.CharField(max_length=280, label='Think inside the comma separated box:',
                             required=False)

    def clean_genres(self):
        data = self.cleaned_data['genres']
        return data


class ReportForm(forms.Form):

    REPORT_TYPE_CHOICES = [
        # use 4 letter keys
        ('nsfw', 'NSFW'),
        ('hrmt', 'HARASSMENT'),
        ('cprt', 'COPYRIGHT'),
        # and more
    ]
    type = forms.ChoiceField(
        choices=REPORT_TYPE_CHOICES,
        label="What's wrong?"
    )
    reportText = forms.CharField(widget=forms.Textarea, max_length=400, label="Tell us more:")
