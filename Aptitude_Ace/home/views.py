from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import JsonResponse
from .models import Question, Action
from datetime import datetime


@login_required
def home(request):
    questions = Question.objects.all()

    current_user = Action.objects.filter(user_id=request.user.id)
    no_of_attempt = get_no_of_attempted_ques(current_user)
    no_of_solved = get_no_of_solved_ques(current_user)
    total_score = get_total_score(current_user)
    league_level = get_league_level(current_user)

    return render(
            request,
            "home/home.html",
            {
                'questions': questions,
                'no_of_attempt': no_of_attempt,
                'no_of_solved': no_of_solved,
                'total_score': total_score,
                'league_level': league_level,
            }
        )


# function to get number of attempted question by a users
def get_no_of_attempted_ques(current_user):
    no_of_attempt = current_user.filter(attempted=True)
    return to_count(no_of_attempt)


# function to get number of question successfully solved by users
def get_no_of_solved_ques(current_user):
    no_of_solved = current_user.filter(solved=True)
    return to_count(no_of_solved)


# function to get total score of a specific user
def get_total_score(current_user):
    if current_user.exists():
        return current_user.aggregate(Sum('score'))['score__sum']
    else:
        return "---"


# function to get league level
def get_league_level(current_user):
    current_score = get_total_score(current_user)
    if current_score == "---":
        return "---"
    elif current_score < 10:
        return "Bronze"
    elif current_score < 20:
        return "Silver"
    elif current_score < 30:
        return "Gold"
    elif current_score < 40:
        return "Crystal"
    elif current_score < 50:
        return "Master"
    elif current_score < 60:
        return "Champion"
    elif current_score < 70:
        return "Titan"
    elif current_score < 80:
        return "Legend"


# function to count
def to_count(current_user_attempt):
    if current_user_attempt.exists():
        return current_user_attempt.count()
    else:
        return "---"


@login_required
def check_answer(request):
    choosenOption = request.GET.get('choosenOption', None)
    q_id = request.GET.get('q_id', None)
    correct_option = Question.objects.get(id=q_id).correct_option
    is_correct = correct_option == choosenOption
    scoreUpdate(q_id, request, is_correct)
    data = {
        'is_correct': is_correct,
        'correct_option': correct_option,
    }
    return JsonResponse(data)


def scoreUpdate(q_id, request, is_correct):
    current_user = request.user.id
    current_user_actions = Action.objects.filter(user_id=current_user)
    action_on_given_question = current_user_actions.filter(question_id=q_id)
    acted_on_given_question = action_on_given_question.exists()
    if not acted_on_given_question:
        if is_correct:
            a = Action(
                solved=True,
                attempted=True,
                score=5,
                score_date=datetime.now(),
                user_id=current_user,
                question_id=q_id,
            )
            a.save()
        else:
            a = Action(
                solved=False,
                attempted=True,
                score=-1,
                score_date=datetime.now(),
                user_id=current_user,
                question_id=q_id,
            )
            a.save()
