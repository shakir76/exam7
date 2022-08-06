from django.contrib import admin

# Register your models here.
from webapp.models import Poll, Choice


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


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
