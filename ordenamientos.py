# ---------------------------------------------------------
# Módulo: ordenamientos.py
# Aquí implementarán sus funciones de ordenamiento.
#
# Cada función debe:
#   - Recibir una lista de strings (nombres)
#   - Tener el parámetro ascendente=True por omisión
#   - Ordenar la lista in-place (sin crear una copia)
#   - Regresar la lista ordenada
#
# Algoritmos a implementar:
#   1. Bubble Sort
#   2. Insertion Sort
#   3. Selection Sort
#   4. Shell Sort
#   5. Merge Sort
#   6. QuickSort (solo pivote central)
# ---------------------------------------------------------

def bubble_sort(lista, ascendente=True):
    """
    Implementa el algoritmo Bubble Sort.
    Ordena la lista in-place.
    """
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if ascendente:
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
            else:
                if lista[j] < lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def insertion_sort(lista, ascendente=True):
    """
    Implementa el algoritmo Insertion Sort.
    Ordena la lista in-place.
    """
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1

        if ascendente:
            while j >= 0 and lista[j] > clave:
                lista[j + 1] = lista[j]
                j -= 1
        else:
            while j >= 0 and lista[j] < clave:
                lista[j + 1] = lista[j]
                j -= 1

        lista[j + 1] = clave
    return lista

def selection_sort(lista, ascendente=True):
    """
    Implementa el algoritmo Selection Sort.
    Ordena la lista in-place.
    """
    n = len(lista)

    for i in range(n):
        indice = i
        for j in range(i + 1, n):
            if ascendente:
                if lista[j] < lista[indice]:
                    indice = j
            else:
                if lista[j] > lista[indice]:
                    indice = j

        lista[i], lista[indice] = lista[indice], lista[i]

    return lista

def shell_sort(lista, ascendente=True):
    """
    Implementa el algoritmo Shell Sort.
    Ordena la lista in-place.
    """
    n = len(lista)
    salto = n // 2

    while salto > 0:
        for i in range(salto, n):
            temp = lista[i]
            j = i

            if ascendente:
                while j >= salto and lista[j - salto] > temp:
                    lista[j] = lista[j - salto]
                    j -= salto
            else:
                while j >= salto and lista[j - salto] < temp:
                    lista[j] = lista[j - salto]
                    j -= salto

            lista[j] = temp

        salto //= 2

    return lista

def merge_sort(lista, ascendente=True):
    """
    Implementa el algoritmo Merge Sort.
    Debe regresar la lista ordenada.
    Puede usar funciones auxiliares si lo desean.
    """
    if len(lista) <= 1:
        return lista

    mitad = len(lista) // 2
    izquierda = merge_sort(lista[:mitad], ascendente)
    derecha = merge_sort(lista[mitad:], ascendente)

    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if ascendente:
            if izquierda[i] <= derecha[j]:
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1
        else:
            if izquierda[i] >= derecha[j]:
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado

def quick_sort(lista, ascendente=True):
    """
    Implementa QuickSort usando pivote central.
    Debe ordenar la lista in-place.
    Puede usar funciones auxiliares si lo desean.
    """
     def quicksort_aux(inicio, fin):
        if inicio < fin:
            pivote_indice = particion(inicio, fin)
            quicksort_aux(inicio, pivote_indice - 1)
            quicksort_aux(pivote_indice + 1, fin)

    def particion(inicio, fin):
        medio = (inicio + fin) // 2
        pivote = lista[medio]

        lista[medio], lista[fin] = lista[fin], lista[medio]

        i = inicio
        for j in range(inicio, fin):
            if ascendente:
                if lista[j] <= pivote:
                    lista[i], lista[j] = lista[j], lista[i]
                    i += 1
            else:
                if lista[j] >= pivote:
                    lista[i], lista[j] = lista[j], lista[i]
                    i += 1

        lista[i], lista[fin] = lista[fin], lista[i]
        return i

    quicksort_aux(0, len(lista) - 1)
    return lista
