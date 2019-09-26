from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class QuestionsTopic(models.Model):
    """It contains all the topics name.
       Any question that will uploaded fetch topic name form this table"""

    topic_name = models.CharField(max_length=60)
    color = models.CharField(max_length=10, default="black")

    def __str__(self):
        return f'{self.topic_name}'


class Question(models.Model):
    """It holds all the question uploaded by all the users"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET("Anonymus"),
    )

    topic = models.ForeignKey(
        QuestionsTopic,
        on_delete=models.CASCADE,
    )

    question_text = models.CharField(max_length=1000)

    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)

    correct_option = models.CharField(max_length=200)

    hint = models.CharField(max_length=500, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.question_text[:200]}...'

    def get_uploader_name(self):
        uploader_obj = User.objects.get(id=self.user_id)
        return f'{uploader_obj.first_name} {uploader_obj.last_name}'

    def get_topic_name(self):
        temp = QuestionsTopic.objects.get(id=self.topic_id)
        return f'{temp.topic_name}'

    def get_color(self):
        temp = QuestionsTopic.objects.get(id=self.topic_id)
        return f'{temp.color}'

    class Meta:
        ordering = ('-date_created',)
