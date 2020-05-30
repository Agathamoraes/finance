from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produto', views.produto_list, name='produto_list'),

]