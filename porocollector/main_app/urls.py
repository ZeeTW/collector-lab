from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('poros/', views.poro_index, name= 'index'),
    path('poros/<int:poro_id>/', views.poros_detail, name='detail'),
    path('poros/create/', views.PoroCreate.as_view(), name='poros_create'),
    path('poros/<int:pk>/update', views.PoroUpdate.as_view(), name='poros_update'),
    path('poros/<int:pk>/delete', views.PoroDelete.as_view(), name='poros_delete'),
    path('poros/<int:poro_id>/add_feeding', views.add_feeding, name='add_feeding'),
    # CRUD for Toys using CBV's
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),

    # Associate a toy with a poro (M:M)
    path('poros/<int:poro_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),

    # Unassociate / Disassociate a toy with a poro (M:M)
    path('poros/<int:poro_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy')
]