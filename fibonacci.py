#Améliorer lalgo pour qu'il soit plus performant (Voir sur wiki) : approche iterative
#Implenter est Tester la performance des differents algorithmes
#Formules de Binet, Algo recursif Naif (fait), Algo Lineaires, Algo Recursif Terminal, Algo Co Recursif, Algo Logarithmique
def fibonacci(n):
	if n < 0 :
		if (n % 2):
			return abs(fibonacci(n+1)) + fibonacci(n+2)
		else :
			return -fibonacci(n+1) + fibonacci(n+2)
	if n >= 2 :
		return fibonacci(n-1) + fibonacci(n-2)
	else :
		return n

