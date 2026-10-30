# proyecto_freegames

Proyecto final: modificación de un videojuego de la librería open source **Freegames** de Python.

## Datos del alumno

- **Nombre:** Santiago Valdés Cruz
- **Matrícula:** A01799784
- **Usuario de GitHub:** SantiagoValdesA01799784
- **Juego:** Tic Tac Toe (Gato) - archivo `tictactoe.py`
- **Rama de trabajo:** `A01799784_tictactoe`

## Cómo ejecutar el juego

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install freegames
python3 tictactoe.py
```

En Mac con Python de Homebrew también fue necesario instalar tkinter: `brew install python-tk@3.14`.

## Cambios realizados

1. **Tamaño y color de X y O, centrados:** la X ahora es roja y la O azul, las dos con línea más gruesa (`width(10)`). También las hice más pequeñas y las acomodé para que queden en el centro de cada casilla.
2. **Validar casilla ocupada:** agregué un diccionario `board` que guarda qué casillas ya tienen ficha. Si se hace clic en una casilla ocupada (o fuera del tablero) no se dibuja nada y el turno no cambia.
3. **Detectar el final del juego:** después de cada jugada se revisan las 8 combinaciones ganadoras (3 filas, 3 columnas y 2 diagonales). Si alguien gana aparece "Ganó X" o "Ganó O"; si se llenan las 9 casillas sin ganador aparece "Empate". Al terminar ya no se pueden poner más fichas.
4. **Comentarios:** traduje los comentarios originales al español y agregué comentarios en cada modificación.

## Proceso que seguí

1. Creé el repositorio, lo cloné y preparé el entorno virtual con freegames.
2. Creé mi rama `A01799784_tictactoe` desde `main` y agregué un `.gitignore` para no subir la carpeta `.venv`.
3. Descargué el juego con `python3 -m freegames copy tictactoe` y subí la versión inicial.
4. Hice cada modificación en un commit separado, probando el juego después de cada cambio.
5. Agregué los comentarios en otro commit.
6. Hice merge de mi rama a `main` y actualicé este README.
