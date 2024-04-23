import random


class Libro:
    def __init__(self, titulo, revisiones, publicacion, codigo, rating, isbn):
        self.titulo = titulo
        self.revisiones = revisiones
        self.publicacion = publicacion
        self.codigo = codigo
        self.rating = rating
        self.isbn = isbn


def str_tolibro(linea):
    token = split_line(linea)  # me devuelve esto al hacer el split: ['n5u8n7v76n7kfyhsneiojp37', 'Fede Bett', '1', '1', '1000.0', '200.0']
    titulo = token[0]
    revisiones = int(token[1])
    publicacion = int(token[2])
    codigo = int(token[3])
    rating = float(token[4])
    isbn = token[5]
    return Libro(titulo, revisiones, publicacion, codigo, rating, isbn)


def split_line(linea, sep=','):
    t = []
    initial_pos = 0
    for i in range(len(linea)):
        if linea[i] == sep:
            comma_pos = i

            if initial_pos == comma_pos:
                t.append(linea[initial_pos: comma_pos + 1])
            else:
                t.append(linea[initial_pos: comma_pos])
            initial_pos = i + 1

    if initial_pos < len(linea):
        t.append(linea[initial_pos:])

    return t


def mostrar_registro(l):
    print("TItulo: {} - Revisiones: {} - Publicacion: {} - Codigo: {} - Rating: {} - ISBN: {}".format(l.titulo,
                                            l.revisiones, l.publicacion, l.codigo, l.rating, l.isbn))