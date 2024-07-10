# reviews/urls.py
from django.urls import path
from .views import RegisterView, LoginView
from .views import MovieListView, MovieDetailView
from .views import ReviewListView, ReviewDetailView
from .views import RecommendationView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
     path('recommendations/', RecommendationView.as_view(), name='recommendations'),
]
