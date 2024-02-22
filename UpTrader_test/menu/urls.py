from django.urls import path
import menu.views as menu

urlpatterns = [
    path('', menu.index, name='index'),
    path(r'^(\d+)', menu.index, name='index')
]