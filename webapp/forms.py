from django import forms

from webapp.models import Poll, Choice, Answer


class SearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label='Найти')


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question']


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['text']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['choice']
