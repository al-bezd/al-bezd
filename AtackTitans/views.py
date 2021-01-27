import glob
from django.http import JsonResponse
import os


def getChapters(request):
    manga = request.GET['manga']
    path = '' + os.path.abspath(os.curdir) + '\\static\\img\\' + manga + '\\*'
    path = path.replace('\\', '/')
    chapters = glob.glob(path)
    chapters = [i.split('\\')[-1].replace('\\', '/') for i in chapters]
    #chapters = [i.split('\\')[-1] for i in chapters]
    if len(chapters) == 0:
        path = '' + os.path.abspath(os.curdir) + '\\AtackTitans\\static\\img\\' + manga + '\\*'
        path = path.replace('\\', '/')
        chapters = glob.glob(path)
        chapters = [i.split('\\')[-1].replace('\\', '/') for i in chapters]
        #chapters = [i.replace('\\', '/') for i in chapters]
    return JsonResponse({'manga': manga, 'chapters': chapters})



def getLinks(request):
    manga = request.GET['manga']
    chapter = request.GET['chapter']
    path = "" + os.path.abspath(os.curdir) + "\\static\\img\\" + manga + "\\" + chapter + "\\*.*"
    path = path.replace('\\', '/')
    pages = glob.glob(path)
    pages = ['/static' + i.split("static")[1] + '' for i in pages]
    pages = [i.replace('\\','/') for i in pages]
    if len(pages) == 0:
        path = "" + os.path.abspath(os.curdir) + "\\AtackTitans\\static\\img\\" + manga + "\\" + chapter + "\\*.*"
        path = path.replace('\\', '/')
        pages = glob.glob(path)
        pages = ['/static' + i.split("static")[1] + '' for i in pages]
        pages = [i.replace('\\', '/') for i in pages]

    return JsonResponse({'manga': manga, 'chapter': chapter, 'pages': pages})



