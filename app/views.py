from django.shortcuts import render
from app.forms import QuestionForm, SubscribeForm, ReservationForm
from app.models import *

def index(request):
    movies = Movie.objects.all()
    popular_movies = Movie.objects.filter(is_popular=True)
    new_movies = Movie.objects.filter(is_new=True)
    upcoming_movies = Movie.objects.filter(is_upcoming=True)
    genres = Genre.objects.all()
    partners = PartnerBrand.objects.all()
    subscribe_form = SubscribeForm()
    subscribe_message = ''

    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            request.session['subscribed'] = True
            subscribe_message = 'Uspešno ste se prijavili za newsletter! Hvala!'
            subscribe_form = SubscribeForm()
        else:
            subscribe_message = 'Greška prilikom prijave za newsletter'
    context = {
        'movies': movies,
        'popular_movies': popular_movies,
        'new_movies': new_movies,
        'upcoming_movies': upcoming_movies,
        'genres': genres,
        'partners': partners,
        'subscribe_form': subscribe_form,
        'subscribe_message': subscribe_message,
    }

    return render(request, 'app/index.html', context)


def movies(request):
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    popular_movies = Movie.objects.filter(is_popular=True)
    new_movies = Movie.objects.filter(is_new=True)
    upcoming_movies = Movie.objects.filter(is_upcoming=True)

    context = {
        'movies': movies,
        'genres': genres,
        'popular_movies': popular_movies,
        'new_movies': new_movies,
        'upcoming_movies': upcoming_movies,
    }

    return render(request, 'app/movies.html', context)


def movie_page(request, slug):
    movie = Movie.objects.get(slug=slug)

    context = {
        'movie': movie,
    }
    return render(request, 'app/movie.html', context)


def genre_page(request, slug):
    genre = Genre.objects.get(slug=slug)
    movies = Movie.objects.filter(genres=genre)
    genres = Genre.objects.all()

    context = {
        'genre': genre,
        'movies': movies,
        'genres': genres,
    }

    return render(request, 'app/genre.html', context)


def events(request):
    events = Event.objects.all()

    context = {
        'events': events,
    }

    return render(request, 'app/events.html', context)


def about_us(request):
    return render(request, 'app/about_us.html')


def contact_page(request):
    question_form = QuestionForm()

    if request.POST:
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question_form.save()
            question_form = QuestionForm()

    context = {
        'question_form': question_form,
    }

    return render(request, 'app/contact.html', context)


def reservation_page(request):
    reservation_form = ReservationForm()
    projection = Projection.objects.none()
    
    message = """Maksimalan broj karata za jednu rezervaciju je 5!
        Rezervacija karata (sa istim podacima) moguća je samo za jednu projekciju!
        """
        
    if request.POST:
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            projection_tmp = Projection.objects.get(pk = request.POST.get('projection'))
            tickets_tmp = request.POST.get('number_of_tickets')
            email = request.POST.get('email')
            if int(tickets_tmp) == 0 or int(tickets_tmp) < 0:
                message = "Neispravna vrednost u polju predvidjenom za broj karata!"
            else:
                if email_check(email) is True:
                    if seats(projection_tmp, tickets_tmp) is True:
                        if int(tickets_tmp) < 6:
                            projection_tmp.available_seats -= int(tickets_tmp)
                            projection_tmp.taken_seats += int(tickets_tmp)
                            first_name = request.POST.get('first_name')
                            last_name = request.POST.get('last_name')
                            projection_tmp.save()
                            reservation_form.save()
                            reservation_form = ReservationForm()
                            message = f"""
                                Uspesna rezervacija! Broj rezervisanih karata:
                                {tickets_tmp}, na ime {first_name} {last_name}.
                                Uživajte u filmu!
                            """
                        else:
                            message = """Podsećamo Vas da je maksimalan broj karata za jednu rezervaciju je 5!"""
                    else:
                        message = is_full(projection_tmp)
                else:
                        message = """
                            Rezervacija sa unetim podacima već postoji!
                            Podsećamo Vas da je rezervacija karata (sa istim podacima)
                            moguća je samo za jednu projekciju!
                        """
    context = {
        'reservation_form': reservation_form,
        'message':message,
        'projection': projection,
    }
    return render(request, 'app/reservation.html', context)

    
# fucntions for reservation_page START
def email_check(email_to_check):
    if Reservation.objects.filter(email=email_to_check):
        print(f"email vec postoji u sistemu : {email_to_check}")
        return False
    return True


def seats(projection_id, tickets):
    if (int(projection_id.available_seats) > int(tickets)) or (int(projection_id.available_seats) == int(tickets)):
        return True
    else:
        return False


def is_full(projection_id):
    if int(projection_id.available_seats) > 0:
        message = f"""
            Broj preostalih slobodnih mesta za film "{projection_id.movie.title}" je: {projection_id.available_seats}
        """
    else:
        message = """
            Broj rezervacija za izabranu projekciju je popunjen!
            Molimo izaberite drugi termin. Hvala!
        """
    return message
# fucntions for reservation_page END