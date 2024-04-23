__author__ = 'GRUPO TP3-G159'
from soporte import *


def main():
    opcion = -1
    opcion1 = opcion3 = False
    libros = []
    genero_mayor = subopcion = 0
    print(colores(
        "\n\t\t\t############################################### BIENVENIDO AL PROGRAMA ###################"
        "############################\n",
        "cyan"))
    print(
        colores("\t\t\t\t\t\t\t\t\t\t\t\t\t\t############################ \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t>>>>", "cyan"),
        sep="", end="")
    print(colores("\t  TP 3 AED"), sep="", end="")
    print(colores("\t\t<<<<\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t############################\n", "cyan"), sep="", end="")
    print()
    while opcion != 8:
        opcion = menu()

        if opcion == 1:
            opcion1 = True
            subopcion = -1
            while subopcion != 1 and subopcion != 2:
                subopcion = int(input("Ingrese una opción valida (1 - Carga manual, 2 - Carga automática): "))
            if subopcion == 1:
                # CORRECCION: Está en las dos ramas, debería estar fuera
                n = validar_valor(0)
                libros = [0] * n
                cargar_vector_registro(libros)
            else:
                n = validar_valor(0)
                libros = [0] * n
                carga_automatica(libros, n)
                print()
                print(colores("{:^137}".format("************* Generación automática *************"), "azul"))
                print()
                mostrar_registro(libros)

        elif opcion == 2:
            if opcion1:
                seleccion_directa(libros)
                mostrar_genero_idioma(libros)
            else:
                print(colores("Debe generar o cargar un libro", "rojo"))

        elif opcion == 3:
            if opcion1:
                vector_genero_contador = filtrado_genero_conteo(libros)
                mostrar_filtrados_conteo(vector_genero_contador)
                genero_mayor = mayor_genero(vector_genero_contador)
                mostrar_genero_mayor(vector_genero_contador, genero_mayor)
                opcion3 = True
            else:
                print(colores("Debe generar o cargar un libro", "rojo"))

        elif opcion == 4:
            if opcion1:
                idioma_i = int(input("Ingrese el idioma (1: español, 2: inglés, 3: francés, 4:italiano, 5:otros): "))
                precio_mayor, titulo = filtrar_idioma_mayor(libros, idioma_i)
                if titulo != 0 and precio_mayor != 0:
                    print(colores("El libro de mayor precio para el idioma buscado es: titulo : {}, precio: {}".
                          format(titulo, precio_mayor), "azul"))
                    print()
                else:
                    print("No se encontraron libros con el idioma buscado")
            else:
                print(colores("Debe generar o cargar un libro", "rojo"))

        elif opcion == 5:
            if opcion1:
                if subopcion == 1:
                    x = input("Ingrese el código ISBN del libro a buscar: ")
                    indice_buscado = busqueda_secuencial(libros, x)
                    if indice_buscado != -1:
                        mostrar_libro_isbn(libros, indice_buscado)
                    else:
                        print(colores("No existe un libro con el código ISBN ingresado", "rojo"))
                else:
                    # CORRECCION: Está todo duplicado
                    x = input("Ingrese el código ISBN del libro a buscar: ")
                    vector_codigo = isbn_vector(x)
                    indice_buscado_vector_codigo = busqueda_secuencial2(libros, vector_codigo)
                    if indice_buscado_vector_codigo != -1:
                        mostrar_libro_isbn(libros, indice_buscado_vector_codigo)
                    else:
                        print(colores("No existe un libro con el código ISBN ingresado", "rojo"))
                        print()
            else:
                print(colores("Debe generar o cargar un libro", "rojo"))

        elif opcion == 6:
            if opcion1 and opcion3:
                ordenar_precio_genero(libros)
                mostrar_precio_genero(libros, genero_mayor)
            else:
                print(colores("Debe ingresar a las opciones 1 y 3 antes de esta", "rojo"))

        elif opcion == 7:
            if opcion1:
                n = int(input("Ingrese la cantidad de libros que necesita: "))
                isbn_x = [0]*n
                carga_punto7(isbn_x)
                posiciones_punto7 = busqueda_catalogo_punto7(libros, isbn_x)
                total_precios_libros = mostrar_libros(libros, posiciones_punto7, isbn_x)
                print("El total a abonar por los libros que se encuentran disponibles es: {}".format
                      (total_precios_libros))
                print()
            else:
                print(colores("Debe generar o cargar un libro", "rojo"))
                print()

        elif opcion == 8:
            print(colores("{:^137}".format("***************** Fin del programa *****************"), "rojo"))


if __name__ == '__main__': 
    main()
