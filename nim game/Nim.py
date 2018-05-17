import numpy as np
import pickle

# produit le tableau du jeu dans la console

def display(pierre) :
	top = max( pierre.values() )
	for key, value in pierre.items():
		print( f"{key}|  " + "*"*value + " "*(top-value+2) + f"|{value}" )


# calcule les score et met a jour les scores dans le fichier pickle
# affiche la liste des meilleurs scores

def score(winner, loser, moves, data) :
	v = sum( i*(10**i) for i in range(1, moves+1) ) # calcule du score
	
	if winner in data :
		if v < data[winner]['best'] :
			data[winner]['best'] = v
		data[winner]['last'] = v
	else :
		data[winner] = { 'best' : v , 'last' : v }

	if loser in data :
		data[loser]['last'] = float('inf')
	else :
		data[loser] = { 'best' : float('inf') , 'last' : float('inf') }
	
	print('Meilleurs scores :')
	for n, s in enumerate( sorted( data.items(), key=lambda x : x[1]['best'] )) :
		i, j = s
		if n == 10 : # maximum de 10 scores afficher
			break
		else :
			print( f"{i} : {j['best']}" )

	with open( 'scores' , 'wb') as fp:
		pickle.dump( data , fp)


def Game() :
	## charge les anciens score si present
	try :
		with open( 'scores' , 'rb') as fp:
			data = pickle.load(fp)
	except :
		data = {}

	## enregistre les joueurs
	a = input('Entrer votre nom, Joueur 1 : ')
	b = input('Entrer votre nom, Joueur 2 : ')
	Joueurs = [a, b]

	## crée la table de jeu
	pierre = {}
	for tas in range( 3 + int(np.random.random(1)*5) ) :
		pierre[tas+1] = 5 + int(np.random.random(1)*19)
	display(pierre)

	## choisi le premier joueur au hasard et initialise le nombre de coups
	n = int( np.random.random(1)<0.5 )
	moves = 0

	## jeu a proprement dit
	while sum( pierre.values() ) > 1 :
		a = input(f"{ Joueurs[n%2] } veillez entrer votre coups : ")
		a = a.split('-')

		moves += 1

		# teste si les valeur entrer forment un coups valide
		if eval(a[0]) not in pierre.keys() :
			print("Coups illégal, veillez rejouer")
			continue
		else :
			if pierre[ eval(a[0]) ] - eval(a[1]) < 0 or eval(a[1]) == 0 :
				print("Coups illégal, veillez rejouer")
				continue
			else :
				pierre[ eval(a[0]) ] -= eval(a[1])

		# met a jour la table de jeu
		display(pierre)
		n += 1  # donne le tour au joueur suivant
	
	# condition de fin de jeu et affichage des scores
	if sum( pierre.values() ) == 1 :
		winner, loser = Joueurs[(n+1)%2], Joueurs[n%2]
	else :
		winner, loser = Joueurs[n%2], Joueurs[(n+1)%2]
	
	score(winner, loser, moves, data)

	# propose de continuer ou quiter le jeu
	a = input ("Entre oui pour démarrer une nouvelle partie, non pour quitter : ")
	if a == 'oui' :
		Game()

Game()