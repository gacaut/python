"""
-----------------------------------------------------------------------------------------------
Título:
Fecha:
Autor:
Descripción:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS IMPORTADOS
#----------------------------------------------------------------------------------------------
import random


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def agregarAmigoAlSorteo(_path):
    ## Desarrolla aquí el código ##
    ## Esta función permite agregar un amigo al archivo
    ## (el string a almacenar debe quedar así "nombre;apellido;dni;num1;num2;num3;num4;num5;num6")
    cadenaCaracter = ""

    x = input("Dime el nombre de tu amigo... ")
    cadenaCaracter = x
    
    x = input("Dime su apellido... ")
    cadenaCaracter = cadenaCaracter + ";" + x

    mensajePedido = "Dime su DNI... "
    mensajeError = "El valor no es un entero!"
    x = validarEntero(mensajePedido, mensajeError)
    cadenaCaracter = cadenaCaracter + ";" + str(x)
    
    # Solicita los 6 números del amigo
    for i in range(0,6):
            mensajePedido = "Dime el número elegido... "
            mensajeError = "El valor no es un entero!"
            x = validarEntero(mensajePedido, mensajeError)
            cadenaCaracter = cadenaCaracter + ";"  + str(x)
    
    # Se escriben los datos ingresados en el archivo
    try:
        f = open(_path, mode="a", encoding='utf-8')
        f.write(cadenaCaracter + "\n")

    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)

    finally:
        try:
            f.close()
        except:
            pass

    return


#---------------------------
def validarEntero(_mensajePedido, _mensajeError):
    ## Desarrolla aquí el código ##
    ## Esta función se utilizará en las funciones agregarAmigosAlSorteo y repartirPozo
    ## para validar que los valores ingresados (dni y numeros elegidos en el primer caso y monto en el segundo) sean enteros
    ## utilizar un manejador de excepciones 
    ## No es necesario validar que el número jugado esté entre 0 y 90, asumiremos que el usuario siempre ingresa correctamente esos números
    while True:
        try:
            valor = int(input(_mensajePedido))
            break
        except ValueError:
            print(_mensajeError)
    return valor


#---------------------------
def realizarSorteo(_path):
    ## desarrolla aquí el código ##
    _numerosSorteados = []
    _listaGanadores = []

    # Parte 1: Se llama a la función que genera una lista de 6 números distintos obtenidos al azar
    _numerosSorteados = sortearNumeros()

    # Parte 2: 
    try:
        f = open(_path, mode="r", encoding='utf-8')

        # Se recorre el archivo de amigos
        for linea in f:
            aciertos = 0
            # Se limpia y separa la línea en campos
            campos = linea.replace('\n','').split(";")
            
            # Se recorre la lista de números sorteados 
            for numero in _numerosSorteados:
                # Si se encuentra coincidencia con alguno de los 6 números del amigo entonces se cuenta un acierto
                if str(numero) in campos[3:9]:
                    aciertos = aciertos + 1 
     
            # De haber 2 o más aciertos el amigo resulta ganador
            if aciertos >= 2:
                _listaGanadores.append(f"{campos[0]} {campos[1]}")

    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)

    finally:
        try:
            f.close()
        except:
            pass

    return _numerosSorteados, _listaGanadores


#---------------------------
def sortearNumeros():
    ## Desarrolla aquí el código ##
    ## Esta función crea una lista de 6 números aleatorios distintos
    numerosSorteados = []
    
    # Se genera un primer número aleatorio
    numeroSorteado = random.randint(0, 90)
    
    # Se continua la generación de los siguientes 5 números aleatorios
    while len(numerosSorteados) < 6:
        numeroSorteado = random.randint(0, 90)
        
        # Tienen que ser distintos, si sale uno repetido lo descarta
        if numeroSorteado not in numerosSorteados:
            numerosSorteados.append(numeroSorteado)

    return numerosSorteados


#---------------------------
def repartirPozo(_listaGanadores):
    ## Desarrolla aquí el código ##
    ## Utilizar un manejador de excepciones si el pozo es vacante
    mensajePedido = "ingrese un monto total de apuestas válido: "
    mensajeError = "El monto no es un número, intente denuevo"
    monto = validarEntero(mensajePedido, mensajeError)

    try:
        # Se divide el monto en partes iguales para cada ganador
        montoGanado = monto / len(_listaGanadores)
        
        for ganador in _listaGanadores:
            print(f"{ganador} ganó ${montoGanado:.2f}")

    except ZeroDivisionError:
        print("Pozo Vacante!")

    return

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
# Declaración de variables
#----------------------------------------------------------------------------------------------
numerosSorteados = []
listaGanadores = []
path = "c:/uade/amigos.txt" # IMPORTANTE!!!!! usa esta variable string para el path completo del archivo amigos.txt

# Bloque de menú
#----------------------------------------------------------------------------------------------
while True:
    while True:
        print()
        print("---------------------------")
        print("MENÚ DEL SISTEMA           ")
        print("---------------------------")
        print("[1] Cargar Amigo al sorteo")
        print("[2] Sortear!")
        print("[3] Mostrar ganadores!")
        print("[0] Salir del programa")
        print()
        opcion = input("Seleccione una opción: ")
        if opcion in ("0","1","2","3"): # Sólo continua si se elije una opcion de menú válida
            break
        else:
            input("Opción inválida. Presione ENTER para continuar.")

    if opcion == "0": # Opción salir del programa
        exit()

    elif opcion == "1":   # Opción Cargar Amigo al sorteo
        agregarAmigoAlSorteo(path)
        
    elif opcion == "2":   # Sortear!
        numerosSorteados, listaGanadores = realizarSorteo(path)
        print('Números sorteados: ', numerosSorteados)
        print('Ganadores: ', listaGanadores)

    elif opcion == "3":   # Vaciar lista de amigos
        if len(numerosSorteados) > 0:
            repartirPozo(listaGanadores)
        else:
            print("Primero realice el sorteo!")

    print()
    input("Presione ENTER para continuar.")
