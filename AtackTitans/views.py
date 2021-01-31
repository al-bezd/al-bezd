import glob
from django.http import JsonResponse
import os
from mysite.settings.base import PROJECT_DIR, BASE_DIR
from wagtail.project_template.project_name.settings.base import BASE_DIR

image_titles = [
    {"name":"AtackTitans","title_image":"https://pbs.twimg.com/media/D12AKs2XQAAD3Gn.jpg"}
]

def getMangas(request):
    path = '' + PROJECT_DIR.replace('mysite','AtackTitans') + '\\static\\img\\*'
    path = path.replace('\\', '/')
    mangas = glob.glob(path)
    mangas = [i.replace('\\', '/').split('/')[-1] for i in mangas]
    m=[]
    for i in mangas:
        if i == "AtackTitans":
            m.append({'title': i, 'title_image': 'https://pbs.twimg.com/media/D12AKs2XQAAD3Gn.jpg'})
        else:
            m.append({'title': i, 'title_image': ''})




    return JsonResponse({'mangas': m})


def getChapters(request):
    manga = request.GET['manga']
    path = '' + PROJECT_DIR.replace('mysite','AtackTitans') + '\\static\\img\\' + manga + '\\*'
    path = path.replace('\\', '/')
    chapters = glob.glob(path)
    chapters = [i.replace('\\', '/').split('/')[-1] for i in chapters]

    return JsonResponse({'manga': manga, 'chapters': chapters})



def getLinks(request):
    manga = request.GET['manga']
    chapter = request.GET['chapter']
    path = "" + PROJECT_DIR.replace('mysite','AtackTitans') + "\\static\\img\\" + manga + "\\" + chapter + "\\*.*"
    path = path.replace('\\', '/')
    pages = glob.glob(path)
    pages = ['/static' + i.split("static")[1] + '' for i in pages]
    pages = [i.replace('\\','/') for i in pages]


    return JsonResponse({'manga': manga, 'chapter': chapter, 'pages': pages})



