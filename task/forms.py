from django.conf import settings
from django import forms

from task.models import Task


class TaskForm(forms.ModelForm):
    """
    Custom form for the Task model. Dynamically generates fields for each language specified in LANGUAGES setting.
    """

    class Meta:
        model = Task
        fields = ('is_done',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for lang_code, lang_name in settings.LANGUAGES:
            self.fields[f'title_{lang_code}'] = forms.CharField(label=f'Title ({lang_name})', required=lang_code == settings.LANGUAGE_CODE)
            if self.instance.pk:
                self.initial[f'title_{lang_code}'] = self.instance.title.get(lang_code, '')

    def save(self, commit=True):
        task = super().save(commit=False)
        task.title = {lang_code: self.cleaned_data[f'title_{lang_code}'] for lang_code, lang_name in settings.LANGUAGES}
        if commit:
            task.save()
        return task