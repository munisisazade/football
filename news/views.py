from django.shortcuts import render
from django.views.generic import View
from threading import Thread
from django.http import HttpResponse
from news.tasks import python_shell
# Create your views here.


class MyTestView(View):

    def get(self,request,*args,**kwargs):
        background_task = Thread(target=python_shell)
        background_task.start()
        return HttpResponse("It works inshallah")