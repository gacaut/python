import random
#funciones:
def primo(carta):
    if carta < 2:
        return False
    for i in range(2, int(carta**0.5)+1):
        if carta % i == 0:
            return False
    return True

def raiz_exacta(carta):
    raiz = int(carta ** 0.5)
    return raiz ** 2 == carta
#contadores:
contPrimos=0
contMulti=0
cont7=0
contOro5=0
contRaizExacta=0
#programa
for i in range(80):
    palo=random.randint(1,4)
    carta=random.randint(1,12)
    #palo
    if palo==1:
        palo = "oro"
    elif palo == 2:
        palo = "basto"
    elif palo == 3:
        palo = "espada"
    else:
        palo="copa"
    #primo
    if primo(carta):
        contPrimos +=1
    #multiplo2
    if carta % 2 == 0:
        contMulti += 1
    #7espadas
    if palo == "espada" and carta == 7:
        cont7 += 1
    #porcentaje 5 oro
    if palo == "oro" and carta == 5:
        contOro5 += 1
    #raiz exacta
    if raiz_exacta(carta):
        contRaizExacta += 1
#resultados   
    print(carta,"de", palo, end=", ")
print("\nSalieron", contPrimos, "numeros primos")
print("El siete de espada salio", cont7, "veces")
print("El 5 de oro salio el", (contOro5*80)/100,"% de las veces")
print("hay", contRaizExacta,"numeros con raiz exacta")


