from django.urls import path
from . import views

urlpatterns = [
    path('', views.MovieView.as_view(), name='home_page_url'),
    path('filter/', views.FilterMovieView.as_view(), name='filter_page_url'),
    path('search/', views.SearchMovieView.as_view(), name='search_page_url'),
    path('rating/', views.AddRating.as_view(), name='add_rating_url'),
    path('<slug:slug>/', views.MovieDetailView.as_view(), name='movie_detail_url'),
    path('review/<int:pk>/', views.AddReview.as_view(), name='add_review_url'),
    path('person/<str:slug>/', views.PersonDetailView.as_view(), name='person_detail_url')
]
