from django.contrib import admin
from .models import *


@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    list_filter = ['variants']


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_filter = ['testing']


admin.site.register(Testing)
admin.site.register(Attempts)
