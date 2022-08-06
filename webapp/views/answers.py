from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from webapp.forms import AnswerForm
from webapp.models import Answer, Poll


class AnswerAdd(CreateView):
    form_class = AnswerForm
    model = Answer
    template_name = 'answers/view_answer.html'
    context_object_name = 'answers'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        context['poll'] = poll
        return context

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        form.instance.poll = poll
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('view_poll', kwargs={'pk': self.object.poll.pk})
