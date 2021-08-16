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

		'AlexanderWyatt' : Player.objects.filter(first_name__contains = 'alexander') | Player.objects.filter(first_name__contains = 'Wyatt'),
		# todos los jugadores con nombre "Alexander" O nombre "Wyatt"


		# PARTE 2
		# 1 todos los equipos en la Atlantic Soccer Conference
		'atlanticSoccer' : Team.objects.filter(league__name__contains = 'Atlantic Soccer Conference'),

		# 2 todos los jugadores (actuales) en los Boston Penguins
		'actuales' : Player.objects.filter(curr_team__team_name__contains = 'Penguins'),

		# 3 todos los jugadores (actuales) en la International Collegiate Baseball Conference
		'actuales_baseball' : Player.objects.filter(curr_team__league__name__contains = 'Collegiate Baseball'),

		# 4 todos los jugadores (actuales) en la American Conference of Amateur Football con el apellido "López"
		'actuales_soccer' : Player.objects.filter(curr_team__league__name__contains = 'American Conference of Amateur Football') & Player.objects.filter(last_name__contains = 'Lopez'),

		# 5 todos los jugadores de fútbol
		'jugadoresFutbol' : Player.objects.filter(curr_team__league__sport__contains = 'football'),

		# 6 todos los equipos con un jugador (actual) llamado "Sophia"
		'sofia' : Team.objects.filter(curr_players__first_name__contains = 'sophia'),

		# 7 todas las ligas con un jugador (actual) llamado "Sophia"
		'sofia2' : League.objects.filter(teams__curr_players__first_name__contains = 'sophia'),

		#8 todos con el apellido "Flores" que NO (actualmente) juegan para los Washington Roughriders
		'flores' : Player.objects.filter(last_name__contains = 'flores').exclude(curr_team__team_name = 'Roughriders'),

		#9 todos los equipos, pasados y presentes, con los que Samuel Evans ha jugado
		'samuel' : Team.objects.filter(all_players__first_name__contains = 'samuel') &  Team.objects.filter(all_players__last_name__contains = 'Evans'),

		# 10 todos los jugadores, pasados y presentes, con los gatos tigre de Manitoba
		'tigres' : Player.objects.filter(all_teams__team_name__contains = 'Tiger-Cats'),

		# 11 todos los jugadores que anteriormente estaban (pero que no lo están) con los Wichita Vikings
		'Vikings' : Player.objects.filter(all_teams__team_name__contains = 'Vikings').exclude(curr_team__team_name = 'Vikings'),

		# 12 cada equipo para el que Jacob Gray jugó antes de unirse a los Oregon Colts
		'Jacob' : Team.objects.filter(all_players__first_name__contains = 'Jacob' ) & Team.objects.exclude(team_name = 'Colts'),

		# 13 todos llamados "Joshua" que alguna vez han jugado en Atlantic Federation of Amateur Baseball Players
		'noJoshua' : Player.objects.filter(first_name__contains = 'Joshua') & Player.objects.filter(all_teams__league__name__contains = 'Atlantic Federation of Amateur Baseball Players'),

		# 14 todos los equipos que han tenido 12 o más jugadores, pasados y presentes. (SUGERENCIA: busque la función de anotación de Django).
		'contar' : Team.objects.filter(location__contains = 'boston')








	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")