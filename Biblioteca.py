from Libro import Libro
class Biblioteca:
    def __init__(self, libros, socios):
        self.libros = libros
        self.socios = socios

    def getLibros(self):
        """
        MUESTRA EL NOMBRE DE LOS LIBROS EN BIBLIOTECA
        :return:
        """
        for libro in self.libros:
           print(libro.getName())
    def getSocios(self):
        """
        MUESTRA EL NOMBRE DE LOS SOCIOS EN BIBLIOTECA
        :return:
        """
        for socio in self.socios:
            print(socio.getNombre())
    def buscarlibro(self, nombreBuscado):
        """
        :param nombreBuscado: Se ingresa el nombre de algún libro p ver si está en biblioteca
        :return: none... muestra si X libro está o no en biblioteca
        """
        for libro in self.libros:
            nombre = libro.getName()
            if nombreBuscado == nombre:
                #print(f"el libro {nombreBuscado} sí está en la biblioteca")
                return libro
        return None
    def buscarsocio(self, socioBuscado):
        """
        :param socioBuscado: Se ingresa el nombre de algún socio p ver si está en la lista
        :return: none... muestra si X socio está o no en la lista
        """
        for socio in self.socios:
            nombre = socio.getNombre()
            if socioBuscado == nombre:
                #print(f"el libro {nombreBuscado} sí está en la biblioteca")
                return socio
        return None