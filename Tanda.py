import random, os, time
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

    def comprobar_ganador(equipo1, equipo2, tiros):  
        if equipo1.goles > equipo2.goles + (5 - tiros):
            return True
        elif equipo2.goles > equipo1.goles + (5 - tiros):
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
        
    def animacionPortero(portero, lanzador, quieto):
        print(f"Y bajo palos, con el dorsal{portero.dorsal}")
        print(f"{portero.nombre.upper()}")
        if (quieto):
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

    def animacionLanzador(lanzador, fueraBola, quieto):
        if (quieto):
            print("                       ")
            print("                       ")
            print("          ●            ")
            print("         /|\\           ")
            print("         / \\           ")
        elif (lanzador.movimiento == 1 and fueraBola == False):
            print("      O                ")
            print("                       ")
            print("         \●            ")
            print("         \\|\\            ")
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
            print("         \\|\\            ")
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

    def animaciones(equipo_atacante, equipo_defensor, indice_atacante, indice_defensor):
        os.system("cls")
        Tanda.animacionPortero(equipo_defensor.jugadores[indice_defensor], equipo_atacante.jugadores[indice_atacante], True)
        Tanda.animacionLanzador(equipo_atacante.jugadores[indice_atacante], False, True)
        time.sleep(2)
        os.system("cls")
        Tanda.animacionPortero(equipo_defensor.jugadores[indice_defensor], equipo_atacante.jugadores[indice_atacante], True)
        Tanda.animacionLanzador(equipo_atacante.jugadores[indice_atacante], False, False)
        time.sleep(2)
        os.system("cls")
        Tanda.animacionPortero(equipo_defensor.jugadores[indice_defensor], equipo_atacante.jugadores[indice_atacante], False)
        Tanda.animacionLanzador(equipo_atacante.jugadores[indice_atacante], True, False)
        time.sleep(2)