from ordenamientos import (
    bubble_sort,
    insertion_sort,
    selection_sort,
    shell_sort,
    merge_sort,
    quick_sort
)

def leer_archivo(nombre_archivo):
    lista = []
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            lista.append(linea.strip())
    return lista

def main():
    print("=== PROGRAMA DE ORDENAMIENTO DE NOMBRES ===")
    nombres = leer_archivo("nombres.txt")

    while True:
        print("\nElige un algoritmo:")
        print("1. Bubble Sort")
        print("2. Insertion Sort")
        print("3. Selection Sort")
        print("4. Shell Sort")
        print("5. Merge Sort")
        print("6. QuickSort (pivote central)")
        print("7. Salir")

        opcion = input("Opción: ")

        if opcion == "7":
            print("Saliendo...")
            break

        orden = input("¿Orden ascendente (A) o descendente (D)? ").upper()
        asc = True if orden == "A" else False

        lista_trabajo = nombres.copy()

        if opcion == "1":
            resultado = bubble_sort(lista_trabajo, asc)
        elif opcion == "2":
            resultado = insertion_sort(lista_trabajo, asc)
        elif opcion == "3":
            resultado = selection_sort(lista_trabajo, asc)
        elif opcion == "4":
            resultado = shell_sort(lista_trabajo, asc)
        elif opcion == "5":
            resultado = merge_sort(lista_trabajo, asc)
        elif opcion == "6":
            resultado = quick_sort(lista_trabajo, asc)
        else:
            print("Opción no válida.")
            continue

        print("\nResultado del ordenamiento:")
        for nombre in resultado:
            print(nombre)

if __name__ == "__main__":
    main()
