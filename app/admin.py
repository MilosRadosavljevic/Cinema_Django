from django.contrib import admin

from app.models import *


class MovieAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'duration_minutes', 'is_upcoming',
                    'is_new', 'is_popular', 'slug')
    list_filter = ('is_new', 'is_popular', 'is_upcoming',
                   'duration_minutes', 'directors', 'actors')
    search_fields = ('title', 'desc',)
    exclude = ('slug',)
    fieldsets = (
        ('Basic informations', {
            'fields': ('title', 'desc', 'genres', 'duration_minutes',),
        }),
        ('Other informations', {
            'fields': ('poster_image', 'is_popular', 'is_new', 'is_upcoming', 'actors', 'directors', 'writters',),
        }),
    )


class GenreAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('__str__', 'slug',)
    fields = ('name',)
    exclude = ('slug',)


class ActorAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name',)


class WritterAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name',)


class DirectorAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name',)


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email', 'date',)
    search_fields = ('email',)
    list_filter = ('date',)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('email', 'date',)
    search_fields = ('email',)
    list_filter = ('date',)
    
class ProjectionAdmin(admin.ModelAdmin):
    list_display = ('movie','show_time', 'available_seats', 'taken_seats')
    
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','number_of_tickets', 'projection')
    search_fields = ('first_name','last_name',)


# Register your models here.
admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Writter, WritterAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(PartnerBrand)
admin.site.register(Event)
admin.site.register(Subscribe, SubscribeAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Projection, ProjectionAdmin)
admin.site.register(Reservation,ReservationAdmin)


