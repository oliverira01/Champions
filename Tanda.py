import random
class Tanda:
    
    def comparar_equipos(jugador1, jugador2):
        if jugador1.movimiento == jugador2.movimiento:
            return False
        else:
            return True
        
    def elegir_jugadores(equipo_atacante, equipo_defensor, tiros):
        if tiros < 6:
            elegido = False
            while elegido == False:
                jugador_atacante = random.randint(0,len(equipo_atacante.jugadores)-1)
                if jugador_atacante not in equipo_atacante.lista_lanzadores:
                    equipo_atacante.lista_lanzadores.append(jugador_atacante)
                    elegido = True
        else:
            jugador_atacante = random.randint(0,len(equipo_atacante.jugadores)-1)
        for i in range(len(equipo_defensor.jugadores)):
            if equipo_defensor.jugadores[i].dorsal == 1 or equipo_defensor.jugadores[i].dorsal == 13:
                jugador_defensor = i
                break
        return (jugador_atacante, jugador_defensor)

    def comprobar_media_ganador(equipo1, equipo2, tiros):
        if (equipo2.goles + (6 - tiros) == equipo1.goles) and tiros <= 5:
            return True        
        elif (equipo1.goles != equipo2.goles) and tiros > 5:
            return True
        else:
            return False

    def comprobar_ganador(equipo1, equipo2, tiros):
        if (equipo1.goles + (6 - tiros) == equipo2.goles) and tiros <= 5:
            return True        
        elif (equipo1.goles != equipo2.goles) and tiros > 5:
            return True
        else:
            return False
        
    def comprobar_goles(equipo1, equipo2):
        if equipo1.goles > equipo2.goles:
            return 1
        elif equipo2.goles > equipo1.goles:
            return 2
        else:
            return 0
        
    def animacionPortero(portero, lanzador):
        print(f"Y bajo palos, con el dorsal{portero.dorsal}")
        print(f"{portero.nombre.upper()}")
        if (portero.movimiento == 0):
            print("╔═════════════════════╗")
            print("║                     ║")
            print("║         ☻           ║")
            print("║        /|\\          ║")
            print("║        / \\          ║")
        elif (portero.movimiento == 1 and lanzador.movimiento == 1):
            print("╔═════════════════════╗")
            print("║                     ║")
            print("║   ☻                 ║")
            print("║   \\O\\               ║")
            print("║    \\ \\              ║")
        elif (portero.movimiento == 1 and lanzador.movimiento == 2):
            print("╔═════════════════════╗")
            print("║                     ║")
            print("║  \\☻\\     O          ║")
            print("║    \\                ║")
            print("║    \\ \\              ║")
        elif (portero.movimiento == 1 and lanzador.movimiento == 3):
            print("╔═════════════════════╗")
            print("║                     ║")
            print("║  \\☻\\            O   ║")
            print("║    \\                ║")
            print("║    \\ \\              ║")
        elif (portero.movimiento == 2 and lanzador.movimiento == 1):
            print("╔═════════════════════╗")
            print("║                     ║")
            print("║   O    \\☻/          ║")
            print("║         |           ║")
            print("║        / \\          ║")
        elif (portero.movimiento == 2 and lanzador.movimiento == 2):
            print("╔═════════════════════╗")
            print("║                     ║")
            print("║         ☻           ║")
            print("║        \\O/          ║")
            print("║        / \\          ║")
        elif (portero.movimiento == 2 and lanzador.movimiento == 3):
            print("╔═════════════════════╗")
            print("║                     ║")
            print("║        \\☻/      O   ║")
            print("║         |           ║")
            print("║        / \\          ║")
        elif (portero.movimiento == 3 and lanzador.movimiento == 1):
            print("╔═════════════════════╗")
            print("║                     ║")
            print("║   O           /☻/   ║")
            print("║               /     ║")
            print("║             / /     ║")
        elif (portero.movimiento == 3 and lanzador.movimiento == 2):
            print("╔═════════════════════╗")
            print("║                     ║")
            print("║         O     /☻/   ║")
            print("║               /     ║")
            print("║             / /     ║")
        elif (portero.movimiento == 3 and lanzador.movimiento == 3):
            print("╔═════════════════════╗")
            print("║                     ║")
            print("║                ☻    ║")
            print("║              /O/    ║")
            print("║             / /     ║")

    def animacionLanzador(lanzador, fueraBola):
        if (lanzador == 0):
            print("                       ")
            print("                       ")
            print("          ●            ")
            print("         /|\\           ")
            print("         / \\           ")
        elif (lanzador.movimiento == 1 and fueraBola == False):
            print("      O                ")
            print("                       ")
            print("         \●            ")
            print("         \|\            ")
            print("           |           ")
        elif (lanzador.movimiento == 2 and fueraBola == False):
            print("          O            ")
            print("                       ")
            print("          ●            ")
            print("         /|\\           ")
            print("         / L           ")
        elif (lanzador.movimiento == 3 and fueraBola == False):
            print("              O        ")
            print("                       ")
            print("          ●/           ")
            print("         /|/           ")
            print("         |             ")
        elif (lanzador.movimiento == 1 and fueraBola == True):
            print("                       ")
            print("                       ")
            print("         \●            ")
            print("         \|\            ")
            print("           |           ")
        elif (lanzador.movimiento == 2 and fueraBola == True):
            print("                       ")
            print("                       ")
            print("          ●            ")
            print("         /|\\           ")
            print("         / L           ")
        elif (lanzador.movimiento == 3 and fueraBola == True):
            print("                       ")
            print("                       ")
            print("          ●/           ")
            print("         /|/           ")
            print("         |             ")
        print(f"Para batir la porteria, con el dorsal{lanzador.dorsal}")
        print(f"{lanzador.nombre.upper()}")