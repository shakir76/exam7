from django.contrib import admin

# Register your models here.
from webapp.models import Poll, Choice, Answer


class PollAdmin(admin.ModelAdmin):
    list_display = ['id', 'question']
    list_display_links = ['question']
    list_filter = ['question', ]
    search_fields = ['question', ]
    fields = ['question']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'poll']
    list_display_links = ['text']
    list_filter = ['text', 'poll']
    search_fields = ['text', ]
    fields = ['text', 'poll']


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'poll', 'choice']
    list_display_links = ['poll']
    list_filter = ['choice', 'poll']
    search_fields = ['poll', ]
    fields = ['poll', 'choice']


admin.site.register(Answer, AnswerAdmin)
admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
