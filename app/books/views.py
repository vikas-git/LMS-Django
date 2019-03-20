from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book

# Create your views here.

def index(request):
    books = Book.objects.all().order_by('-created_on')
    return render(request, 'books/index.html', {'books': books})


def add(request):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'author': request.POST.get('author'),
            'publisher': request.POST.get('publisher'),
            'price': int(request.POST.get('price')),
            'quantity': int(request.POST.get('quantity'))
        }
        try:
            userObj = Book(**data).save()
            messages.success(request, 'Book added successfully !!')
            return redirect('books-list')
        except Exception as e:
            messages.error(request, "Error: "+str(e))
    return render(request, 'books/add.html', {})


def delete(request, book_id):
    try:
        Book.objects.filter(id=book_id).delete()
        messages.success(request, 'Book deleted successfully !!')
    except Exception as e:
        messages.error(request, "Error: "+str(e))

    return redirect('books-list')