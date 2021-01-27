import glob

from django.http import JsonResponse
import os
from django.shortcuts import render

# Create your views here.

from wagtail.project_template.project_name.settings.base import BASE_DIR, PROJECT_DIR


# import importlib.resources


def getLinks(request):
    manga = request.GET['manga']
    chapter = request.GET['chapter']
    path = "" + os.path.abspath(os.curdir) + "\\AtackTitans\\static\\img\\" + manga + "\\" + chapter + "\\*.*"
    path = path.replace('\\', '/')
    pages = glob.glob(path)
    pages = ['/static' + i.split("static")[1] + '' for i in pages]
    return JsonResponse({'manga': manga, 'chapter': chapter, 'pages': pages})


def getChapters(request):
    manga = request.GET['manga']
    path = '' + os.path.abspath(os.curdir) + '\\AtackTitans\\static\\img\\'+manga+'\\*'
    path = path.replace('\\', '/')
    chapters = glob.glob(path)
    chapters = [i.split('\\')[-1] for i in chapters]
    if len(chapters)==0:
        chapters = ["087", "088", "089", "090", "091", "092", "093", "094", "095", "096", "097", "098", "099", "100", "101", "102",
         "103", "104", "105b", "106b", "107b", "108b", "109beta", "110beta", "111b", "112beta", "113b", "114bt",
         "115bt", "116bt", "117bt", "118"]
    return JsonResponse({'manga': manga, 'chapters': chapters})
