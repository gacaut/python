#potencia
print(9**2)

#cociente entero
print(11//2)

#resto division
print(11%2) 

"""= asignar
  == comparar
 === comparar estrictamente"""

#primo
def primo(numero):
    if numero < 2:      #un numero menor a 2 no es primo
        return False
    for i in range(2, int(numero**0.5)+1): #se verifica hasta su raiz cuadrada+1 ya que tendria divisores mas pequeños que lo incluyan
        if numero % i == 0: #verifico que ningun numero sea divisible
            return False
    return True

#raiz
def raiz_exacta(numero):
    raiz = int(numero ** 0.5)  #busco raiz del numero, descarto decimales con el "int"
    return raiz ** 2 == numero #verifico que sea perfecta

#perfecto
def perfecto(numero):
    SumaDivisores = 0
    for i in range(1, numero):
        if numero % i == 0: #busco divisores
            SumaDivisores += i #los sumo
    if SumaDivisores == numero:
        return True
    else:
        return False

#fibonacci
    