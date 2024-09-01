# busqueda_matriz.py

def buscar_valor(matriz, valor_buscado):
    """
    Busca un valor en una matriz bidimensional.

    :param matriz: List of lists representing the 2D matrix
    :param valor_buscado: The value to search for
    :return: A tuple with the position (row, col) if found, otherwise None
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_buscado:
                return i, j
    return None

def main():
    # Definir una matriz de ejemplo 3x3
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Valor que queremos buscar
    valor_buscado = 5

    # Llamar a la función de búsqueda
    resultado = buscar_valor(matriz, valor_buscado)

    if resultado:
        print(f"Valor {valor_buscado} encontrado en la posición {resultado}")
    else:
        print(f"Valor {valor_buscado} no encontrado en la matriz.")

if __name__ == "__main__":
    main()
