
# Cet implémentation est basé sur l'algorithme de Poppenger, lui meme n'étant qu'une façon de détourner le résultat de n'importe quel algrothme produisant une chaine d'addition minimal de nombre input n. Cela est possible du fait que lors de l'exponentiation, les exponenents sont additionner.
# L'algorithme de chaine d'addition que nous avons choisie et celui des fractions contenues présenté par Bergson, Brlek, Berstel (1994).

import numpy as np
# numpy nous sera utile afin de calculer des logarithme en base 2.

def continious_fraction(n, k):
	U = []

	while True :
		u, v = divmod(n,k)
		U.append(u)

		n, k = k, v

		if v == 0 :
			break
	
	return U[::-1]


# Calcule les éléments de la fractions contenu de n/k et les retour dans l'ordre opposé a leur apparition.


def gcd(n, k):
	while k:
		n, k = k, n%k
	return n


# Calcule le plus grand diviseur commun de n et k.


def Q_func(u, q_0 ) :
	N = len(u)+1
	Q = [ 0 for _ in range(N) ]

	Q[0] = q_0
	Q[1] = q_0*u[0]

	for i in range(2, N) :
		Q[i] = Q[i-1]*u[i-1] + Q[i-2]

	return Q

# Calcule les éléments de la liste Q tel que spécifié dans l'article de référence.


def C(n, D):
	if np.log2(n)%1 == 0 :
		return [ 2**i for i in range( int(np.log2(n)) +1 ) ]
	else :
		return D[n]


# La méthode est récursive. C(n, D) va retourner la chaine d'addtion de n. si n est une puissance de 2 il s'agira de [1,2,4,8...,n]. Sinon celle-ci aura deja était calculer et enregistrer dans le dictionnaire D, il suffira de la retourner. 


def mul(a, b):
	b = [ a[-1]*i for i in b ]
	return a[:-1]+b

def add(a, b):
	return a+[ a[-1]+b ]


# Oppérateur de multiplication et d'addition spéciaux, tel que définie dans l'article de référence.


def X_func(Q, D, u):
	N = len(Q)
	X = [ 0 for _ in range(N) ]

	X[0] = C(Q[0], D)
	X[1] = mul( X[0], C(u[0], D) )

	for i in range(2, N) :
		X[i] =  add( mul(X[i-1], C(u[i-1], D)), Q[i-2])

	return X[-1]


# Calcule les éléments de la liste X tel que définie par l'article de référence. le dernier élément de cette liste correspondra à la chaine d'addition optimale.


def minProd(mode, s) :
	
	# on initialise le dictionnaire des chaine d'addition avec les valeurs de départ
	D = { 1:[1], 2:[1,2], 3:[1,2,3] }

	for n in range(4, s+1) : # liste des valeurs à tester
		chains = []          # chains contiendra toute les chaine d'addition de n étant de k, seul la meilleure sera retenu

		for k in range(2, n-1) : # toute les valeur de k à tester avc un n donné 

			# exécution de l'algorithme tel que décrit dans l'article de référence
			u = continious_fraction(n, k)
			Q = Q_func( u, gcd(n, k) )
			X = X_func(Q, D, u)
			
			chains.append( X )

		best = sorted( chains, key= lambda x : len(x) )[0]   # choix de la chaine la plus courte
		D[n] = best  # enregistrement de celle-ci dans un dictionnaire

	# en mode 'upto' c la somme qui sera retourner tel que demander dans l'exercice
	if mode == 'upto' :
		return sum( len(D[i])-1 for i in range(1, s) ) # la longeur de la chaine d'exponentiation minimal est
													   # égale a la (longeur de X)-1 (élément 1 de la chaine)

	# le mode 'only' permet de vérifier les valeurs des chaine calculer pour une entré donnée
	elif mode == 'only' :
		return len(D[s])-1, D[s]


s = 200
# print( minProd(mode='only', s=s) )
print( f"Somme des chaines d'exponentiatiations jusqu'a {s} = {minProd(mode='upto', s=s)}" )

