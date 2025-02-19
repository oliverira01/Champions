import random
class Jugador:
    nombre: str
    dorsal: int
    movimiento: int

    def __init__(self, nombre: str, dorsal: str) -> None:
        self.nombre = nombre
        self.dorsal = dorsal
    
    def __str__(self) -> str:
        return f"Nombre del jugador: {self.nombre}\nNº de dorsal: {self.dorsal}"
    
    def generar_movimiento(self) -> None:
        self.movimiento = random.randint(1,3)
    
    def elegir_movimiento(self) -> None:
        print("--------------------------------------------------------------")
        self.movimiento = int(input("1.Izquierda    2.Centro    3.Derecha > "))