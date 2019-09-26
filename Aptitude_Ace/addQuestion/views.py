from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Max

from home.models import Action
from .models import Question
from home.views import get_total_score
from .forms import AddQuestionForm


@login_required
def addQuestion(request):
    # to display score in the navbar
    current_user = Action.objects.filter(user_id=request.user.id)
    total_score = get_total_score(current_user)

    # to display addQues page when request is Post
    if request.method == 'POST':
        form = AddQuestionForm(request.POST)

        q_id = Question.objects.aggregate(Max('id'))
        if q_id['id__max'] is None:
            q_id['id__max'] = 0

        if form.is_valid():
            correct_option = request.POST.get('correct-option')
            if correct_option == 'option1':
                correct_option = form.cleaned_data['optionA']
            elif correct_option == 'option2':
                correct_option = form.cleaned_data['optionB']
            elif correct_option == 'option3':
                correct_option = form.cleaned_data['optionC']
            elif correct_option == 'option4':
                correct_option = form.cleaned_data['optionD']

            question = Question(
                q_id['id__max'] + 1,
                request.user.id,
                form.cleaned_data['choose_topic'],
                form.cleaned_data['question_text'],
                form.cleaned_data['optionA'],
                form.cleaned_data['optionB'],
                form.cleaned_data['optionC'],
                form.cleaned_data['optionD'],
                correct_option,
                form.cleaned_data['solution_text'],
            )
            question.save()

            return HttpResponseRedirect(reverse('home'))

    # to display addQues page when request is get
    else:
        form = AddQuestionForm()

    return render(
                    request,
                    'addQuestion/addQuestion.html',
                    {
                        'total_score': total_score,
                        'form': form,
                    }
                  )
