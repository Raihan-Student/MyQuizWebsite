from django.contrib import admin
from .models import Subject, Question, Choice, QuizResult

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Subject)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(QuizResult)
# Register your models here.
