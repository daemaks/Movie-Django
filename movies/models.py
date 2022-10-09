from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField("Category", max_length=50)
    description = models.TextField("Description")
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Person(models.Model):
    full_name = models.CharField(max_length=150)
    age = models.PositiveSmallIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='person/')

    def __str__(self):
        return self.full_name

    def get_adsolute_url(self):
        return reverse('person_detail_url', kwargs={'slug': self.full_name})

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'


class Genre(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField("Description")
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
        ordering = ['name']


class Movie(models.Model):
    name = models.CharField("Name", max_length=100)
    description = models.TextField("Description")
    trailer = models.TextField("Trailer", blank=True)
    poster = models.ImageField(upload_to='movies/')
    year = models.PositiveSmallIntegerField("Year")
    contry = models.CharField("Contry", max_length=50)
    director = models.ManyToManyField(Person, verbose_name='Director',
                                      related_name='film_director')
    actors = models.ManyToManyField(Person, verbose_name='Actors',
                                    related_name='film_actor')
    genres = models.ManyToManyField(Genre, verbose_name='Genres')
    premiere = models.DateField("Premiere")
    budget = models.PositiveIntegerField("Budget")
    box_office = models.PositiveIntegerField("Box office")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_adsolute_url(self):
        return reverse('movie_detail_url', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
        ordering = ['-year']


class Footage(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='footage/')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Footage'
        verbose_name_plural = 'Footage'


class RatingStar(models.Model):
    value = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return str(self.value)

    class Meta:
        ordering = ['-value']


class Rating(models.Model):
    ip = models.CharField(max_length=15)
    star = models.ForeignKey(
        RatingStar, on_delete=models.CASCADE, verbose_name='star')
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, verbose_name='movie')

    def __str__(self):
        return f'{self.movie} - {self.star}'

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Rating'


class Review(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    parent = models.ForeignKey(
        'self', verbose_name='Parent', on_delete=models.SET_NULL,
        null=True, blank=True)
    movie = models.ForeignKey(
        Movie, verbose_name='movie', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.movie}'

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Review'
