from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("movies/", views.movies, name="movies"),
    path("movies/<slug:slug>", views.movie_page, name="movie_page"),
    path('genre/<slug:slug>', views.genre_page, name="genre_page"),
    path('events/', views.events, name="events"),
    path('about/', views.about_us, name="about_us"),
    path('contact/', views.contact_page, name="contact_page"),
    path('reservation/', views.reservation_page, name="reservation_page"),
]
