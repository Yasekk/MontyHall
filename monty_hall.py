"""Program symulujący rozgrywkę według Problemu Monty'ego Halla i
pozwalający na garficzne zareprezentowanie statystyk wyników,
przemawiających na korzyść argumentu, że zamiana bramki daje dwukrotnie
większe prawdopodobieństwo wygranej.
"""

from random import choice
from matplotlib import pyplot

#Możliwośc wyboru liczby rozgrywek, jakie zostaną zasymulowane.
liczba = int(input("Podaj liczbę losowań: "))
#Wybór, czy w każdej rozgrywce bramka ma zostać zamieniona.
decyzja = input("Czy w losowaniach masz zawsze zmieniać bramkę czy nie?"
                +" y/n: ")
#Lista, która będzie zawierała zbiór wyników z każdej rozgrywki.
wyniki=[]

 
def losowanie(decyzja):
	"""Funkcja symulująca pojedyńczą rozgrywkę i zwracająca wynik jako
	'przegrana' lub 'wygrana'.
	"""
	bramki = ["bramka 1", "bramka 2", "bramka 3"]
	#Losowanie, która bramka zawiera zwycięstwo.
	dobra_bramka = choice(bramki)
	#Losowanie wybranej bramki (symulowanie ślepego wyboru gracza)
	wybrana_bramka = choice(bramki)
	#Usunięcie wybranej bramki z listy (która przechowywana teraz będzie
	#w zmiennej 'wybrana_bramka'.
	bramki.remove(wybrana_bramka)
	while True:
		#Usunięcie jednej z pozotałych bramek, która nie zawiera
		#zwycięstwa (symulowanie odsłonięcia jej i ukazania, że jest
		#pusta).
		eliminowana_bramka = choice(bramki)
		if eliminowana_bramka != dobra_bramka:
			bramki.remove(eliminowana_bramka)
			break
	if decyzja == "y":
		#Zamiana pierwotnie wybranej bramki na drugą (pozostałą)
		#nieodsłoniętą bramkę, jeżeli taki był pierwotny wybór gracza.
		wybrana_bramka = bramki[0]
	if wybrana_bramka == dobra_bramka:
		#Jeżeli obecnie wybrana bramka jest wygrywającą bramką,
		#następuje zwycięstwo.
		wynik = "Wygrana"
	else:
		#Jeżeli obecnie wybrana bramka nie jest wygrywającą bramką,
		#następuje przegrana.
		wynik = "Przegrana"	
	return wynik


#Powtórzenie rozgrywki tyle razy, ile zostało wybrane na początku i
#dodanie wyników każdej rozgrywki do listy 'wyniki'.
for x in range(liczba):
	wyniki.append(losowanie(decyzja))
#Skopiowanie listy wyników do nowej zmiennej, aby zachować oryginalną
#kolejnośc zwycięstw i przegranych.
ostateczne_wyniki=wyniki
#Usunięcie każdej przegranej z listy, tak aby pozostała lista
#zawierająca same zwycięstwa.
while "Przegrana" in wyniki:
		wyniki.remove("Przegrana")
#Oblicznie procent zwycięstw w stosunku do liczby przeprowadzonych gier.
procent_zwyciestw = len(wyniki)/int(liczba)*100
print("Liczba zwysięstw to "+str(procent_zwyciestw))
