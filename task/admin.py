from django import forms
from django.conf import settings
from django.contrib import admin

from .forms import TaskForm
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    form = TaskForm
    list_display = ['title_display', 'is_done', 'created', 'updated']
    fieldsets = [
        ('Titles', {'fields': [f'title_{lang_code}' for lang_code, lang_name in settings.LANGUAGES]}),
        (None, {'fields': ['is_done']}),
    ]

    def get_form(self, request, obj=None, **kwargs):
        form = TaskForm
        form.base_fields['is_done'].widget = forms.CheckboxInput()
        return form

    def title_display(self, obj):
        return obj.title.get(settings.LANGUAGE_CODE, "")

    title_display.short_description = "Title"
