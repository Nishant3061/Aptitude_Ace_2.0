from django import forms
from home.models import QuestionsTopic


class AddQuestionForm(forms.Form):
    topics = QuestionsTopic.objects.all()
    TOPIC_CHOICES = []
    for topic in topics:
        var = [topic.id, topic.topic_name]
        TOPIC_CHOICES.append(var)
    choose_topic = forms.ChoiceField(choices=TOPIC_CHOICES)

    question_text = forms.CharField(
        help_text="Enter your question here",
        widget=forms.Textarea,
        required=True,
        strip=True,
    )

    optionA = forms.CharField(required=True)
    optionB = forms.CharField(required=True)
    optionC = forms.CharField(required=True)
    optionD = forms.CharField(required=True)

    solution_text = forms.CharField(
        help_text="You can write hint of this question here",
        widget=forms.Textarea,
        required=False,
        strip=True,
    )
