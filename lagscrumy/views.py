from django.shortcuts import render
from django.http import HttpResponse
from .models import ScrumyUser

def index(request):
    return HttpResponse('You are at Lagscrumy')


def add_user(request):
    scrumyuser_list=ScrumyUser.objects.all()
    output=','.join([u.username for u in ScrumyUser_list])
    return HttpResponse(output)


def move_goal(request,task_id):
    return HttpResponse(task_id)
