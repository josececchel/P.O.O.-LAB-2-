class Libro:
    def __init__(self, nombre, autor, editorial, anio, cantidadtotal = 0, noalquilados = 0):
        self.nombre = nombre
        self.autor = autor
        self.editorial = editorial
        self.anio = anio
        self.cantidadtotal = cantidadtotal
        self.noalquilados = noalquilados

    # GETTERS de LIBRO
    def getName(self):
        nombre = self.nombre
        return nombre
    def getAutor(self):
        autor = self.autor
        return autor
    def geteditorial(self):
        editorial = self.editorial
        return editorial
    def getanio(self):
        anio = self.anio
        return anio
    def getcantidadtotal(self):
        cantidadtotal = self.cantidadtotal
        return cantidadtotal
    def getnoalquilados(self):
        noalquilados = self.noalquilados
        return noalquilados

    # STR
    def __str__(self):
        texto = f"{self.nombre};{self.autor};{self.editorial};{self.anio};{self.cantidadtotal};{self.noalquilados}\n"
        return texto

    # SETTERS de LIBRO
    def setName(self, nuevoNombre):
        self.nombre = nuevoNombre
    def setAutor(self, nuevoAutor):
        self.autor = self.nuevoAutor
    def seteditorial(self, nuevaEditorial):
        self.editorial = nuevaEditorial
    def setanio(self, nuevoAnio):
        self.anio = nuevoAnio
    def setcantidadtotal(self, nuevaCantTotal):
        self.cantidadtotal = nuevaCantTotal
    def setnoalquilados(self, libNoAlquilados):
        self.noalquilados = libNoAlquilados