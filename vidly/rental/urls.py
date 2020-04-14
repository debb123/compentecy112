from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('about', views.about,name='about'),
    path('<int:movie_id>',views.details, name='movies_detail'),
]