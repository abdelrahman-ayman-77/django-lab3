from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from firstapp.models import Book 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    books = Book.objects.all()
    return render(request, 'books/home.html',{'books': books})
@login_required
def addpage(request):
    return render(request, 'books/add.html')
@login_required
def allbooks(request):
    books = Book.objects.all()
    return render(request, 'books/allbooks.html',{'books': books})
@login_required
def details(request,id):
    book = Book.objects.get(id=id)
    return render(request, 'books/details.html', {'book': book})
@login_required
def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        year = request.POST.get('year')
        book=Book(title=title,author=author,year=year)
        book.save()
        return redirect('home')
    else:
        return render(request, 'books/add.html',)
@login_required
def delete(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('home')
@login_required
def update(request, id):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        year = request.POST.get('year')
        book = Book.objects.get(id=id)
        book.title=title
        book.author=author
        book.year=year
        book.save()
        return redirect('home')
    else:
        book = Book.objects.get(id=id)
        return render(request, 'books/update.html', {'book': book})   

def register(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirmpassword')
        if password != confirm_password:
            return redirect('register')
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()
        return redirect('login')
    return render(request,'books/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')

    return render(request, 'books/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
