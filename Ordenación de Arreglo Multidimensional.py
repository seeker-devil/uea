# ordenar_fila_matriz.py

def bubble_sort(arr):
    """
    Ordena un arreglo usando el algoritmo Bubble Sort.

    :param arr: Lista de números a ordenar
    :return: Lista ordenada
    """
    n = len(arr)
    for i in range(n):
        # Últimos i elementos ya están en su lugar
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Intercambiar si el elemento encontrado es mayor
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def ordenar_fila(matriz, fila_index):
    """
    Ordena una fila específica de la matriz.

    :param matriz: Lista de listas representando la matriz 2D
    :param fila_index: Índice de la fila a ordenar
    """
    if fila_index < 0 or fila_index >= len(matriz):
        print("Índice de fila fuera de rango.")
        return
    matriz[fila_index] = bubble_sort(matriz[fila_index])

def imprimir_matriz(matriz):
    """
    Imprime la matriz de forma legible.

    :param matriz: Lista de listas representando la matriz 2D
    """
    for fila in matriz:
        print(fila)

def main():
    # Definir una matriz de ejemplo 3x3
    matriz = [
        [9, 7, 5],
        [3, 6, 2],
        [8, 4, 1]
    ]

    # Mostrar la matriz original
    print("Matriz original:")
    imprimir_matriz(matriz)

    # Índice de la fila que queremos ordenar (por ejemplo, la fila 0)
    fila_a_ordenar = 0

    # Ordenar la fila específica
    ordenar_fila(matriz, fila_a_ordenar)

    # Mostrar la matriz con la fila ordenada
    print(f"\nMatriz después de ordenar la fila {fila_a_ordenar}:")
    imprimir_matriz(matriz)

if __name__ == "__main__":
    main()
