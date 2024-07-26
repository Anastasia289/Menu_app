from django.shortcuts import render

from .models import Menu, MenuItem


def draw_menu(request, path):
    return render(request, 'menu/index.html',
                  {'menu_name': path.split('/')[0],
                   'menu_item': path.split('/')[-1]}
                  )


def index(request):
    return render(request, 'menu/index.html',
                  {'menus': Menu.objects.all()})
