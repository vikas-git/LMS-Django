from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.hashers import make_password, check_password

from .forms import RegisterForm, LoginForm
from .models import User
from helpers.common import create_user_session

# Create your views here.
class RegisterView(TemplateView):
    template_name = 'user/register.html'
    form = RegisterForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form()} )
    
    def post(self, request):
        form = self.form(request.POST)

        if form.is_valid():
            data = {
                'name': request.POST.get('name'),
                'email': request.POST.get('email'),
                'password': make_password(request.POST.get('password')),
                'role': 3
            }
            try:
                userObj = User(**data)
                userObj.save()
                messages.success(request, 'User Registered successfully !!')
                return redirect('login')
            except IntegrityError as e:
                messages.error(request, "This email is already exists Please try with another email")

        return render(request, self.template_name, {'form': form} )        


class LoginView(TemplateView):
    template_name = 'user/login.html'
    form = LoginForm

    def get(self, request):
        if 'userauth' in request.session:
            return redirect('student-list')

        return render(request, self.template_name, {'form': self.form()} )

    def post(self, request):
        if 'userauth' in request.session:
            return redirect('student-list')

        form = self.form(request.POST)

        if form.is_valid():
            try:
                user_email = request.POST.get('email')
                user_password = request.POST.get('password')
                user_obj = User.objects.get(email=user_email, role=3)
                if check_password(user_password, user_obj.password):
                    create_user_session(request, user_obj)
                    if user_obj.role == 3:
                        return redirect('student-list')
                else:
                    messages.error(request, "Invalid password.")
            except Exception as e:
                messages.error(request, str(e))

        return render(request, self.template_name, {'form': form})


class Logout(TemplateView):
    def get(self, request):
        role = request.session.get('userauth', {}).get('role')
        del request.session['userauth']
        messages.success(request, 'Logged out successfully')
        if role == 1:
            redirect_url = 'student-login'
        elif role == 2:
            redirect_url = 'faculty-login'
        else:
            redirect_url = 'admin-login'
        return redirect(redirect_url)