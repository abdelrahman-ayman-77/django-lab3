from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse

trainees=[] 
def home(request):
    return render(request, 'books/home.html',{'trainees': trainees})

def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        track = request.POST.get('track')
        trainees.append({'name': name, 'email': email,'track': track})
        return redirect('home')
    else:
        return render(request, 'books/add.html', {'trainees': trainees})


def delete(request, id):
    trainees.pop(id)
    return redirect('home')

def update(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        track = request.POST.get('track')
        trainees[id] = {'name': name, 'email': email, 'track': track}
        return redirect('home')
    else:
        trainee = trainees[id]
        return render(request, 'books/update.html', {'trainee': trainee, 'id': id})    
