import random, os, time
class Tanda:
    
    def comparar_equipos(movimiento1: int, movimiento2: int) -> bool:
        if movimiento1 == movimiento2:
            return False
        else:
            return True
        
    def elegir_jugadores(equipo_atacante, equipo_defensor, tiros: int) -> tuple:
        if tiros < 6:
            elegido = False
            while elegido == False:
                jugador_atacante = random.randint(0,len(equipo_atacante["jugadores"])-1)
                if jugador_atacante not in equipo_atacante["lista_lanzadores"]:
                    equipo_atacante["lista_lanzadores"].append(jugador_atacante)
                    elegido = True
        else:
            jugador_atacante = random.randint(0,len(equipo_atacante["jugadores"])-1)
        for i in range(len(equipo_defensor["jugadores"])):
            if equipo_defensor["jugadores"][i].dorsal == 1 or equipo_defensor["jugadores"][i].dorsal == 13:
                jugador_defensor = i
                break
        return (jugador_atacante, jugador_defensor, equipo_atacante["lista_lanzadores"])

    def comprobar_ganador(goles_equipo1: int, goles_equipo2: int, tiros: int) -> bool:  
        if goles_equipo1 > goles_equipo2 + (5 - tiros):
            return True
        elif goles_equipo2 > goles_equipo1 + (5 - tiros):
            return True
        else:
            return False

    def comprobar_goles(goles_equipo1: int, goles_equipo2: int) -> int:
        if goles_equipo1 > goles_equipo2:
            return 1
        elif goles_equipo2 > goles_equipo1:
            return 2
        else:
            return 0
        
    def animacion_portero(portero: dict, lanzador: dict, quieto: bool) -> None:
        print(f"Y bajo palos, con el dorsal {portero["dorsal"]}")
        print(f"{portero["nombre"].upper()}")
        if (quieto):
            print("╔═════════════════════╗")
            print("║                     ║")
            print("║         ☻           ║")
            print("║        /|\\          ║")
            print("║        / \\          ║")
        elif (portero["movimiento"] == 1 and lanzador["movimiento"] == 1):
            print("╔═════════════════════╗")
            print("║                     ║")
            print("║   ☻                 ║")
            print("║   \\O\\               ║")
            print("║    \\ \\              ║")
        elif (portero["movimiento"] == 1 and lanzador["movimiento"] == 2):
            print("╔═════════════════════╗")
            print("║                     ║")
            print("║  \\☻\\     O          ║")
            print("║    \\                ║")
            print("║    \\ \\              ║")
        elif (portero["movimiento"] == 1 and lanzador["movimiento"] == 3):
            print("╔═════════════════════╗")
            print("║                     ║")
            print("║  \\☻\\            O   ║")
            print("║    \\                ║")
            print("║    \\ \\              ║")
        elif (portero["movimiento"] == 2 and lanzador["movimiento"] == 1):
            print("╔═════════════════════╗")
            print("║                     ║")
            print("║   O    \\☻/          ║")
            print("║         |           ║")
            print("║        / \\          ║")
        elif (portero["movimiento"] == 2 and lanzador["movimiento"] == 2):
            print("╔═════════════════════╗")
            print("║                     ║")
            print("║         ☻           ║")
            print("║        \\O/          ║")
            print("║        / \\          ║")
        elif (portero["movimiento"] == 2 and lanzador["movimiento"] == 3):
            print("╔═════════════════════╗")
            print("║                     ║")
            print("║        \\☻/      O   ║")
            print("║         |           ║")
            print("║        / \\          ║")
        elif (portero["movimiento"] == 3 and lanzador["movimiento"] == 1):
            print("╔═════════════════════╗")
            print("║                     ║")
            print("║   O           /☻/   ║")
            print("║               /     ║")
            print("║             / /     ║")
        elif (portero["movimiento"] == 3 and lanzador["movimiento"] == 2):
            print("╔═════════════════════╗")
            print("║                     ║")
            print("║         O     /☻/   ║")
            print("║               /     ║")
            print("║             / /     ║")
        elif (portero["movimiento"] == 3 and lanzador["movimiento"] == 3):
            print("╔═════════════════════╗")
            print("║                     ║")
            print("║                ☻    ║")
            print("║              /O/    ║")
            print("║             / /     ║")

    def animacion_lanzador(lanzador: int, fueraBola: bool, quieto: bool) -> None:
        if (quieto):
            print("                       ")
            print("                       ")
            print("          ●            ")
            print("         /|\\           ")
            print("         / \\           ")
        elif (lanzador["movimiento"] == 1 and fueraBola == False):
            print("      O                ")
            print("                       ")
            print("         \●            ")
            print("         \\|\\            ")
            print("           |           ")
        elif (lanzador["movimiento"] == 2 and fueraBola == False):
            print("          O            ")
            print("                       ")
            print("          ●            ")
            print("         /|\\           ")
            print("         / L           ")
        elif (lanzador["movimiento"] == 3 and fueraBola == False):
            print("              O        ")
            print("                       ")
            print("          ●/           ")
            print("         /|/           ")
            print("         |             ")
        elif (lanzador["movimiento"] == 1 and fueraBola == True):
            print("                       ")
            print("                       ")
            print("         \●            ")
            print("         \\|\\            ")
            print("           |           ")
        elif (lanzador["movimiento"] == 2 and fueraBola == True):
            print("                       ")
            print("                       ")
            print("          ●            ")
            print("         /|\\           ")
            print("         / L           ")
        elif (lanzador["movimiento"] == 3 and fueraBola == True):
            print("                       ")
            print("                       ")
            print("          ●/           ")
            print("         /|/           ")
            print("         |             ")
        print(f"Para batir la porteria, con el dorsal {lanzador["dorsal"]}")
        print(f"{lanzador["nombre"].upper()}")

    def animaciones(jugadores_equipo_atacante: list, jugadores_equipo_defensor: list, indice_atacante: int, indice_defensor: int) -> None:
        jugador_defensor = {"nombre": jugadores_equipo_defensor[indice_defensor].nombre, 
                            "dorsal": jugadores_equipo_defensor[indice_defensor].dorsal, 
                            "movimiento": jugadores_equipo_defensor[indice_defensor].movimiento}
        
        jugador_atacante = {"nombre": jugadores_equipo_atacante[indice_atacante].nombre, 
                            "dorsal": jugadores_equipo_atacante[indice_atacante].dorsal, 
                            "movimiento": jugadores_equipo_atacante[indice_atacante].movimiento}
        
        os.system("cls")
        Tanda.animacion_portero(jugador_defensor, jugador_atacante, True)
        Tanda.animacion_lanzador(jugador_atacante, False, True)
        time.sleep(2)
        os.system("cls")
        Tanda.animacion_portero(jugador_defensor, jugador_atacante, True)
        Tanda.animacion_lanzador(jugador_atacante, False, False)
        time.sleep(2)
        os.system("cls")
        Tanda.animacion_portero(jugador_defensor, jugador_atacante, False)
        Tanda.animacion_lanzador(jugador_atacante, True, False)
        time.sleep(2)