from django.contrib import admin

from .models import QuestionsTopic, Question

admin.site.register(QuestionsTopic)
admin.site.register(Question)
