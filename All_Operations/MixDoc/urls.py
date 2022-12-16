from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home,name="home"),
    path('Os/', views.Os, name="Os"),
    path('courses/', views.courses, name="courses"),
    path('contactus/', views.contactus, name="contactus"),
    path('news/', views.news, name="news"),
    path('resume/', views.HomeView.as_view(), name="resume"),
    path('<int:pk>',views.candidateView.as_view(),name='candidate'),
    path('videogallery/', views.videogallery, name="videogallery"),

]