from tkinter import Tk, Canvas
import random
import time


# Configuración de la ventana y la pelota
ANCHO_VENTANA = 500
ALTO_VENTANA = 400
TAMANO_PELOTA = 15
VELOCIDAD = 3
TIEMPO_ACTUALIZACION = 0.01


class Pelota:
    def __init__(self, canvas, color):
        self.canvas = canvas

        # Crear pelota
        self.id_pelota = canvas.create_oval(
            10,
            10,
            10 + TAMANO_PELOTA,
            10 + TAMANO_PELOTA,
            fill=color
        )

        # Posición inicial
        self.canvas.move(self.id_pelota, 245, 100)

        # Dirección aleatoria
        direcciones = [-VELOCIDAD, -2, -1, 1, 2, VELOCIDAD]
        random.shuffle(direcciones)

        self.velocidad_x = direcciones[0]
        self.velocidad_y = -VELOCIDAD

        # Tamaño del canvas
        self.ancho_canvas = self.canvas.winfo_width()
        self.alto_canvas = self.canvas.winfo_height()

    def mover(self):
        """Mueve la pelota dentro del canvas."""

        self.canvas.move(
            self.id_pelota,
            self.velocidad_x,
            self.velocidad_y
        )

        posicion = self.canvas.coords(self.id_pelota)

        # Rebote superior
        if posicion[1] <= 0:
            self.velocidad_y = VELOCIDAD

        # Rebote inferior
        if posicion[3] >= self.alto_canvas:
            self.velocidad_y = -VELOCIDAD

        # Rebote izquierdo
        if posicion[0] <= 0:
            self.velocidad_x = VELOCIDAD

        # Rebote derecho
        if posicion[2] >= self.ancho_canvas:
            self.velocidad_x = -VELOCIDAD


# Ventana principal
ventana = Tk()
ventana.title("Juego de Pelota")
ventana.resizable(False, False)
ventana.wm_attributes("-topmost", 1)

# Crear canvas
canvas = Canvas(
    ventana,
    width=ANCHO_VENTANA,
    height=ALTO_VENTANA,
    bd=0,
    highlightthickness=0
)

canvas.pack()
ventana.update()

# Crear objeto pelota
pelota = Pelota(canvas, "red")



# Bucle 
while True:
    pelota.mover()

    ventana.update_idletasks()
    ventana.update()

    time.sleep(TIEMPO_ACTUALIZACION)
