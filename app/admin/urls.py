from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^student-list/$', views.StudentListView.as_view(), name='student-list'),
    url(r'^faculty-list/$', views.FacultyListView.as_view(), name='faculty-list'),
    url(r'^create-student/$', views.CreateStudentView.as_view(), name='create-student'),
    url(r'^create-faculty/$', views.CreateFacultyView.as_view(), name='create-faculty'),
]