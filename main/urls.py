from . import views

from django.urls import path, include

urlpatterns = [
path('tinymce/', include('tinymce.urls')),
    path('', views.index, name='index'),
    path('<slug:slug>/', views.detail, name='detail'),
    
]