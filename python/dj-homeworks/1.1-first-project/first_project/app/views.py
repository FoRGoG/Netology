from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os

def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    time_format = "%Y-%m-%d %H:%M:%S"
    msg = f'Текущее время: {datetime.datetime.now():{time_format}}'
    return HttpResponse(msg)


def workdir_view(request):
    return HttpResponse('\n'.join(os.listdir('.')))