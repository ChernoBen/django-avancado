from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic.base import TemplateView



def home(request):
    return render(request, 'home.html')


def my_logout(request):
    logout(request)
    return redirect('home')

class HomePageView(TemplateView):
    template_name = 'home3.html'

    '''inserindo variavel no template
        talvez retornar um grande objeto p/ alimentar a pagina
    '''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['minha_variavel'] = 'Ola, seja bem vindo ao curso de django avançado'
        return context
