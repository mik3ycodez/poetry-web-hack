from django import forms


class NewPoemForm(forms.Form):
    title = forms.CharField(max_length=48, label='A title for your thoughts?', required=False)
    text = forms.CharField(max_length=280, label='go ahead and scream', required=False)
    author = forms.CharField(max_length=48, label="Who are you (not) really?", required=False)
    genres = forms.CharField(max_length=280, label='put your work into lots of little comma separated boxes',
                             required=False)

    def clean_genres(self):
        data = self.cleaned_data['genres']
        return data.replace(' ', '').split(',')
