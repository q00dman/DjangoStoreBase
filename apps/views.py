from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from apps.models import Goods
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from . import listfilter
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.admin.views.decorators import staff_member_required
from .models import Genre, Technique


def index(request, **kwargs):
    if kwargs.get('genre', None):
        a = Goods.objects.all().filter(genre=kwargs['genre'])
    elif kwargs.get('technique', None):
        a = Goods.objects.all().filter(technique=kwargs['technique'])
    else:
        a = Goods.objects.all()
    try:
        query = request.GET.get('q')
        a = Goods.objects.all().filter(title__istartswith=query)
    except:
        pass
    main_list = []
    genre_list = Genre.objects.all()
    technique_list = Technique.objects.all()
    for i in a:
        main_list.append(i.dict_transform())
    return render(request, 'interface\store.html', {
        'picture_list': main_list,
        'genre_list': genre_list,
        'technique_list': technique_list,
    })


def user(request):     # test
    q = Goods(author='Yasmine Bell', genre='пейзаж', technique='акварель', title='Valkirie flight', price=125)
    q.save()

    return HttpResponse('bober prishel')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


@staff_member_required
def add_goods(request):
    if request.method == 'POST':
        good_form = GoodsRegistrationForm(request.POST)
        if good_form.is_valid():
            new_good = good_form.save(commit=False)
            new_good.save()
    else:
        good_form = GoodsRegistrationForm()
    return render(request, 'interface/good_adding.html', {'good_form': good_form})


def info_board(request):
    return render(request, 'interface/website_info.html', {'section': 'dashboard'})#<-


def contact_form(request):
    return render(request, 'interface/contact_form.html', {'section': 'dashboard'})#<-

