import glob

from django.http import JsonResponse
import os
from django.shortcuts import render

# Create your views here.

from wagtail.project_template.project_name.settings.base import BASE_DIR, PROJECT_DIR
#import importlib.resources


def getLinks(request):
    manga = request.GET['manga']
    chapter = request.GET['chapter']
    pages = glob.glob(f'{os.path.abspath(os.curdir)}\\AtackTitans\\static\\img\\{manga}\\{chapter}\\*.*')
    pages = [f'/static{i.split("static")[1]}'.replace('\\','/') for i in pages]
    return JsonResponse({'manga':manga,'chapter':chapter,'pages':pages})

def getChapters(request):
    manga = request.GET['manga']
    #chapter = request.GET['chapter']
    chapters = glob.glob(f'{os.path.abspath(os.curdir)}\\AtackTitans\\static\\img\\{manga}\\*')
    chapters = [i.split('\\')[-1] for i in chapters]
    return JsonResponse({'manga': manga, 'chapters': chapters})
