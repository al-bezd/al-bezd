from django.urls import include, path
from .views import *
from django.views.generic import TemplateView
urlpatterns = [

    path('', TemplateView.as_view(template_name='AtackTitans/index.html')),

]