from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import *
from apps.models import Goods
import datetime

@login_required
def ordering(request,**kwargs):#<-
    good_to_order = Goods.objects.get(id=kwargs.get('good_id',None)) #<-
    if request.method == 'POST':
        form = GoodsOrderingForm(request.POST)
        if form.is_valid():
            ordered_good = form.save(commit=False)
            ordered_good.good = good_to_order#<-
            ordered_good.buyer = request.user
            ordered_good.save()
            return HttpResponseRedirect('/user/ordering_success/')#<-
    else:
        form = GoodsOrderingForm()
    return render(request, 'ordering.html', {'form': form, 'next': 'ordering_success', 'good': good_to_order})#<-



@login_required#<-
def ordering_success(request):#<-
    return render(request, 'ordering-success.html', {'section': 'dashboard'})#<-



@login_required
def dashboard(request):
    return render(request, 'info.html', {'section': 'dashboard'})#<-



@login_required
def commenting(request, **kwargs): #<-
    good_to_comment = Goods.objects.get(id=kwargs.get('good_id', None)) #<-
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.good = good_to_comment#<-
            review.user_name = request.user
            review.date = datetime.date.today()
            review.save()
            return HttpResponseRedirect('/user/')#<-
    else:
        form = CommentForm()
    return render(request, 'commenting.html', {'form': form, 'next': 'ordering_success', 'good': good_to_comment})#<-

