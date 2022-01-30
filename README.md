
### Módulo de la Consola.

Proporciona las clases de la consola (Console) y su canvas (ConsoleCanvas) para el programa falken.

La clase WinConsole facilita la creación de una ventana de pygame con una consola incorporada.

---

### clase Console.

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
Limpia la consola.  

---

```python
set_cursor(position) 
```
Establece la posición del cursor.

- **position** (tuple(int, int)): nueva posición del cursor (fila, columna).
- **_returns_**: None

---

```python
make_beep() 
```
Fuerza un beep de la consola.

- **_returns_**: None

---

```python
print(text="") 
```
Imprime en la consola el texto a partir de la posición actual del cursor. No
añade un salto de línea al final.

- **text** (str)): texto a imprimir. Por defecto, vacío.
- **_returns_**: None

---

```python
input(text="") 
```
Establece la posición del cursor.

- **text** (str)): nueva posición del cursor (fila, columna).
- **_returns_** (str): el texto introducido hasta el return (no incluido).
  Provoca un salto de línea final.

---

```python
process_key(key, mod) 
```
Permite la impresión directa de pulsaciones de teclas. 

- **key** (pygame.KEYUP.key ó pygame.KEYDOWN.key): id de la tecla pulsada.
- **key** (pygame.KEYUP.mod ó pygame.KEYDOWN.mod): estado de las teclas
  modificadoras.
- **_returns_**: None

---

### clase WinConsole.

Crea una ventana pygame con una consola iniciada y la fuente por defecto.

#### Constructor:

```python

WinConsole(src, width, height, title="", full=False, tts=False, font_size=32)
```

- **width** (int): ancho de la ventana.

- **height** (int): alto de la ventana.

- **title** (src): texto del título de la ventana. Por defecto, vacío.

- **full** (bool): indica si se crea la ventana a tamaño completo (full=True) o no. Por defecto, False.

- **tts** (bool): indica si se crea la ventana con el motor de text-to-speach inicializado. Por defecto, False.

- **font_size** (int): tamaño de la fuente. Por defecto, 32


#### Parámetros:

- **console** (console.Console): devuelve la referencia a la consola de la ventana. Sólo lectura.

---

#### Métodos:

```python
exit(ret=0) 
```
Cierra la ventana y finaliza la aplicación.  

- **ret** (int): código de retorno de la aplicación.
- **_returns_**: None

