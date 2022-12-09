from django.contrib import admin
from django import forms
from .models import *

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = '__all__'

    def clean(self):
        if self.cleaned_data.get('question') == 'dmiv':
            raise forms.ValidationError('name incorrect')
        return self.cleaned_data

@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    list_filter = ['variants']


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_filter = ['testing']
    form = QuestionForm



admin.site.register(Testing)
admin.site.register(Attempts)
