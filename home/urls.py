from django.urls import path
from .views import home, my_logout
'''utilizar quando eu quiser mostrar uma pg html estática'''
from django.views.generic.base import TemplateView
from .views import HomePageView


urlpatterns = [
    path('', home, name="home"),
    path('logout/', my_logout, name="logout"),
    path('home2/',TemplateView.as_view(template_name='home2.html')),
    path('home3/',HomePageView.as_view(template_name='home3.html')),
]