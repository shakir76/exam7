from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import SearchForm, PollForm
from webapp.models import Poll


class IndexPollView(ListView):
    model = Poll
    template_name = "poll/index.html"
    context_object_name = "polls"
    ordering = ("-created_at",)
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        if self.search_value:
            return Poll.objects.filter(
                Q(question__icontains=self.search_value))
        return Poll.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["form"] = self.form
        if self.search_value:
            query = urlencode({'search': self.search_value})
            context["query"] = query
            context["search"] = self.search_value
        return context

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get("search")


class PollView(DetailView):
    template_name = "poll/view.html"
    model = Poll


class CreatePoll(CreateView):
    form_class = PollForm
    template_name = "poll/create.html"


class UpdatePoll(UpdateView):
    form_class = PollForm
    template_name = 'poll/update.html'
    model = Poll


class DeletePoll(DeleteView):
    model = Poll
    template_name = 'poll/delete.html'
    success_url = reverse_lazy('index_poll')
