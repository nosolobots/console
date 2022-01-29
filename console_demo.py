import sys
import pygame
from console import Console

_DEFAULT_WIDTH = 800
_DEFAULT_HEIGHT = 600

def init_pygame(width, height, full=False):
    pygame.init()

    scr = None
    if full:
        scr = pygame.display.set_mode(
                (0, 0),
                pygame.DOUBLEBUF | pygame.FULLSCREEN,
                32)
    else:
        scr = pygame.display.set_mode(
                (width, height),
                pygame.DOUBLEBUF,
                32)
        pygame.display.set_caption("WOPR Console")

    return scr

def exit():
    pygame.display.quit()
    pygame.quit()
    sys.exit()

def main(width=_DEFAULT_WIDTH, height=_DEFAULT_HEIGHT, full=False):
    scr = init_pygame(width, height, full)

    if full:
        console = Console(scr, tts_on=True, font_size=64)
    else:
        #console = Console(scr, font=pygame.freetype.SysFont("arial", 32))
        console = Console(scr, tts_on=True)

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
    console.print("can switch of the beeeep\n\n")

    # PUEDO SITUAR EL CURSOR
    console.print("set the cursor position")
    console.set_cursor((10, 8))

    # PUEDO SOLICITAR ENTRADAS
    console.beep = True
    msg = console.input("and ask for something: ")
    print(msg)
    console.print("You entered: " + msg + "\n\n")

    # PUEDO IMPRIMIR EN LA CONSOLA LIBREMENTE
    console.print("I can allow free writing on the console\n\n")
    while(True):
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                # ESCRIBO CADA PULSACION DE TECLA
                console.process_key(event.key, event.mod)



if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == "fs":
            main(full=True)
        else:
            w,h = sys.argv[1].split("x")
            main(int(w), int(h))
    else:
        main()

