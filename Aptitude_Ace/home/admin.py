from django.contrib import admin

from .models import QuestionsTopic, Question, Action

admin.site.register(QuestionsTopic)
admin.site.register(Question)
admin.site.register(Action)
