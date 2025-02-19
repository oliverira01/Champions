from Tanda import Tanda
from Equipo import Equipo
from Jugador import Jugador
import time, os

jugadores = []
dorsales = []

nombre = input("Nombre del portero: ")
dorsal_elegido = False
while dorsal_elegido == False:
    dorsal = int(input("Dorsal del portero (obligatorio 1 o 13): "))
    if dorsal ==  1 or dorsal == 13 :
        dorsales.append(dorsal)
        dorsal_elegido = True
        break
    print("Dorsal diferente de 1 o 13")
jugador = Jugador(nombre, dorsal)
jugadores.append(jugador)

for i in range(5):
    nombre = input("Nombre del jugador: ")
    dorsal_elegido = False
    while dorsal_elegido == False:
        dorsal = int(input("Dorsal del jugador: "))
        if dorsal not in dorsales:
            dorsales.append(dorsal)
            dorsal_elegido = True
            break
        print("Dorsal ya escogido")
    jugador = Jugador(nombre, dorsal)
    jugadores.append(jugador)

nombre_equipo = input(f"Dime el nombre de tu equipo: ")
nombre_estadio = input(f"Dime en que estadio juega tu equipo: ")
equipo_jugador = Equipo(nombre_equipo, nombre_estadio, jugadores, True)

jugadores_bot = [Jugador("Pedro 🏥🚑", 7),Jugador("Darwin Núñez", 9),Jugador("Salah", 11),Jugador("Alexander Arnold", 66),Jugador("Van Dijk", 4),Jugador("Alisson", 1)]
equipo_bot = Equipo("Liverpool", "Anfield", jugadores_bot, False)

equipo_atacante = equipo_jugador
equipo_defensor = equipo_bot

tiros = 0

while True:
    indice_atacante, indice_defensor, equipo_atacante.lista_lanzadores = Tanda.elegir_jugadores({"lista_lanzadores": equipo_atacante.lista_lanzadores, "jugadores": equipo_atacante.jugadores}, {"lista_lanzadores": equipo_defensor.lista_lanzadores, "jugadores": equipo_defensor.jugadores}, tiros)
    print("--------------------------------------------------------------")
    print(f"RONDA {tiros + 1} | Portero: {equipo_defensor.jugadores[indice_defensor].nombre} | Lanzador: {equipo_atacante.jugadores[indice_atacante].nombre}")
    tiros += 1
    if not equipo_atacante.humano:
        equipo_atacante.jugadores[indice_atacante].generar_movimiento()
        equipo_defensor.jugadores[indice_defensor].elegir_movimiento()
    else:
        equipo_defensor.jugadores[indice_defensor].generar_movimiento()
        equipo_atacante.jugadores[indice_atacante].elegir_movimiento()
    Tanda.animaciones(equipo_atacante.jugadores, equipo_defensor.jugadores, indice_atacante, indice_defensor)
    if Tanda.comparar_equipos(equipo_atacante.jugadores[indice_atacante].movimiento, equipo_defensor.jugadores[indice_defensor].movimiento):
        equipo_atacante.goles += 1
        print(f"Goool de {equipo_atacante.jugadores[indice_atacante].nombre}\n{equipo_jugador.nombre} {equipo_jugador.goles} - {equipo_bot.nombre} {equipo_bot.goles}")
    else:
        print(f"Paradon de {equipo_defensor.jugadores[indice_defensor].nombre}\n{equipo_jugador.nombre} {equipo_jugador.goles} - {equipo_bot.nombre} {equipo_bot.goles}")
    if Tanda.comprobar_ganador(equipo_atacante.goles, equipo_defensor.goles, tiros):
        break
    if equipo_atacante == equipo_jugador:
        equipo_atacante = equipo_bot
        equipo_defensor = equipo_jugador
    else:
        equipo_atacante = equipo_jugador
        equipo_defensor = equipo_bot
    indice_atacante, indice_defensor, equipo_atacante.lista_lanzadores = Tanda.elegir_jugadores({"lista_lanzadores": equipo_atacante.lista_lanzadores, "jugadores": equipo_atacante.jugadores}, {"lista_lanzadores": equipo_defensor.lista_lanzadores, "jugadores": equipo_defensor.jugadores}, tiros)
    print("--------------------------------------------------------------")
    print(f"Portero: {equipo_defensor.jugadores[indice_defensor].nombre} | Lanzador: {equipo_atacante.jugadores[indice_atacante].nombre}")
    if not equipo_atacante.humano:
        equipo_atacante.jugadores[indice_atacante].generar_movimiento()
        equipo_defensor.jugadores[indice_defensor].elegir_movimiento()
    else:
        equipo_defensor.jugadores[indice_defensor].generar_movimiento()
        equipo_atacante.jugadores[indice_atacante].elegir_movimiento()
    Tanda.animaciones(equipo_atacante.jugadores, equipo_defensor.jugadores, indice_atacante, indice_defensor)
    if Tanda.comparar_equipos(equipo_atacante.jugadores[indice_atacante].movimiento, equipo_defensor.jugadores[indice_defensor].movimiento):
        equipo_atacante.goles += 1
        print(f"Goool de {equipo_atacante.jugadores[indice_atacante].nombre}\n{equipo_jugador.nombre} {equipo_jugador.goles} - {equipo_bot.nombre} {equipo_bot.goles}")
    else:
        print(f"Paradon de {equipo_defensor.jugadores[indice_defensor].nombre}\n{equipo_jugador.nombre} {equipo_jugador.goles} - {equipo_bot.nombre} {equipo_bot.goles}")
    if Tanda.comprobar_ganador(equipo_atacante.goles, equipo_defensor.goles, tiros):
        break
    if equipo_atacante == equipo_jugador:
        equipo_atacante = equipo_bot
        equipo_defensor = equipo_jugador
    else:
        equipo_atacante = equipo_jugador
        equipo_defensor = equipo_bot

ganador = Tanda.comprobar_goles(equipo_jugador, equipo_bot)
if ganador == 1:
    ganador = equipo_jugador
elif ganador == 2:
    ganador = equipo_bot

print("--------------------------------------------------------------")
print(f"🏆 {ganador.nombre.upper()} GANADOR DE LA CHAMPIONS 🏆")