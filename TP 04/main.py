from registro import *
import os.path
import pickle


def menu():
    # print("\nMenu de opciones:")
    print(colores("\nMenu de opciones:", "amarillo"))
    print("1 - Cargar libros")
    print("2 - Sumar revisión")
    print("3 - Mayor revisiones")
    print("4 - Popularidad 2000")
    print("5 - Publicaciones por década")
    print("6 - Guardar populares")
    print("7 - Mostrar archivo")
    print("8 - Salir")
    opcion = int(input(colores("Ingrese una opción: ", "blanco")))
    return opcion


def colores(text, color="blanco"):
    new_text = ""
    if color == "blanco":
        new_text = chr(27) + "[1;38m" + text
    elif color == "rojo":
        new_text = chr(27) + "[0;31m" + text
    elif color == "azul":
        new_text = chr(27) + "[0;34m" + text
    elif color == "amarillo":
        new_text = chr(27) + "[1;33m" + text
    elif color == "verde":
        new_text = chr(27) + "[0;32m" + text
    elif color == "naranja":
        new_text = chr(27) + "[0;33m" + text
    elif color == "violeta":
        new_text = chr(27) + "[0;35m" + text
    elif color == "cyan":
        new_text = chr(27) + "[0;36m" + text
    return new_text


def efecto():
    print(colores(
        "\n\t\t\t############################################### BIENVENIDO AL PROGRAMA ###################"
        "############################\n",
        "cyan"))
    print(
        colores("\t\t\t\t\t\t\t\t\t\t\t\t\t\t############################ \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t>>>>", "cyan"),
        sep="", end="")
    print(colores("\t  TP 4 AED"), sep="", end="")
    print(colores("\t\t<<<<\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t############################\n", "cyan"), sep="", end="")
    print()


def cargar_vector_libros(v, nombre):
    if os.path.exists(nombre):
        archivo = open("libros.csv", mode="rt", encoding="utf8")
        cantidad = 0
        for linea in archivo:
            # linea me devuelve algo asi: A Short History of Nearly Everything,9545,2004,1,4.21,076790818X
            if cantidad > 0:
                libro = str_tolibro(linea[:-1])
                insertar_ordenado(v, libro)
            cantidad += 1
        archivo.close()
    return v


def insertar_ordenado(v, libro):
    n = len(v)
    izq = 0
    pos = -1
    der = n - 1
    while izq <= der:
        c = (izq + der) // 2
        if v[c].isbn == libro.isbn:
            pos = c
            break
        if libro.isbn > v[c].isbn:
            izq = c + 1
        else:
            der = c - 1

    if izq > der:
        pos = izq

    v[pos:pos] = [libro]


def busqueda_binaria(v, x):
    izq, der = 0, len(v) - 1
    while izq <= der:
        c = (izq + der) // 2
        if x == v[c].isbn:
            return v[c]
        if x < v[c].isbn:
            der = c - 1
        else:
            izq = c + 1
    return -1


def busqueda_secuencial(v, x):
    for i in range(len(v)):
        if x == v[i].titulo:
            return v[i]
    return -1


def libro_mayor_revisiones(libros):
    n = len(libros)
    mayor = 0
    registro = None
    for i in range(n):
        if i == 0 or libros[i].revisiones > mayor:
            mayor = libros[i].revisiones
            registro = libros[i]
    return registro


def calcular_promedio(libros, codigo):
    total = 0
    cantidad = 0
    for libro in libros:
        if libro.codigo == codigo:
            cantidad += 1
            total += libro.rating
    return total // cantidad


def mayor_rating_punto4(libros, id, a):
    mayor = 0
    registro = None
    for libro in libros:
        if libro.codigo == id and libro.publicacion == a:
            if libro.rating > mayor:
                mayor = libro.rating
                registro = libro
    return registro


def cargar_matriz(libros):
    # año = Columnas
    # idioma = Filas
    filas = 27
    columnas = 21
    contadorc = 0
    matriz = [[0] * columnas for i in range(filas)]
    for f in range(filas):
        contadorc = -1
        for a in range(2000, 2021):
            contadorc += 1
            matriz[f][contadorc] = mayor_rating_punto4(libros, f, a)
            if matriz[f][contadorc] is not None:
                if matriz[f][contadorc].rating != 0:
                    print("Mayor rating de libro con codigo de idioma {} y año de publicación {}: {}".format(f, a,
                                                                                    matriz[f][contadorc].rating))
    return matriz


def filtrar_numero(numero):
    if numero in range(1900, 1910):
        return 0
    elif numero in range(1910, 1920):
        return 1
    elif numero in range(1920, 1930):
        return 2
    elif numero in range(1930, 1940):
        return 3
    elif numero in range(1940, 1950):
        return 4
    elif numero in range(1950, 1960):
        return 5
    elif numero in range(1960, 1970):
        return 6
    elif numero in range(1970, 1980):
        return 7
    elif numero in range(1980, 1990):
        return 8
    elif numero in range(1990, 2000):
        return 9


def numero_decada(numero):
    if numero == 0:
        return "1900 - 1909"
    elif numero == 1:
        return "1910 - 1919"
    elif numero == 2:
        return "1920 - 1929"
    elif numero == 3:
        return "1930 - 1939"
    elif numero == 4:
        return "1940 - 1949"
    elif numero == 5:
        return "1950 - 1959"
    elif numero == 6:
        return "1960 - 1969"
    elif numero == 7:
        return "1970 - 1979"
    elif numero == 8:
        return "1980 - 1989"
    elif numero == 9:
        return "1990 - 1999"


def cargar_vector_conteo(libros):
    vector_conteo = [0]*10
    for libro in libros:
        if libro.publicacion in range(1900, 2000):
            a = libro.publicacion
            indice = filtrar_numero(a)
            vector_conteo[indice] += 1
    return vector_conteo


def mostrar_vector_conteo(v):
    n = len(v)
    for i in range(n):
        if v[i] > 0:
            decada = numero_decada(i)
            print("Cantidad de libros vendidos decada {}: {}".format(decada, v[i]))


def decada_mayor(v):
    n = len(v)
    mayor = 0
    posicion = 0
    for i in range(n):
        if i == 0 or v[i] > mayor:
            mayor = v[i]
            posicion = i
    return posicion


def generar_archivo(matriz):
    archivo = open("populares.dat", "wb")
    n = len(matriz)
    m = len(matriz[0])
    contador_registros = 0
    for f in range(n):
        for c in range(m):
            if matriz[f][c] is not None:
                pickle.dump(matriz[f][c], archivo)
                contador_registros += 1
    archivo.close()
    return contador_registros


def mostrar_archivo():
    if not os.path.exists('populares.dat'):
        print('No se ha creado el archivo!')
        return

    archivo = open('populares.dat', 'rb')
    tam = os.path.getsize('populares.dat')
    while archivo.tell() < tam:
        l = pickle.load(archivo)
        mostrar_registro(l)
        print()
    archivo.close()


def main():
    efecto()
    opcion = 0
    libros = []
    matriz = None
    while opcion != 8:
        opcion = menu()

        if opcion == 1:
            libros = cargar_vector_libros(libros, "libros.csv")
            print("libros cargados correctamente..")

        elif opcion == 2:
            if len(libros) != 0:
                carga = int(input("Ingrese la el modo de búsqueda (1 - ISBN, 2 - titulo): "))
                if carga == 1:
                    isbn = input("Ingrese el ISBN: ")
                    registro = busqueda_binaria(libros, isbn)
                    if registro != -1:
                        print("Libro encontrado:")
                        mostrar_registro(registro)
                        registro.revisiones += 1
                        print("Se le ha sumado una revisión al libro..")
                    else:
                        print("No existe el libro con el criterio buscado..")
                elif carga == 2:
                    titulo = input("Ingrese el titulo: ")
                    registro = busqueda_secuencial(libros, titulo)
                    if registro != -1:
                        print("Libro encontrado:")
                        mostrar_registro(registro)
                        registro.revisiones += 1
                        print("Se le ha sumado una revisión al libro..")
                    else:
                        print("No existe el libro con el criterio buscado..")
                else:
                    print("La opción ingresada no es valida..")
            else:
                print("Debe cargar los libros primero..")

        elif opcion == 3:
            if len(libros) != 0:
                mayor = libro_mayor_revisiones(libros)
                promedio = calcular_promedio(libros, mayor.codigo)
                if mayor.revisiones == promedio:
                    print("El rating del libro con mayor cantidad de revisiones es igual al rating promedio de su "
                          "mismo idioma.")
                elif mayor.revisiones > promedio:
                    print("El rating del libro con mayor cantidad de revisiones es mayor al rating promedio de su "
                          "mismo idioma.")
                else:
                    print("El rating del libro con mayor cantidad de revisiones es menor al rating promedio de su "
                          "mismo idioma.")
            else:
                print("No se han cargado libros..")

        elif opcion == 4:
            if len(libros) != 0:
                matriz = cargar_matriz(libros)
            else:
                print("No se han cargado libros..")

        elif opcion == 5:
            if len(libros) != 0:
                vector_conteo = cargar_vector_conteo(libros)
                mostrar_vector_conteo(vector_conteo)
                ind = decada_mayor(vector_conteo)
                dec = numero_decada(ind)
                print("La decada con más publicaciones fue {} con un total de: {} publicaciones".format(dec,
                                                                                            vector_conteo[ind]))
            else:
                print("No se han cargado libros..")

        elif opcion == 6:
            if matriz is not None:
                contador_registros = generar_archivo(matriz)
                print("La cantidad de registros grabados en el archivo es:", contador_registros)
            else:
                print("Se debe cargar la matriz en el punto 4..")

        elif opcion == 7:
            mostrar_archivo()

        elif opcion == 8:
            print("Fin de programa...")


if __name__ == '__main__':
    main()
