from multiprocessing import AuthenticationError
from django.shortcuts import render
from django.contrib.auth.hashers import check_password
from django.views.generic import FormView, View
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from .dto import RawAuthDTO, LoginDTO
from utils.exceptions import InvalidPassword
from .forms import SignUpForm, LoginForm
from repositories.auth_app_repository import AuthAppRepository
# Create your views here.


class SignUpView(View):
    form_class = SignUpForm
    initial = {"key": "value"}
    template_name = 'auth_app/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            second_name = form.cleaned_data['second_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if password == confirm_password:
                dto = RawAuthDTO(email=email, second_name=second_name,
                                 first_name=first_name, password=password)
                AuthAppRepository.register_user(auth_dto=dto)
            else:
                raise Exception('invalid password')

            return HttpResponseRedirect(reverse('login'))

        return render(request, self.template_name, {'form': form})


class LoginView(View):
    form_class = LoginForm
    initial = {"key": "value"}
    template_name = 'auth_app/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            dto = LoginDTO(email=email, password=password)
            user = AuthAppRepository.get_user_by_email_password(dto=dto)
            if user is not None:
                if check_password(dto.password, user.password):

                    # TODO разобраться с аутетнтификацией

                    user = authenticate(request=request)
                    login(request, user)
                else:
                    raise InvalidPassword
            return HttpResponseRedirect(reverse('content'))

        return render(request, self.template_name, {'form': form})
