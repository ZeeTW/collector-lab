from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('poros/', views.poro_index, name= 'index'),
    path('poros/<int:poro_id>/', views.poros_detail, name='detail'),
    path('poros/create/', views.PoroCreate.as_view(), name='poros_create')
]