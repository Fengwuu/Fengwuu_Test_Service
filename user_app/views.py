from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterUserForm, LoginUserForm
from .models import UserProfile
from .tasks import *

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'user_app/register.html'
    success_url = reverse_lazy('login')

    def post(self, request):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data.get('email'))
            send_reg_mail.delay(email=form.cleaned_data.get('email'), username=form.cleaned_data.get('username')) # celery task

            user = form.save()
            profile = UserProfile.objects.create(user=user)
            profile.avatar = 'photos/avatars/users/default.png'
            profile.save()
            user.save()
            login(request, user)

            return redirect('home')

        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'user_app/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')


def user_page(request, user_id):
    try:
        avatar = User.objects.get(pk=user_id).userprofile.avatar
    except:
        avatar = None

    nickname = User.objects.get(pk=user_id).username
    test_ready = list()
    try:
        tests_completed = User.objects.get(pk=user_id).userprofile.completed_tests.values('title')
        for test in tests_completed:
            test_ready.append(test['title'])
    except:
        test_ready = list()

    context = {'avatar': avatar,
               'nickname': nickname,
               'tests_completed': test_ready
               }

    return render(request, 'user_app/user_page.html', context=context)
