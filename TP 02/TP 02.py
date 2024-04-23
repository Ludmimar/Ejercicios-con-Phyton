__author__ = ' TP2-Grupo G041 '

import random


def lanza1dado():
    return random.randint(1, 6)



def lanzarDados():
    input("\t>>Presione ENTER para tirar los dados<<")
    d1 = lanza1dado()
    d2 = lanza1dado()
    d3 = lanza1dado()
    print("\tObtuvo:", d1, d2, d3,)
    return d1, d2, d3



def jugada():
    apuesta = int(input("\tDebe elegir su apuesta:\n "
                        "\t(ingrese '1' para elegir par o '2' para elegir impar: "))
    punjug = acierto = 0
    if apuesta == 1:
        print("\t**Selecciono Par**")
        dado1, dado2, dado3 = lanzarDados()
        sdados = dado1 + dado2 + dado3
        if sdados % 2 == 0:
            dado_mayor = max(dado1, dado2, dado3)
            punjug += dado_mayor
            print(("." * 75))
            print(("." * 5),"La suma es de la paridad elegida. Sumaste ", dado_mayor, "puntos",("." * 5))
            acierto += 1
            if dado1 % 2 == 0 and dado2 % 2 == 0 and dado3 % 2 == 0:
                punjug *= 2
                print("CADA DADO ES DE LA PARIDAD ELEGIDA!!! ACUMULASTE ", punjug, "PUNTOS")
        elif sdados % 2 != 0:
            dado_menor = min(dado1, dado2, dado3)
            punjug -= dado_menor
            print(("." * 75))
            print(("." * 5),"La suma no es de la paridad elegida. Se restaron ", dado_menor, "puntos",("." * 5))

    elif apuesta == 2:
        print("\t**Selecciono Impar**")
        dado1, dado2, dado3 = lanzarDados()
        sdados = dado1 + dado2 + dado3
        if sdados % 2 != 0:
            dado_mayor = max(dado1, dado2, dado3)
            punjug += dado_mayor
            print(("." * 75))
            print(("." * 5),"La suma es de la paridad elegida. Sumaste ", dado_mayor,"puntos",("." * 5))
            acierto += 1
            if dado1 % 2 != 0 and dado2 % 2 != 0 and dado3 % 2 != 0:
                punjug *= 2
                print("Cada dado es de la paridad elegida!!! Acumulaste ", punjug)
        elif sdados % 2 == 0:
            dado_menor = min(dado1, dado2, dado3)
            punjug -= dado_menor
            print(("." * 75))
            print(("." * 5),"La suma no es de la paridad elegida. Se restaron ",dado_menor,"puntos",("." * 5))

    else:
        print("Opción incorrecta!")

    return punjug, acierto




def Juego():
    print("\n", (">" * 20), "COMENZEMOS EL JUEGO", ("<" * 20), "\n")
    x = int(input("\tIngrese el puntaje a lograr: (debe ser mayor a 10): "))
    while x <= 10:
        x = int(input("Ingrese el puntaje a lograr: (debe ser mayor a 10): "))
    acump1 = acump2 = 0
    cantaci1 = cantaci2 = 0
    cvuelta = 0
    bandera = False
    ganador = False
    win1 = win2 = 0
    gan1 = gan2 = 0

    jugador1 = input("\n\tIngrese el nombre del jugador 1: ")
    jugador2 = input("\tIngrese el nombre del jugador 2: ")
    while acump1 < x and acump2 < x:
        cvuelta += 1
        print(("*" * 75))

        # Jugador 1

        print("\tTurno del Jugador: ", jugador1)
        puntaje1, acierto1 = jugada()
        acump1 += puntaje1
        cantaci1 += acierto1
        print(("." * 75))

        # Jugador 2
        print("\tTurno del Jugador: ", jugador2)
        puntaje2, acierto2 = jugada()
        acump2 += puntaje2
        cantaci2 += acierto2

        if puntaje1 == puntaje2:
            bandera = True

        # puntaje al finalizar la ronda
        print("-" * 75)
        print("\tPuntajes de la Ronda")
        print("\tJugador: ", jugador1, puntaje1, "puntos")
        print("\tJugador: ", jugador2, puntaje2, "puntos")
        print("." * 75)
        print("\tPuntaje acumulado hasta el momento")
        print("\tJugador: ", jugador1, acump1, "puntos")
        print("\tJugador: ", jugador2, acump2, "puntos")


        if puntaje1 > puntaje2:
            win1 += 1
            gan1 += 1
            win2 = 0
            if win1 == 3:
                ganador = True
        elif puntaje2 > puntaje1:
            win2 += 1
            gan2 += 1
            win1 = 0
            if win2 == 3:
                ganador = True

    print(("*" * 75))
    print("\n", (">" * 20), "JUEGO FINALIZADO", ("<" * 20),)
    print("\n", (">" * 20), "RESULTADOS", ("<" * 20),)
    print("\t°°°° CANTIDAD DE JUGADAS REALIZADAS: ", cvuelta, "°°°°")
    if bandera:
        print("\tHubo al menos una jugada con puntaje empatado entre ambos jugadores")
    print(("-" * 75))
    promedio1 = acump1 / cvuelta
    promedio2 = acump2 / cvuelta
    print("\tPuntaje Promedio obtenido por jugada del jugador: ", jugador1, "es: ", round(promedio1, 2))
    print("\tPuntaje Promedio obtenido por jugada del jugador: ", jugador2, "es: ", round(promedio2, 2))
    porc1 = cantaci1 * 100 / cvuelta
    porc2 = cantaci2 * 100 / cvuelta
    print("\tPorcentaje de aciertos:",
          "Jugador: ", jugador1,"es: ",round(porc1, 2),"%", "y",
          "jugador", jugador2, "es: ", round(porc2, 2),"%")

    if ganador:
        print("\t*** Al menor un jugador gano 3 turnos seguidos ***")

    print("\n", ("°" * 20), "GANADOR", ("°" * 20), )

    if acump1 > acump2:
        print("\tGANO EL JUGADOR: ", jugador1, "CON ", acump1, "PUNTOS")
        if porc1 > porc2:
            print("\ty obtuvo el mayor porcentaje de aciertos ")
    elif acump1 < acump2:
        print("\tGANO EL JUGADOR: ", jugador2, "CON ", acump2, "PUNTOS")
        if porc1 < porc2:
            print("\tY OBYUVO EL MAYOR PORCENTAJE DE ACIERTOS ")

    #condicion de empate
    if acump1 == acump2:
        print("\tSE PRODUJO UN EMPATE!!!!")
        if gan1 > gan2:
            print("GANO EL JUGADOR CON MAYOR JUGADAS GANADAS: ", jugador1, "con: ", acump1, "PUNTOS")
        elif gan1 < gan2:
            print("GANO EL JUGADOR CON MAYOR JUGADAS GANADAS: ", jugador2, "con: ", acump2, "PUNTOS")
        elif gan1 == gan2:
            print("AMBOS JUGADORES OBTUVIERON EL MISMO PUNTAJE Y CANTIDAD DE ACIERTOS")



Juego()