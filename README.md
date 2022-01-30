
### Módulo de la Consola.
---

Proporciona las clases de la consola (Console) y su canvas (ConsoleCanvas) para el programa falken.

La clase WinConsole nos facilita la creación de una ventana de pygame con una
consola incorporada.

### Clase Console.
---

Clase principal de la consola.

#### Constructor:

```python

Console(src, tts_on=False, font=None, font_size=32)
```

- **src** (pygame.Surface): superficie de pygame sobre la que se crea la consola.

- **tts_on** (bool): crea la consola con un engine pytts3 para text-to-speach que
        se ejcuta al final de cada print(). Por defecto, False.

- **font** (pygame.freetype.Font): fuente empleada por la consola. Si no se indica
        ninguna, se emplea la fuente [wopr-tweaked.ttf](https://fontstruct.com/fontstructions/show/1854233/wopr-terminal-1).

- **font_size** (int): tamaño de la fuente. Por defecto, 32


#### Parámetros:

- **canvas** (pygame.Surface): superficie de pygame sobre la que se crea la consola. Sólo lectura.

- **tts\_engine** (pyttsx3.Engine): engine pyttsx3 para text-to-speach. Sólo
  lectura.

- **tts** (bool): activa/descativa el text-to-speach. Lectura/escritura.

- **cursor** (bool): activa/descativa el cursor. Lectura/escritura.

- **beep** (bool): activa/descativa el sonido al escribir. Lectura/escritura.

- **ink** (pygame.Color ó int ó tuple(int, int, int, [int])): color de la tinta. Lectura/escritura.

- **paper** (pygame.Color ó int ó tuple(int, int, int, [int])): color del fondo. Lectura/escritura.


#### Métodos:

```python
clear() 
```
<br>Limpia la consola.  


```python
set\_cursor(position) 
```
<br>Establece la posición del cursor.

- **position** (tuple(int, int)): nueva posición del cursor (fila, columna).




