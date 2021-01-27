import glob
from django.http import JsonResponse
import os
from mysite.settings.base import PROJECT_DIR, BASE_DIR
from wagtail.project_template.project_name.settings.base import BASE_DIR




def getChapters(request):
    manga = request.GET['manga']
    path = '' + PROJECT_DIR.replace('mysite','AtackTitans') + '\\static\\img\\' + manga + '\\*'
    path = path.replace('\\', '/')
    chapters = glob.glob(path)
    chapters = [i.split('\\')[-1].replace('\\', '/') for i in chapters]

    return JsonResponse({'manga': manga, 'chapters': chapters,'curdir':PROJECT_DIR.replace('mysite','AtackTitans')})



def getLinks(request):
    manga = request.GET['manga']
    chapter = request.GET['chapter']
    path = "" + PROJECT_DIR.replace('mysite','AtackTitans') + "\\static\\img\\" + manga + "\\" + chapter + "\\*.*"
    path = path.replace('\\', '/')
    pages = glob.glob(path)
    pages = ['/static' + i.split("static")[1] + '' for i in pages]
    pages = [i.replace('\\','/') for i in pages]


    return JsonResponse({'manga': manga, 'chapter': chapter, 'pages': pages})



