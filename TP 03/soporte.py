__author__ = 'GRUPO TP3-G159'
import random


class Libro:
    def __init__(self, isbn, tit, gen, idio, pre):
        self.codigo = isbn
        self.titulo = tit
        self.genero = gen
        self.idioma = idio
        self.precio = pre


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


def carga_automatica(libros, n):
    titulos = ("El Quijote", "La Odisea", "La Ilíada", "La Divina Comedia", "Hamlet", "En Busca del Tiempo",
               "Perdido", "La Eneida", "Ensayos", "Cumbres Borrascosas", "Edipo Rey", "El Rey Lear",
               "Las Mil y Una Noches", "Perseverante", "Mundo Magnifico", "Oso Polar", "Truenos de noche",
               "Drama Total", "Sao")
    generos = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    idiomas = (1, 2, 3, 4, 5)
    numeros = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
    for j in range(n):
        # CORRECCION: se podría hacer usando una bandera, en vez de poner un valor en duro para entrar a la función
        codigo = [0] * 10
        codigo[2] = str(2)
        while not es_numero(codigo):
            codigo = [0] * 13
            indice1 = indice2 = indice3 = 0
            # CORRECCION: Para que está el while? siempre se va a ejecutar una sola vez.
            while indice1 == 0:
                indice1 = random.randint(1, 11)
            indice2 = random.randint(1, 11)
            while indice2 + 1 == indice1 or indice2 - 1 == indice1 or indice2 == indice1:
                indice2 = random.randint(1, 11)
            indice3 = random.randint(1, 11)
            while indice3 + 1 == indice1 or indice3 - 1 == indice1 or indice3 + 1 == indice2 or indice3 - 1 == indice2 or indice3 == indice1 or indice3 == indice2:
                indice3 = random.randint(1, 11)
            codigo[indice1] = "-"
            codigo[indice2] = "-"
            codigo[indice3] = "-"
            n = len(codigo)
            for i in range(n):
                if codigo[i] != "-":
                    # CORRECCION: El último digito, que es el verificador, lo podrían calcular en vez de hacerlo random.
                    codigo[i] = random.choice(numeros)
        titulo = random.choice(titulos)
        # CORRECCION: Tendrían que usar randint
        genero = random.choice(generos)
        idioma = random.choice(idiomas)
        precio = random.randint(1000, 30000)
        libros[j] = Libro(codigo, titulo, genero, idioma, precio)


def menu():
    print(colores("{:^137}".format("***************************** Menú de opciones *****************************"),
                  "amarillo"))
    print("1_ Generación y carga")
    print("2_ Mostrar")
    print("3_ Conteo y género más popular")
    print("4_ Búsqueda de mayor")
    print("5_ Búsqueda por ISBN")
    print("6_ Consulta de un género")
    print("7_ Consulta de precio por grupo")
    print("8_ Salir")
    print("*" * 60, "\n")
    opcion = int(input(colores("Ingrese una opción: ", "blanco")))
    return opcion


def validar_valor(valor):
    n = valor
    while n <= valor:
        n = int(input(colores("Ingrese la cantidad de libros: ", "blanco")))
        if n <= valor:
            print(colores("El número ingresado no es valido", "rojo"))
    return n


def cargar_vector_registro(v):
    n = len(v)
    for i in range(n):
        isbn = validar_codigo(input("Ingrese el código ISBN: "))
        tit = input("Ingrese el titulo del libro: ")
        gen = validar_genero(int(input(
            "Ingrese un género (0: Autoayuda, 1: Arte, 2: Ficción, 3: Computación, 4: Economía,"
            " 5: Escolar, 6: Sociedad, 7: Gastronomía, 8: Infantil , 9: Otros): ")))
        idio = validar_idioma(
            int(input("Ingrese el idioma del libro (1: español, 2: inglés, 3: francés, 4: italiano, 5: otros): ")))
        precio = int(input("Ingrese el precio del libro: "))
        v[i] = Libro(isbn, tit, gen, idio, precio)
        print("*" * 20)


def validar_genero(n1):
    n = n1
    if 0 <= n <= 9:
        return n
    else:
        while n < 0 or n > 9:
            n = int(input(
                "Ingrese un género valido (0: Autoayuda, 1:Arte, 2: Ficción, 3: Computación, 4:"
                " Economía, 5: Escolar, 6: Sociedad, 7: Gastronomía, 8: Infantil , 9: Otros): "))
        return n


def validar_idioma(n1):
    n = n1
    if 1 <= n <= 5:
        return n
    else:
        while n < 1 or n > 5:
            n = int(input("Ingrese un idioma valido (1: español, 2: inglés, 3: francés, 4:italiano, 5:otros): "))
        return n


def validar_codigo(codigo):
    contador_guion = 0
    contador_guiones_seguidos = 0
    guiones_seguidos = False
    for carac in codigo:
        if carac == "-":
            contador_guion += 1
            contador_guiones_seguidos += 1
            if contador_guiones_seguidos == 2:
                guiones_seguidos = True
        else:
            contador_guiones_seguidos = 0

    while len(codigo) != 13 or contador_guion != 3 or guiones_seguidos or not es_numero(codigo):
        codigo = input("Ingrese el código de identificación (ISBN): ")
        # CORRECCION: Termina repitiendo toda la validación
        contador_guion = 0
        contador_guiones_seguidos = 0
        guiones_seguidos = False
        for carac in codigo:
            if carac == "-":
                contador_guion += 1
                contador_guiones_seguidos += 1
                if contador_guiones_seguidos == 2:
                    guiones_seguidos = True
            elif carac != "-":
                contador_guiones_seguidos = 0
    return codigo


def es_numero(codigo):
    contador_posicion = 10
    acumulador = 0
    for car in codigo:
        if car in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
            numero = int(car)
            acumulador += numero * contador_posicion
            contador_posicion -= 1
    if acumulador % 11 == 0:
        return True
    else:
        return False


def mostrar_genero_idioma(libros):
    generos = ["Autoayuda", "Arte", "Ficción", "Computación", "Economía", "Escolar", "Sociedad", "Gastronomía",
               "Infantíl", "Otros"]
    idiomas = ["Español", "Inglés", "Francés", "Italiano", "Otros"]
    n = len(libros)
    print(colores("{:^137}".format("***************** Libros ordenados por titulo en forma ascendente: *******"
                                   "**********"), "violeta"))
    print()
    for i in range(n):
        # CORRECCION: Falta el precio
        print("Libro " + str(i + 1) + ": " + "Titulo: {}, Genero: {}, Idioma: {}".format(libros[i].titulo,
                                                                                         generos[libros[i].genero],
                                                                                         idiomas[libros[i].idioma - 1]))
    print()


def seleccion_directa(libros):
    n = len(libros)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if libros[i].titulo > libros[j].titulo:
                libros[i], libros[j] = libros[j], libros[i]


def filtrado_genero_conteo(libros):
    n = len(libros)
    vector_genero_contador = [0] * 10
    for i in range(n):
        vector_genero_contador[libros[i].genero] += 1
    return vector_genero_contador


def mostrar_filtrados_conteo(vector_genero_contador):
    # CORRECCION: Está duplicando el array, deberia declararse una sola vez
    generos = ["Autoayuda", "Arte", "Ficción", "Computación", "Economía", "Escolar", "Sociedad", "Gastronomía",
               "Infantíl", "Otros"]
    n = len(vector_genero_contador)
    print(colores("{:^137}".format("***************** Cantidad de libros por genero *****************")))
    print()
    #print("*" * 20 + " Cantidad de libros por genero " + "*" * 20)
    for i in range(n):
        if vector_genero_contador[i] != 0:
            print("Genero:", generos[i], " - Cantidad:", vector_genero_contador[i])


def mayor_genero(vector_genero_contador):
    genero_mayor = posicion = 0
    n = len(vector_genero_contador)
    for i in range(n):
        if i == 0:
            genero_mayor = vector_genero_contador[0]
            posicion = i
        else:
            if vector_genero_contador[i] > genero_mayor:
                genero_mayor = vector_genero_contador[i]
                posicion = i
    return posicion


def mostrar_genero_mayor(vector_genero_contador, genero_mayor):
    generos = ["Autoayuda", "Arte", "Ficción", "Computación", "Economía", "Escolar", "Sociedad", "Gastronomía"
        , "Infantíl", "Otros"]
    print("Genero con mayor cantidad de libros ofrecidos: {}, Cantidad: {}".format(generos[genero_mayor],
                                                                                   vector_genero_contador[
                                                                                       genero_mayor]))
    print()


def filtrar_idioma_mayor(libros, idioma_i):
    n = len(libros)
    contador = precio_mayor = 0
    titulo = 0
    for i in range(n):
        # CORRECCION: Repite la condición del idioma en las dos ramas
        if libros[i].idioma == idioma_i and contador == 0:
            precio_mayor = libros[i].precio
            titulo = libros[i].titulo
        else:
            if libros[i].idioma == idioma_i:
                if libros[i].precio > precio_mayor:
                    precio_mayor = libros[i].precio
                    titulo = libros[i].titulo
        contador += 1
    return precio_mayor, titulo


def mostrar_registro(libros):
    n = len(libros)
    for i in range(n):
        print("Libro: {}, codigo: {}, titulo: {}, genero: {}, idioma = {}, precio: {}".format(i + 1,
                                                                                    carac_isbn(libros[i].codigo),
                                                                                    libros[i].titulo,
                                                                                    libros[i].genero,
                                                                                    libros[i].idioma,
                                                                                    libros[i].precio))
    print()


def busqueda_secuencial(libros, x):
    for i in range(len(libros)):
        if x == libros[i].codigo:
            return i
    return -1


def busqueda_secuencial2(libros, vector_x):
    for i in range(len(libros)):
        if vector_x == libros[i].codigo:
            return i
    return -1


def mostrar_libro_isbn(libros, indice):
    indice_buscado = indice
    if libros[indice_buscado].precio != 0:
        porcentaje10 = (10*libros[indice_buscado].precio)/100
        libros[indice_buscado].precio += porcentaje10
    generos = ["Autoayuda", "Arte", "Ficción", "Computación", "Economía", "Escolar", "Sociedad", "Gastronomía",
               "Infantíl", "Otros"]
    idiomas = ["Español", "Inglés", "Francés", "Italiano", "Otros"]
    print(colores("Libro; titulo: {}, genero: {}, idioma: {}, precio: {}".format(libros[indice_buscado].titulo,
                                                                         generos[libros[indice_buscado].genero],
                                                                         idiomas[libros[indice_buscado].idioma - 1],
                                                                         libros[indice_buscado].precio), "azul"))
    print(colores("Su precio aumentó un 10%", "azul"))
    print()


def isbn_vector(codigo):
    v = []
    for carac in codigo:
        v.append(carac)
    return v


def ordenar_precio_genero(libros):
    n = len(libros)
    for i in range(n-1):
        for j in range(i+1, n):
            if libros[i].precio < libros[j].precio:
                libros[i], libros[j] = libros[j], libros[i]


def mostrar_precio_genero(libros, genero_mayor):
    n = len(libros)
    print()
    for i in range(n):
        if libros[i].genero == genero_mayor:
            print("Libro {}; Código ISBN: {}, Titulo: {}, Genero: {}, Idioma: {}, Precio: {}".format(i, carac_isbn(
                                                                                    libros[i].codigo),
                                                                                    libros[i].titulo,
                                                                                    libros[i].genero,
                                                                                    libros[i].idioma,
                                                                                    libros[i].precio))
    print()


def carga_punto7(isbn_x):
    n = len(isbn_x)
    for i in range(n):
        isbn_x[i] = validar_codigo(input("Ingrese el codigo ISBN del libro {}: ".format(i + 1)))


def busqueda_catalogo_punto7(libros, isbn_x):
    n = len(isbn_x)
    m = len(libros)
    posiciones_punto7 = [None]*n
    for i in range(n):
        for j in range(m):
            if isbn_vector(isbn_x[i]) == isbn_vector(libros[j].codigo):
                posiciones_punto7[i] = j
    return posiciones_punto7


def carac_isbn(v):
    a = ""
    for i in range(len(v)):
        a += v[i]
    return a


def mostrar_libros(libros, posiciones_punto7, isbn_x):
    total_precios_libros = 0
    n = len(posiciones_punto7)
    print()
    print(colores("{:^137}".format("***************** Consulta de precio por grupo *****************"), "cyan"))
    print()
    for i in range(n):
        # CORRECCION: Debía mostrarse todos los libros encontrados primero y los no despues
        if posiciones_punto7[i] != None:
            total_precios_libros += libros[posiciones_punto7[i]].precio
            print("Libro {}; Codigo: {}, Titulo: {}, Precio: {}".format(i+1, isbn_x[i],
                                                                        libros[posiciones_punto7[i]].titulo,
                                                                        libros[posiciones_punto7[i]].precio))
        else:
            print("El libro cuyo codigo ingresado fue {} no se encuentra en el catalogo".format(isbn_x[i]))
    return total_precios_libros
