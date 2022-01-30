# -*- coding: utf-8 -*-

"""Módulo de la Consola.

    Proporciona las clases de la consola (Console) y su canvas (ConsoleCanvas)
    para el programa falken.

    TO-DO:

        - backspace, debe subir una línea si borramos y llegamos al ppio de la
          linea?
        - backspace repeat
        - se debe dejar escribir si pasamos la ultima fila?
        - shift + números
        - cambiar el tiempo de beep
        - posibilidad de capturar ESC o CTRl-C para salir en print() y/o
          input()

    Changes:
        ver: 0.3
        - se añadió Console.clear() y ConsoleCanvas.clear_screen()
        - se añadión propiedad Console.canvas para acceder al surface
        - se añadió make_beep() a Console
        - get/set color de fondo y tinta

        ver: 0.2
        - se añadió __version__
        - input():
          - se eliminó el salto de línea final
          - se añadió valor por defecto a parámetro text
          - se añadió check de longitud de parámetro text

        ver: 0.1
        - se ajustó la posición de QUOTE
"""
__version__ = "0.3"

import os
import pygame
import pygame.freetype


class ConsoleCanvas():
    """Da acceso a la superficie de dibujo de la consola."""

    _package_dir = os.path.dirname(os.path.abspath(__file__))
    _resources_dir = os.path.join(_package_dir, "resources")
    _audio_dir = os.path.join(_resources_dir, "audio")
    _fonts_dir = os.path.join(_resources_dir, "fonts")

    _DEFAULT_BACK_COLOR = (10, 10, 10)
    _DEFAULT_FONT_COLOR = (150, 225, 255)
    _DEFAULT_TTF_FONT_FILE = os.path.join(_fonts_dir, "wopr.ttf")
    _DEFAULT_KEY_SND_FILE = os.path.join(_audio_dir, 'key.wav')

    def __init__(self, scr, font_size, font=None, pause=50):
        # Surface
        self._scr = scr

        # cursor
        self._cursor_pos = [0, 0]
        self._cursor = True

        # font
        self._font_size = font_size
        self._font = font if font else pygame.freetype.Font(
                self._DEFAULT_TTF_FONT_FILE, self._font_size)
        self._cursor_height = self._font.get_rect('\u2588').height
        self._cursor_width = self._font.get_rect('\u2588').width
        self._ncols = scr.get_width() // self._cursor_width
        self._nrows = scr.get_height() // self._cursor_height

        self._font_color = self._DEFAULT_FONT_COLOR
        self._back_color = self._DEFAULT_BACK_COLOR

        # Beeping
        self._char_pause = pause
        self._char_snd = pygame.mixer.Sound(self._DEFAULT_KEY_SND_FILE)
        self._beep = True

        # clear console
        self.clear_screen()

    # ------------------------------------------------------------------------
    # PROPIEDADES
    # ------------------------------------------------------------------------

    @property
    def scr(self):
        return self._scr

    @property
    def cursor(self):
        return self._cursor

    @cursor.setter
    def cursor(self, active):
        self._cursor = active

    @property
    def cursor_pos(self):
        return self._cursor_pos

    @cursor_pos.setter
    def cursor_pos(self, position):
        self.clear_cursor()
        self._cursor_pos[0] = position[0]
        self._cursor_pos[1] = position[1]
        self.render_cursor()

    @property
    def beep(self):
        return self._beep

    @beep.setter
    def beep(self, active):
        self._beep = active

    @property
    def font_color(self):
        return self._font_color

    @font_color.setter
    def font_color(self, color):
        self._font_color = color

    @property
    def back_color(self):
        return self._back_color

    @back_color.setter
    def back_color(self, color):
        self._back_color = color

    # ------------------------------------------------------------------------
    # METODOS
    # ------------------------------------------------------------------------

    def clear_screen(self):
        # clear surface
        self._scr.fill(self._back_color)

        # set cursor
        self.cursor_pos = (0, 0)

    def clear_cursor(self):
        # borra posición actual
        pygame.draw.rect(
            self._scr,
            self._back_color,
            pygame.Rect(
                self._cursor_pos[0] * self._cursor_width,
                self._cursor_pos[1] * self._cursor_height,
                self._cursor_width,
                self._cursor_height +
                    (self._cursor_height -
                        self._font.get_rect('A').height)))

    def render_cursor(self):
        if self._cursor:
            self._font.render_to(
                self._scr,
                (self._cursor_pos[0] * self._cursor_width,
                   (self._cursor_pos[1] * self._cursor_height) +
                   (self._cursor_height - self._font.get_rect('A').height)),
                '\u2588',
                self._font_color)
            if self._beep:
                self._char_snd.play()
            pygame.display.update()

    def print(self, text):
        for ch in text.upper():
            self.clear_cursor()

            if ch == '\n':
                self._cursor_pos = [0, self._cursor_pos[1] + 1]

            elif ch == '\b':
                if self._cursor_pos[0]:
                    self._cursor_pos = [self._cursor_pos[0] - 1, self._cursor_pos[1]]
                    self.clear_cursor()

            else:
                y_pos = self._cursor_pos[1] * self._cursor_height
                if ch in ('\''):
                    # caracteres que tienen que "pegarse" arriba
                    y_pos += self._font.get_rect(ch).height
                elif ch in ('-'):
                    # caracteres que van al medio
                    y_pos += self._cursor_height // 2 + \
                        self._font.get_rect(ch).height
                else:
                    # caracteres que van abajo
                    y_pos += self._cursor_height - self._font.get_rect(ch).height

                self._font.render_to(
                    self._scr,
                    (self._cursor_pos[0] * (self._cursor_width), y_pos),
                    ch,
                    self._font_color)

                # avanza cursor
                self._cursor_pos[0] += 1
                if self._cursor_pos[0] == self._ncols:
                    self._cursor_pos = [0, self._cursor_pos[1] + 1]

            if self._beep:
                self._char_snd.play()

            if self._cursor:
                self.render_cursor()

            pygame.time.wait(self._char_pause)
            pygame.display.update()

class Console():
    """Proporciona el interfaz de comunicación con la consola."""

    def __init__(self, scr, tts_on=False, font=None, font_size=32):

        # TTS
        self._tts_on = tts_on
        self._tts_engine = None
        if tts_on:
            import pyttsx3
            self._tts_engine = pyttsx3.init()
            self._tts_engine.setProperty('voice', 'english-us')

        # canvas
        self._canvas = ConsoleCanvas(scr, font_size, font)

    # ------------------------------------------------------------------------
    # PROPIEDADES
    # ------------------------------------------------------------------------

    @property
    def tts_engine(self):
        return self._tts_engine

    @property
    def tts(self):
        return self._tts_on

    @tts.setter
    def tts(self, active):
        self._tts_on = active

    @property
    def beep(self):
        return self._canvas.beep

    @beep.setter
    def beep(self, active):
        self._canvas.beep = active

    @property
    def canvas(self):
        return self._canvas.scr

    @property
    def ink(self):
        return self._canvas.font_color

    @ink.setter
    def ink(self, color):
        self._canvas.font_color = color

    @property
    def paper(self):
        return self._canvas.back_color

    @paper.setter
    def paper(self, color):
        self._canvas.back_color = color

    # ------------------------------------------------------------------------
    # METODOS
    # ------------------------------------------------------------------------

    def clear(self):
        self._canvas.clear_screen()

    def set_cursor(self, position):
        self._canvas.cursor_pos = position

    def make_beep(self):
        self._canvas._char_snd.play()

    def print(self, text):
        self._canvas.print(text)

        if self._tts_engine and self._tts_on:
            self._tts_engine.say(text)
            self._tts_engine.runAndWait()

    def input(self, text=""):
        if len(text):
            self.print(text)

        cmd = ""
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    cmd += self.process_key(event.key, event.mod)
                    if event.key == pygame.K_RETURN:
                        # self._canvas.print('\n')
                        return cmd

    def process_key(self, key, mod):
        letter = ""
        if (key >= pygame.K_a and key <= pygame.K_z) or         \
                (key >= pygame.K_0 and key <= pygame.K_9) or    \
                (not (mod & pygame.KMOD_SHIFT) and key in (
                        pygame.K_PERIOD,
                        pygame.K_QUOTE,
                        pygame.K_COMMA,
                        pygame.K_PERIOD,
                        pygame.K_LESS,
                        pygame.K_MINUS,
                        pygame.K_PLUS)):
            letter = pygame.key.name(key).upper()
            self._canvas.print(letter)
        elif key == pygame.K_SPACE:
            self._canvas.print(" ")
            letter = " "
        elif key == pygame.K_RETURN:
            self._canvas.print("\n")
        elif key == pygame.K_BACKSPACE:
            self._canvas.print("\b")
        elif mod & pygame.KMOD_SHIFT:
            if key == pygame.K_QUOTE:
                self._canvas.print("?")
                letter = "?"
            elif key == pygame.K_COMMA:
                self._canvas.print(";")
                letter = ";"
            elif key == pygame.K_PERIOD:
                self._canvas.print(":")
                letter = ":"
            elif key == pygame.K_LESS:
                self._canvas.print(">")
                letter = ">"
            elif key == pygame.K_MINUS:
                self._canvas.print("_")
                letter = "_"
            elif key == pygame.K_PLUS:
                self._canvas.print("*")
                letter = "*"

        return letter
