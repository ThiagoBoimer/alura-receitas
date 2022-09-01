from unicodedata import name
from django.urls import path
from . import views # o . é para acessarmos o diretório que está o arquivo

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:receita_id>', views.receita, name='receita'),
    path('buscar', views.buscar, name='buscar')
]