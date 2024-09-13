def ordenar_lista_numeros(lista: list[int]):
    lista.sort()
    return lista


def contar_palabras(archivo: str):
    count = 0

    with open(archivo, "r") as f:
        for line in f.readlines():
            sin_espacios = line.split()
            print(sin_espacios)
            count += len(line.split())
    return count

lista_desordenada = [5 , 6, 3, 9, 2, 1, 0, 8]
print("Lista desordenada:", lista_desordenada)

ordenada = ordenar_lista_numeros(lista_desordenada)
print("Lista ordenada:", ordenada)


num_palabras = contar_palabras("./prueba.txt")
print(num_palabras)
