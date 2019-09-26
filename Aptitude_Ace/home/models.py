from django.conf import settings
from django.db import models
from datetime import datetime

from addQuestion.models import Question


class Action(models.Model):
    """It's is the table which contains all the action done by user to any
        question (like score, likes , shares etc)"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET("Anonymus"),
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
    )

    solved = models.BooleanField(default=False)
    attempted = models.BooleanField(default=False)
    Bookmark = models.BooleanField(default=False)

    score = models.IntegerField(default=0)
    score_date = models.DateTimeField(blank=True, default=datetime.now)

    like = models.BooleanField(default=False)
    share = models.BooleanField(default=False)
    report_question = models.BooleanField(default=False)

    Last_action_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.user.first_name}--{self.question.question_text[:100]}'
