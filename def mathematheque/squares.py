
def is_prime(x):
	isprime=True

	if x!=2:
		for i in range (2, int(x**(1/2)+1)):
			if x%i==0:
				isprime=False
				break

	return isprime


# La fonction is_prime(x) prend un entier pour input et retourne True si il est premier et False dans le cas contraire. Ce-ci est déterminer en divisant x sur tout les nombres plus petit que ça racine carré. 1 est considéré premier simplement parce que cela ne pose aucun problème par la suite, nous économisons donc une condition. 

def get_primes(start, stop):
	ensemble = set()
	
	for i in range(start, stop+1):
		if is_prime(i):
			ensemble.add(i)
	
	return ensemble


# Retourne tout les nombres premiers dans un interval donné en faisons appel à la fonction is_prime(). Elle retourne ces nombres dans un objet set().

def C(a, b):
	# vérification des condition élémentaire pour le bon déroulement de l'algorithme
	if b < 1 or b < a :
		print('Interval non valide')
		return

	if a < 1 :
		a = 1
		print(f"Interval non valide, on excecutera sur l'interval {a, b} ")
		
	
	# initialisition de l'interval dans un objet set()
	s = set( range(a, b+1) )
	
	# triage basique des élément de l'interval
	
	# 1. si a < b/2 alors tous les nombre premier dans l'interval (b//2+1, b) n'ont aucun multiple dans (a,b)
	# autre qu'eux meme, ils sont donc éliminés.
	if a < b/2 :
		s -= get_primes(b//2+1, b)

	# dans le cas contraire, il faudra non seulement éliminer les nombre premier dans tout l'interval (a+1, b)
	# mais aussi tous les multiples de ceux dans l'intraval (b-a+1, a) cas ils sont eux aussi uniques.
	else :
		s -= get_primes(a+1, b)
			
		for k in get_primes(b-a+1, a) :
			u = k*(b//k) 
			s -= set(u) if u**(1/2)%1 == 0 else set()
	
	# s est transformer en liste
	s = list(s)
	x, c = len(s), 0
	
	# cela nous permet de parcours tout les élément de la powerset de s une seule fois, et donc tester
	# toute les conbinaison possible sans répétition
	for i in range(1, 1 << x):
		A = [ s[j] for j in range(x) if (i & (1 << j)) ]
		
		# on multiplie tout les éléments de l'ensemble a teste et test si c'est un carré parfais 
		product = 1
		for n in A :
			product *= n

		# si oui on ajoute 1 au conteur
		if product**(1/2)%1 == 0 :
			c += 1
	
	# on retourne le conteur
	return c

print( f"nombre de carrés parfais formés par les éléments de l'interval fourni = {C(40,55)}" )

