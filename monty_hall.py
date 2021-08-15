"""Program symulujący rozgrywkę według Problemu Monty'ego Halla i
pozwalający na garficzne zareprezentowanie statystyk wyników,
przemawiających na korzyść argumentu, że zamiana bramki daje dwukrotnie
większe prawdopodobieństwo wygranej (około 66% zamiast 33%).
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
#Utowrzenie list, które będą zawierały informacje o procentach i liczbie
#zwycięstw przy każdej kolejnej rozgrywce.
procent_zwyciestw = []
zwycieskie_wyniki = []
liczba_wynikow = []
#Uzupełnienie list z danymi, w zależności od wyniku kazdej rozgrywki.
aktualny_wynik = 0
for wynik in wyniki:
	#Jeżeli wynik poszczególnej rozgrywki był pozytywny, zostaje
	#dołączony do zbioru zwycięstw.
	if wynik == "Wygrana":
		zwycieskie_wyniki.append(wynik)
	aktualny_wynik += 1
	liczba_wynikow.append(aktualny_wynik)
	#Oblicznie procent zwycięstw w stosunku do liczby przeprowadzonych
	#gier.
	procent_zwyciestw.append(len(zwycieskie_wyniki)/aktualny_wynik*100)
#Utworzenie wykresu który pokazuje łączny procent zwycięstw przy kazdym
#kolejnym wyniku.
fig=pyplot.figure(dpi=90, figsize=(14, 9))
pyplot.plot(liczba_wynikow, procent_zwyciestw, c="blue", alpha=0.9)
#Tytuł wykrasu będzie zależał od wybranego typu rozgrywki.
if decyzja == "y":
	pyplot.title("Procent zwycięstw przy wyborze zamiany bramki",
	             fontsize=15)
else:
	pyplot.title("Procent zwycięstw przy wyborze pozostawienia bramki",
	             fontsize=15)
pyplot.ylabel("Procent zwycięstw", fontsize=10)
pyplot.xlabel("Liczba rozgrywek", fontsize=10)
#Pokazanie wykresu.
pyplot.show()
