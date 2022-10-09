from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.db.models import Q

from .models import Movie, Person, Genre, Rating
from .forms import ReviewForm, RatingForm


class GetFilterItems:
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.all().values('year').distinct()


class MovieView(GetFilterItems, ListView):
    # Movie list
    model = Movie
    queryset = Movie.objects.all()
    template_name = 'movies/movie_list.html'
    paginate_by = 8


class SearchMovieView(ListView):
    paginate_by = 8

    def get_queryset(self):
        return Movie.objects.filter(name__icontains=self.request.GET.get("query"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["query"] = ''.join([f'query={self.request.GET.getlist("query")}&'])
        return context


class FilterMovieView(GetFilterItems, ListView):
    paginate_by = 8

    def get_queryset(self):
        queryset = Movie.objects.all()
        if 'genres' in self.request.GET:
            queryset = Movie.objects.filter(
                Q(genres__in=self.request.GET.getlist("genres")) | Q(year__in=self.request.GET.getlist("year"))
            ).distinct()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["year"] = ''.join([f'year={year}&' for year in self.request.GET.getlist("year")])
        context["genres"] = ''.join([f'genres={genre}&' for genre in self.request.GET.getlist("genres")])
        return context


class MovieDetailView(DetailView):
    # Details of chosen movie
    model = Movie
    slug_field = 'url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['star_form'] = RatingForm()
        return context

class AddRating(View):
    def get_user_id(self, request):
        forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if forwarded_for:
            ip = forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_user_id(request),
                movie_id=int(request.POST.get('movie')),
                defaults={'star_id': int(request.POST.get('star'))}
            )
            return HTTPResponse(status=201)
        else:
            return HTTPResponse(status=400)

class AddReview(GetFilterItems, View):
    # Reviews
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()
        return redirect(movie.get_adsolute_url())


class PersonDetailView(DetailView):
    model = Person
    template_name = 'movies/person_detail.html'
    slug_field = 'full_name'
