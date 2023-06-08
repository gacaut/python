import random
#1 problema:
"""def CalcSumDiv(num)
    suma=0
    for i in range(1, num)
        if num % i == 0:
            suma +=1
    return suma

while True:
    num = int(input("ingrese num menor a 100"))
    if num < 100:
        break
    else:
        print("debe ser menor a 100")
sumaDiv = CalcSumDiv(num)
if sumaDiv < num:
    print("es deficiente")
if sumaDiv > num:
    print("es abundante")
    if sumaDiv = num:
    print("es perfecto")"""

#2 problema:
"""def repetido(lista, valor):
    cont = lista.count(valor)
    if cont > 1:
        return True
    else:
        return False

def ordenada(lista):
    n = len(lista)
    for i in range(n):
        Min = i
        for j in range(i+1, n):
            if lista[j] < lista[Min]:
                Min = j
        lista[i], lista[Min] = lista[Min], lista[i]
    return lista

lista = random.sample(range(10, 101), 50)
print("lista desordenada:",lista)

listaOrdenada = ordenada(lista)
print("lista ordenada: ",listaOrdenada)

busqueda=int(input("search: "))
inicio = 0
fin = len(listaOrdenada) - 1
encontrado = False

while inicio <= fin:
    medio = (inicio + fin) // 2
    if listaOrdenada[medio] == busqueda:
        encontrado = True
        break
    elif listaOrdenada[medio] < busqueda:
        inicio = medio + 1
    else:
        fin = medio - 1

if encontrado:
    posicion = listaOrdenada.index(busqueda)
    print(f"el valor {busqueda} se encuentra en la posicion {posicion}")
else:
    print(f"el valor {busqueda} no se encuentra en la lista")"""

#3 problema
