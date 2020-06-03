from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('produto', views.produto_list, name='produto_list'),
    path('produto/<int:pk>/', views.detail_prod, name='detail_prod'),
    path('add/', views.ProdutoCreate.as_view(), name='produto_add'),
    path('<int:pk>/edit/', views.ProdutoUpdate.as_view(), name='produto_edit'),
    path('<int:pk>/json/', views.produto_json, name='produto_json'),
    path('estoque', views.ent_estoque, name='ent_estoque'),
    path('estoque/<int:pk>/', views.ent_estoque_detail, name='ent_estoque_detail'),
    path('estoque/add/', views.ent_estoque_form, name='ent_estoque_form'),
]