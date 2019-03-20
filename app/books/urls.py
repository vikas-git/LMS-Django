from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='books-list'),
    path('add', views.add, name='book-add'),
    url(r'^delete/(?P<book_id>[0-9]+)$', views.delete, name="book-delete"), 
]



