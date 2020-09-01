from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    context = {
        'title': 'Página Principal',
        'content': 'Bem-vindo à página principal.'
    }

    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        'title': 'Página Sobre',
        'content': 'Bem-vindo à página sobre.'
    }

    return render(request, "about/about_page.html", context)


def contact_page(request):
    context = {
        'title': 'Página de contato',
        'content': 'Bem-vindo à página de contato.'
    }

    return render(request, "contact/contact_page.html", context)
