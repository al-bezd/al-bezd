from django.urls import include, path
from .views import *
from django.views.generic import TemplateView
from .views import *
urlpatterns = [

    path('', TemplateView.as_view(template_name='AtackTitans/index.html')),
    path('getLinks/', getLinks),
    path('getChapters/', getChapters),
    path('getMangas/', getMangas),

]