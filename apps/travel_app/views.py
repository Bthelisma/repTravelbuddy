# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User
from .models import Trip
from django.contrib import messages

#==================================================#
#                  RENDER METHODS                  #
#==================================================#

def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, "travel_app/index.html", context)

def addplan(request):
    return render(request, "travel_app/new.html")


def dashboard(request):
    try:
        context = {
            'user': User.objects.get(id=request.session['user_id']),
            'my_trips':Trip.objects.filter(travellers=request.session['user_id']),
            'other_plans': Trip.objects.exclude(travellers=request.session['user_id']),
        }
        return render (request, "travel_app/dashboard.html", context)

    except KeyError:
        return redirect('/')

def show(request, id):

    context={

        'trip':Trip.objects.get(id=id),
        'jointrips': Trip.objects.exclude(travellers =request.session['user_id'])

    }
    return render (request, "travel_app/show.html", context)



#==================================================#
#                 PROCESS METHODS                  #
#==================================================#

def register(request):
    result = User.objects.register_validate(request.POST)
    if type(result) == list:
        for error in result:
            messages.error(request, error)
        return redirect('/')

    request.session['user_id'] = result.id

    return redirect('/dashboard')


def login(request):
    result = User.objects.login_validate(request.POST)
    if type(result) == list:
        for error in result:
            messages.error(request, error)
        return redirect ("/")

    request.session['user_id'] = result.id

    return redirect("/dashboard")

def logout(request):
    request.session.clear()
    return redirect('/')

def create(request):
    result = Trip.objects.trip_validate(request.POST, request.session['user_id'])
    if type(result) == list:
        for error in result:
            messages.error(request, error)
        return redirect ("/addplan")
    return redirect('/dashboard')

def join(request, id):
    other_plans = Trip.objects.get(id=id)
    user=User.objects.get(id=request.session['user_id'])
    user.joiner.add(other_plans)
    return redirect('/dashboard')
