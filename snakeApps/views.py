from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import hashlib
from .models import Snake
from .forms import SnakeForm
from .admin import UserCreationForm

# Create your views here.

def default(request):
    return redirect('login')

@login_required(login_url='login')
def index(request):
    totalCount = Snake.objects.count()
    snake_list = Snake.objects.all()
    template = loader.get_template('snakeApps/index.html')
    context = {
        'snake_list': snake_list,
    }
    return HttpResponse(template.render(context, request))

# def page(request,page_id):
#     # page_id start at '1'
#     totalCount = Snake.objects.count()
#     offset = 10 * ( page_id - 1 )
#     snake_list = Snake.objects.all()[offset:10]
#     template = loader.get_template('snakeApps/index.html')
#     context = {
#       'snake_list': snake_list,
#       'page_id': page_id,
#       'TotalCount': totalCount,
#     }
#     return HttpResponse(template.render(context, request))

@login_required(login_url='login')
def loadAdd(request):
    snake_form = SnakeForm()
    return render(request, 'snakeApps/addForm.html', {
        'snake_form' : snake_form,
    })

@login_required(login_url='login')
def loadEdit(request,snake_id):
    snake = Snake.objects.get(pk=snake_id)
    snake_form = SnakeForm(instance=snake)
    return render(request, 'snakeApps/editForm.html', {
        'snake_form' : snake_form,
        'snake' : snake
    })

@login_required(login_url='login')
def add(request):
    form_with_data = SnakeForm(request.POST)
    form_with_data.save()
    return redirect('index')

@login_required(login_url='login')
def edit(request, snake_id):
    snake = Snake.objects.get(pk=snake_id)
    form = SnakeForm(request.POST, instance=snake)
    form.save()
    return redirect('index')

@login_required(login_url='login')
def delete(request, snake_id):
    snake = get_object_or_404(Snake, pk=snake_id)
    snake.delete()
    return redirect('index')

@login_required(login_url='login')
def deleteScientist(request, s_id):
    user = get_object_or_404(User, pk=s_id)
    user.delete()
    return redirect('scientist')

# def loadLogin (request):
#     login_form = LoginForm
#     return render(request, 'registration/login.html', { 'login_form': login_form, })
#
# def login (request):
#
#     if request.POST:
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             # A backend authenticated the credentials
#             login(request,user)
#             return redirect('index')
#         else:
#             # No backend authenticated the credentials
#             #login_form = LoginForm
#             return redirect('login')
#     else:
#         #login_form = LoginForm
#         return redirect('login')
#
# def logout(request):
#     return redirect('logout')

def loadRegistration(request):
    user_form = UserCreationForm()
    return render(request, 'userAccess/registration.html',{ 'user_form': user_form, })

def registration(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        username = form.clean_username
        password = form.clean_password2()
        user = form.save(commit=False)
        user.save()
            # Redirect to a success page.
        return redirect('login')
    else:
        return redirect('loadRegistration')

@login_required(login_url='login')
def scientist(request):
    user_list = User.objects.all()
    template = loader.get_template('userAccess/scientist.html')
    context = {
        'scientist_list': user_list,
    }
    return HttpResponse(template.render(context, request))

