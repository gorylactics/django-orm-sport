from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		
		'baseball' : League.objects.filter(name__contains='baseball'),
		# todas las ligas de béisbol

		'baseball_mujeres': League.objects.filter(name__contains='women'),
		# todas las ligas de mujeres

		'hockey' : League.objects.filter(name__contains='hockey'),
		# todas las ligas donde el deporte es cualquier tipo de hockey

		'noFutbol' : League.objects.exclude(name = 'football'),
		# todas las ligas donde el deporte no sea football

		'conferencias' : League.objects.filter(name__contains = 'conference'),
		# todas las ligas que se llaman "conference"
		
		'atlantic' : League.objects.filter(name__contains = 'atlantic'),
		# todas las ligas de la región atlantic


		'dallas' : Team.objects.filter(location__contains = 'dallas'),
		# todos los equipos con sede en Dallas

		'raptors' : Team.objects.filter(team_name__contains = 'raptors'),
		# todos los equipos nombraron los Raptors

		'city' : Team.objects.filter(location__contains = 'city'),
		# todos los equipos cuya ubicación incluye "Ciudad"

		'T' : Team.objects.filter(team_name__startswith = 't'),
		# todos los equipos cuyos nombres comienzan con "T"

		'ubicacion' : Team.objects.all().order_by('location'),
		# todos los equipos, ordenados alfabéticamente por ubicación

		'inverso' : Team.objects.all().order_by('-team_name'),
		# todos los equipos, ordenados por nombre de equipo en orden alfabético inverso

		'cooper' : Player.objects.filter(last_name__startswith = 'cooper'),
		# cada jugador con apellido "Cooper"
		'joshua' : Player.objects.filter(first_name__startswith = 'joshua'),
		# cada jugador con nombre "Joshua"

		'joshuaCooper': Player.objects.filter(last_name__startswith = 'cooper').exclude(first_name = 'joshua'), 
		# todos los jugadores con el apellido "Cooper" EXCEPTO aquellos con "Joshua" como primer nombre

		'AlexanderWyatt' : Player.objects.filter(first_name__contains = 'alexander') | Player.objects.filter(first_name__contains = 'Wyatt')
		# todos los jugadores con nombre "Alexander" O nombre "Wyatt"


	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")