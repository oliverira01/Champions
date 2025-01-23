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
    
    def comprobar_media_ronda(equipo1, equipo2, tiros):
        if tiros >= 5 and (equipo2 > equipo1):
            return "equipo2"
        elif equipo1.goles == 4 and equipo2.goles == 1:
            return "equipo1"
        elif equipo2.goles == 4 and equipo1.goles == 1:
            return "equipo2"
        elif equipo1.goles == 5 and equipo2.goles == 3:
            return "equipo1"
        elif equipo1.goles == 0 and equipo2.goles == 3:
            return "equipo2"
        else:
            return "empate"

    def comprobar_ganador(equipo1, equipo2, tiros):
        if equipo1.goles - 3 == equipo2.goles:
            return "equipo1"
        elif equipo2.goles -3 == equipo1.goles:
            return "equipo2"
        elif (equipo1.goles > equipo2.goles) and (tiros > 5):
            return "equipo1"
        elif (equipo2.goles > equipo1.goles) and (tiros > 5):
            return "equipo2"
        else:
            return "empate"