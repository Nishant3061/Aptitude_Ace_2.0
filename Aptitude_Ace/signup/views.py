from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect


def signup(request):
    if request.method == 'POST':

        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # TODO: check the uniquness of username i.e email

        user = User.objects.create_user(email, email, password)

        user.first_name = first_name
        user.last_name = last_name
        user.save()

        return HttpResponseRedirect('/accounts/login')

    else:
        return render(request, 'signup/signup.html')
