from django.urls import path
from . import views
import receitas # o . é para acessarmos o diretório que está o arquivo

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:receita_id>', views.receita, name='receita')
]