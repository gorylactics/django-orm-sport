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

		# 'dallas' : League.objects.filter(name__teams__contains = 'dallas')
		# 'dallas' : Team.objects.filter(league__name__contains='Dallas'),
		# 'dallas' : League.objects.filter(team_name__teams__contains = 'dallas'),
		# 'dallas': Team.objecst.filter(team_name__contains = 'dallas'),
		# todos los equipos con sede en Dallas

	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")