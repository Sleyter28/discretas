'''

Consideraciones:
- Meter la primera reina.
- Meter la segunda en una casilla que no esté atacada por
la primera reina.
- Meter la tercera en una casilla no atacada por la
primera o la segunda.
- Meter sucesivamente el resto de reinas. Si en algún
momento no puede colocarse una reina, ir deshaciendo
movimientos de las reinas ya colocadas y a partir de esa
reorganización continuar la colocación del resto de
reinas.
Funciones auxiliares:

Funciones a implementar:
- asignar_reinaA(fila, columa) => Sitúa un 1
en la casilla (Fila, Columna) indicando que está
ocupada por una reina.
- eliminar_reina(fila, columna) => Sitúa un
0 en la casilla (Fila, Columna) indicando que esa casilla
está libre (antes estaba ocupada por una reina y ahora
deja de estarlo).
- recibe_jaque(int fila, int columna) => Devuelve 1
si la casilla (Fila, Columna) recibe jaque de alguna
reina y 0 en caso contrario.
'''


def recibe_jaque(fila, columna):
    pass


def asignar_reina(fila, columna):
    pass


def eliminar_reina(fila, columna):
    pass


def colocar_reina(columna):
    fila = 0
    posicion = 0

    if columna > 7:
        posicion = 1
        return posicion
    else:
        posicion = 0
        fila = 1
        while not posicion and (fila <= 7):
            if recibe_jaque(fila, columna):
                ++fila
            else:
                asignar_reina(fila, columna)
                posicion = colocar_reina(columna + 1)
                if not posicion:
                    eliminar_reina(fila, columna)
                    ++fila
    return posicion
