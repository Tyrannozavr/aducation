from django.contrib import admin
from django import forms
from .models import *

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = '__all__'

    def clean(self):
        if self.cleaned_data.get('correct') == None:
            raise forms.ValidationError('Question must have at least one right answer')

        if list(self.cleaned_data.get('variants')) == list(self.cleaned_data.get('correct')):
            raise forms.ValidationError('All answers cant\'t be right')

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
