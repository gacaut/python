#potencia
print(9**2)

#cociente entero
print(11//2)

#resto division
print(11%2) 

"""= asignar
  == comparar
 === comparar estrictamente"""

#primo:
def primo(numero):
    if numero < 2:      #un numero menor a 2 no es primo
        return False
    for i in range(2, int(numero**0.5)+1): #se verifica hasta su raiz cuadrada+1 ya que tendria divisores mas pequeños que lo incluyan
        if numero % i == 0: #verifico que ningun numero sea divisible
            return False
    return True

#raiz:
def raiz_exacta(numero):
    raiz = int(numero ** 0.5)  #busco raiz del numero, descarto decimales con el "int"
    return raiz ** 2 == numero #verifico que sea perfecta

#numero perfecto:
def perfecto(numero):
    SumaDivisores = 0
    for i in range(1, numero):
        if numero % i == 0: #busco divisores
            SumaDivisores += i #los sumo
    if SumaDivisores == numero:
        return True
    else:
        return False
      
"""ORDEN DE LISTAS"""
      
#seleccion:
def seleccionSort(lista):
    for i in range(len(lista)-1):
        for j in range( i + 1, len(lista)):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                
#burbujeo:
def burbuja(lista):
    desordenado = True
    while desordenado:
        desordenado = False
        for i in range(len(lista)-1):
            
            if lista[i] < lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                desordenado = True
#insercion:
def insercion(lista):
    for i in range(1, len(lista)):
        aux = lista[i]
        j = i
        while j > 0 and lista[j-1] > aux:
            lista[j] = lista[j-1]
            j = j - 1
        lista[j] = aux

"""BUSQUEDA EN LISTAS"""
        
#secuencial:
def secuencial(lista, numero):
    i = 0
    while i < len(lista) and lista[i] != numero:
        i = i+1
    if i < len(lista):
        return i
    else:
        return -1

#binaria (lista ya ordenada)
def binaria(lista, numero):
    izquierda = 0
    derecha = len(lista) - 1
    posicion = -1
    while izquierda <= derecha and posicion == -1:
        centro = (izquierda + derecha) // 2
        if lista[centro] == numero:
            posicion = centro
        elif lista[centro] < numero:
            izquierda = centro + 1
        else:
            derecha = centro - 1
    return posicion

#valor repetido
def repetido(lista, valor)
  cont = lista.count(valor)
  if cont > 1:
      return True
  else:
      return False
