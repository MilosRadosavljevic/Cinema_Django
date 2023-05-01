from django.db import models
from django.utils.text import slugify

# Create your models here.
class Question(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    question_text = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class Event(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    event_image = models.ImageField(upload_to="images/events/")

    def __str__(self):
        return self.name


class PartnerBrand(models.Model):
    name = models.CharField(max_length=200)
    brand_image = models.ImageField(upload_to="images/partner_brands/")

    def __str__(self):
        return self.name


class Subscribe(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class Writter(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Director(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Actor(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        return super(Genre, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    duration_minutes = models.IntegerField()
    poster_image = models.ImageField(upload_to="images/movie_posters/")
    slug = models.SlugField(max_length=200, unique=True)
    is_popular = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    is_upcoming = models.BooleanField(default=False)
    genres = models.ManyToManyField(Genre, related_name='films')
    writters = models.ManyToManyField(Writter, related_name='films')
    directors = models.ManyToManyField(Director, related_name='films')
    actors = models.ManyToManyField(Actor, related_name='films')

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Projection(models.Model):
    show_time = models.DateTimeField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    available_seats = models.IntegerField(default=100)
    taken_seats = models.IntegerField(default=0)

    def __str__(self):
        self.show_time = self.show_time.replace(tzinfo=None)
        return f"{self.movie.title} - {self.show_time.__format__('%d %b %Y %H:%M')}"
    
    
class Reservation(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    projection = models.ForeignKey(Projection, on_delete=models.CASCADE)
    number_of_tickets = models.IntegerField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.projection.movie.title} - {self.projection.show_time.__format__('%d %b %Y %H:%M')} - {self.number_of_tickets}"
    
    
    