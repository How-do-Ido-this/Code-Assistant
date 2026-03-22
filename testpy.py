def buscar_elemento(lista, objetivo):
    i = 0
    
    while i != len(lista):
        if lista[i] == objetivo:
            posicion = i
        i += 1

    return posicion  # ❌ puede no existir

datos = [3, 5, 7, 9]
resultado = buscar_elemento(datos, 4)

print("Posición:", resultado)