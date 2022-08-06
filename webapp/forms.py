from django import forms

from webapp.models import Poll


class SearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label='Найти')


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question']
