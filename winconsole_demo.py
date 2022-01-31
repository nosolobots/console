#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Demo de WinConsole.

Lanza el programa de demostración de uso de WinConsole. Si no se indican
argumentos, crea una ventana a tamaño completo.

uso: python3 wincosole_demo.py [width x height]

Args:
    width x height (str, optional): si existe, crea una ventana de las
        dimensiones indicadas.
"""

import sys
import pygame
from console import WinConsole

_DEFAULT_WIDTH = 800
_DEFAULT_HEIGHT = 600

def main(width=_DEFAULT_WIDTH, height=_DEFAULT_HEIGHT, full=False):
    # Crear la ventana principal
    win = None
    if full:
        # pantalla completa
        win  = WinConsole(0, 0, full=True, tts=True, font_size=64)
    else:
        # ventana width x height
        win  = WinConsole(width, height, title="WinConsole Demo", tts=True)

    # Obtener una referencia a la consola principal
    console = win.console

    # PUEDO IMPRIMIR EN LA CONSOLA
    console.print("I can print to the console\n\n")

    # PUEDO TUNEAR EL TTS
    console.tts_engine.setProperty('rate', 50)
    console.print("I can tune the TTS engine")

    # PUEDO DESACTIVAR EL TTS
    console.tts = False
    console.print(" and deactivate it\n\n")

    # PUEDO DESACTIVAR EL TTS
    console.beep = False
    console.print("can switch of the beeeeping\n\n")

    # PUEDO SITUAR EL CURSOR
    console.print("set the cursor position")
    console.set_cursor((10, 8))

    # PUEDO SOLICITAR ENTRADAS
    console.beep = True
    msg = console.input("and ask for something: ")
    print(msg)
    console.print("\nYou entered: " + msg + "\n\n")

    # PUEDO LIMPIAR LA PANTALLA
    console.print("I can clear the screen\n\n")
    pygame.time.wait(1000)       # pausa
    console.clear()

    # PUEDO CAMBIAR EL COLOR DE LA TINTA
    old_color = console.ink # guardamos el color actual...
    console.ink = (255, 0, 0)
    console.print("I can change the ink color\n\n")
    pygame.time.wait(1000)       # pausa
    console.ink = old_color # ... para restaurarlo otra vez

    # PUEDO CAMBIAR EL COLOR DE FONDO
    old_color = console.paper # guardamos el color actual...
    console.paper = (0, 50, 100)
    console.clear()
    console.print("I can change the background color\n\n")
    pygame.time.wait(1000)       # pausa
    console.paper = old_color # ... para restaurarlo otra vez
    console.clear()

    # PUEDO ACTIVAR Y DESACTIVAR EL CURSOR
    console.print("I can de/activate the cursor --> ")
    for i in range(5):
        console.cursor = False      # desactivar
        pygame.display.update()     # actualizamos pantalla
        pygame.time.wait(500)       # pausamos
        console.cursor = True       # activar
        pygame.display.update()     # actualizamos pantalla
        pygame.time.wait(500)       # pausamos

    # PUEDO USAR LAS FUNCIONES DE DIBUJO DE PYGAME
    console.clear()
    console.print("I can draw on the surface\n\n")
    console.cursor = False

    surface = console.canvas.scr
    pygame.draw.circle(surface, (0, 190, 255), (200, 200), 100, 10)
    pygame.draw.circle(surface, (255, 255, 255), (420, 200), 100, 10)
    pygame.draw.circle(surface, (255, 0, 0), (640, 200), 100, 10)
    pygame.draw.circle(surface, (255, 255, 0), (310, 300), 100, 10)
    pygame.draw.circle(surface, (0, 255, 0), (530, 300), 100, 10)

    pygame.display.update()
    pygame.time.wait(2000)       # pausa

    # PUEDO IMPRIMIR EN LA CONSOLA LIBREMENTE
    console.clear()
    console.cursor = True
    console.print("I can allow free writing on the console\n\n")
    console.print("[ESC] to exit\n\n")

    while(True):
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                win.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                # ESCRIBO CADA PULSACION DE TECLA
                console.process_key(event.key, event.mod)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        # window init
        w,h = sys.argv[1].split("x")
        main(int(w), int(h))
    else:
        # full screen init
        main(full=True)

