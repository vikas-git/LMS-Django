from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.db import IntegrityError
from user.models import User


class StudentListView(TemplateView):
    def get(self, request):
        students = User.objects.filter(role=1).order_by('-created_on')
        return render(request, 'admin/student_list.html', {'students': students} )


class FacultyListView(TemplateView):
    def get(self, request):
        user_id = request.session.get('userauth', {}).get('user_id')
        faculties = User.objects.filter(role=2).order_by('-created_on')
        return render(request, 'admin/faculty_list.html', {'faculties': faculties} )


class CreateStudentView(TemplateView):
    def get(self, request):
        return render(request, 'admin/student_create.html', {} )
    
    def post(self, request):
        data = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'password': make_password(request.POST.get('password')),
            'mobile': request.POST.get('mobile'),
            'role': 1
        }
        try:
            userObj = User(**data)
            userObj.save()
            messages.success(request, 'User Registered successfully !!')
            return redirect('student-list')
        except IntegrityError as e:
            messages.error(request, "This email is already exists Please try with another email")
        
        return render(request, 'admin/student_create.html', {} )


class CreateFacultyView(TemplateView):
    def get(self, request):
        return render(request, 'admin/faculty_create.html', {} )
    
    def post(self, request):
        data = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'password': make_password(request.POST.get('password')),
            'mobile': request.POST.get('mobile'),
            'role': 2
        }
        try:
            userObj = User(**data)
            userObj.save()
            messages.success(request, 'User Registered successfully !!')
            return redirect('faculty-list')
        except IntegrityError as e:
            messages.error(request, "This email is already exists Please try with another email")
        
        return render(request, 'admin/faculty_create.html', {} )
