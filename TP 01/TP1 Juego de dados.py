import random

jugador1 = input("Ingrese el nombre del jugador 1: ")
jugador2 = input("Ingrese el nombre del jugador 2: ")
puntaje1_jugador1 = 0
puntaje1_jugador2 = 0
print("Bienvenidos/as", jugador1, "y", jugador2, ".......Que comience el juego")

# Ronda 1
# jugador 1:
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
dado3 = random.randint(1, 6)
print("\n\t\t\t*********Ronda1*********\n\nJugador1:\n\tLos dados tirados por el jugador 1 fueron:\n\t", "dado1: ",
      dado1, "\n\t", "dado2: ", dado2, "\n\t", "dado3: ", dado3)
if dado1 == dado2 == dado3:
    puntaje1_jugador1 += 6
elif dado1 == dado2 and dado3 != dado2:
    dado3 = random.randint(1, 6)
    print("\tEl dado 3 se volvió a tirar y salió: ", dado3)
    if dado1 == dado2 == dado3:
        puntaje1_jugador1 += 6
    elif dado3 != dado1 and dado2:
        puntaje1_jugador1 += 3

elif dado2 == dado3 and dado1 != dado2:
    dado1 = random.randint(1, 6)
    print("\tEl dado 1 se volvió a tirar y salió: ", dado1)
    if dado1 == dado2 == dado3:
        puntaje1_jugador1 += 6
    elif dado1 != dado2 and dado3:
        puntaje1_jugador1 += 3

elif dado1 == dado3 and dado2 != dado1:
    dado2 = random.randint(1, 6)
    print("\tEl dado 2 se volvió a tirar y salió: ", dado2)
    if dado1 == dado2 == dado3:
        puntaje1_jugador1 += 6
    elif dado2 != dado1 and dado3:
        puntaje1_jugador1 += 3

elif dado1 != dado2 and dado2 != dado3 and dado3 != dado1:
    puntaje1_jugador1 = 0

print("\tEl puntaje obtenido en la primera ronda por el jugador 1 fue: ", puntaje1_jugador1)

# Jugador 2:
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
dado3 = random.randint(1, 6)
print("\n\nJugador2:\n\tLos dados tirados por el jugador 2 fueron:\n\t", "dado1: ", dado1, "\n\t", "dado2: ", dado2,
      "\n\t", "dado3: ", dado3)
if dado1 == dado2 == dado3:
    puntaje1_jugador2 += 6
elif dado1 == dado2 and dado3 != dado2:
    dado3 = random.randint(1, 6)
    print("\tEl dado 3 se volvió a tirar y salió: ", dado3)
    if dado1 == dado2 == dado3:
        puntaje1_jugador2 += 6
    elif dado3 != dado1 and dado2:
        puntaje1_jugador2 += 3

elif dado2 == dado3 and dado1 != dado2:
    dado1 = random.randint(1, 6)
    print("\tEl dado 1 se volvió a tirar y salió: ", dado1)
    if dado1 == dado2 == dado3:
        puntaje1_jugador2 += 6
    elif dado1 != dado2 and dado3:
        puntaje1_jugador2 += 3

elif dado1 == dado3 and dado2 != dado1:
    dado2 = random.randint(1, 6)
    print("\tEl dado 2 se volvió a tirar y salió: ", dado2)
    if dado1 == dado2 == dado3:
        puntaje1_jugador2 += 6
    elif dado2 != dado1 and dado3:
        puntaje1_jugador2 += 3

elif dado1 != dado2 and dado2 != dado3 and dado3 != dado1:
    puntaje1_jugador2 = 0

print("\tEl puntaje obtenido en la primera ronda por el jugador 2 fue: ", puntaje1_jugador2)

# Ronda 2
puntaje2_jugador1 = 0
puntaje2_jugador2 = 0
print("\n\t\t\t*********Ronda2*********\n")
# jugador 1:
apuesta1 = int(input("hola judador 1, Debe elegir su apuesta: (presione '1' para elegir par o '2' para elegir impar: "))
if apuesta1 == 1:
    print("Opción elegida: ", apuesta1)
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    dado3 = random.randint(1, 6)
    print("\nJugador1:\n\tLos dados tirados por el jugador 1 fueron:\n\t", "dado1: ", dado1, "\n\t", "dado2: ", dado2,
          "\n\t", "dado3: ", dado3)
    if (dado1 + dado2 + dado3) % 2 == 0:
        dado_mayor = max(dado1, dado2, dado3)
        puntaje2_jugador1 += dado_mayor
        if dado1 % 2 == 0 and dado2 % 2 == 0 and dado3 % 2 == 0:
            puntaje2_jugador1 *= 2
    elif (dado1 + dado2 + dado3) % 2 != 0:
        dado_menor = min(dado1, dado2, dado3)
        puntaje2_jugador1 -= dado_menor

elif apuesta1 == 2:
    print("Opción elegida: ", apuesta1)
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    dado3 = random.randint(1, 6)
    print("\nJugador1:\n\tLos dados tirados por el jugador 1 fueron:\n\t", "dado1: ", dado1, "\n\t", "dado2: ", dado2,
          "\n\t", "dado3: ", dado3)
    if (dado1 + dado2 + dado3) % 2 != 0:
        dado_mayor = max(dado1, dado2, dado3)
        puntaje2_jugador1 += dado_mayor
        if dado1 % 2 != 0 and dado2 % 2 != 0 and dado3 % 2 != 0:
            puntaje2_jugador1 *= 2
    elif (dado1 + dado2 + dado3) % 2 == 0:
        dado_menor = min(dado1, dado2, dado3)
        puntaje2_jugador1 -= dado_menor

elif apuesta1 != 1 and apuesta1 != 2:
    print("La opción ingresada no es correcta")

print("El puntaje obtenido en la segunda ronda por el jugador 1 fue: ", puntaje2_jugador1)

# Jugador 2:
apuesta2 = int(
    input("\n\nhola jugador 2, Debe elegir su apuesta: (presione '1' para elegir par o '2' para elegir impar: "))
if apuesta2 == 1:
    print("Opción elegida: ", apuesta2)
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    dado3 = random.randint(1, 6)
    print("\nJugador2:\n\tLos dados tirados por el jugador 2 fueron:\n\t", "dado1: ", dado1, "\n\t", "dado2: ", dado2,
          "\n\t", "dado3: ", dado3)
    if (dado1 + dado2 + dado3) % 2 == 0:
        dado_mayor = max(dado1, dado2, dado3)
        puntaje2_jugador2 += dado_mayor
        if dado1 % 2 == 0 and dado2 % 2 == 0 and dado3 % 2 == 0:
            puntaje2_jugador2 *= 2
    elif (dado1 + dado2 + dado3) % 2 != 0:
        dado_menor = min(dado1, dado2, dado3)
        puntaje2_jugador2 -= dado_menor

elif apuesta2 == 2:
    print("Opción elegida: ", apuesta2)
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    dado3 = random.randint(1, 6)
    print("\nJugador2:\n\tLos dados tirados por el jugador 2 fueron:\n\t", "dado1: ", dado1, "\n\t", "dado2: ", dado2,
          "\n\t", "dado3: ", dado3)
    if (dado1 + dado2 + dado3) % 2 != 0:
        dado_mayor = max(dado1, dado2, dado3)
        puntaje2_jugador2 += dado_mayor
        if dado1 % 2 != 0 and dado2 % 2 != 0 and dado3 % 2 != 0:
            puntaje2_jugador2 *= 2
    elif (dado1 + dado2 + dado3) % 2 == 0:
        dado_menor = min(dado1, dado2, dado3)
        puntaje2_jugador2 -= dado_menor

elif apuesta1 != 1 and apuesta1 != 2:
    print("La opción ingresada no es correcta")

print("El puntaje obtenido en la segunda ronda por el jugador 2 fue: ", puntaje2_jugador2)

# final del juego
print("\n\t\t\t*********Fin del juego*********\nResultados:\n")
puntaje1_total = puntaje1_jugador1 + puntaje2_jugador1
puntaje2_total = puntaje1_jugador2 + puntaje2_jugador2
print("\nJugador1: ", jugador1, "\n\tPuntaje total obtenido: ", puntaje1_total)
print("\nJugador2: ", jugador2, "\n\tPuntaje total obtenido: ", puntaje2_total)
if puntaje1_total > puntaje2_total:
    print("\nEl ganador es: ", jugador1)
elif puntaje2_total > puntaje1_total:
    print("\nEl ganador es: ", jugador2)
elif puntaje1_total == puntaje2_total:
    print("\nSe produjo un empate entre ambos jugadores")
