from . import views

from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.detail, name='detail'),
    path('tinymce/', include('tinymce.urls')),
]