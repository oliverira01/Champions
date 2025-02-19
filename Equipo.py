class Equipo:
    nombre: str
    estadio: str
    jugadores: list
    goles: int
    humano: bool
    lista_lanzadores: list

    def __init__(self, nombre: str, estadio: str, jugadores: list, humano: bool) -> None:
        self.nombre = nombre
        self.estadio = estadio
        self.jugadores = jugadores
        self.goles = 0
        self.humano = humano
        self.lista_lanzadores = []

    #def __eq__(self, other): #igual a (eq == equal)
    #    return self.goles == other.goles
    
    def __ne__(self, other): #diferente de (ne = not equal)
        return self.goles != other.goles
    
    def __gt__(self, other): #mayor que (greater than)
        return self.goles > other.goles
    
    def __ge__(self, other): #mayor o igual (greater or equal)
        return self.goles >= other.goles
    
    def __lt__(self, other): #menor que (lower than)
        return self.goles < other.goles
    
    def __le__(self, other): #menor o igual que (lower or equal)
        return self.goles <= other.goles