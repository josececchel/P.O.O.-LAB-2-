from Libro import Libro
from Biblioteca import Biblioteca
from Socio import Socio

def abrirarchivolibros(nombreArchivoLibros):
    """
    :param nombreArchivoLibros: abre el archivo de los libros
    :return: devuelve [] con cada libro (como lista)
    """
    listadoDeLibros = []
    archivoCorrecto = True
    while archivoCorrecto == True:
        try:
            with open(nombreArchivoLibros, "r") as archivo:
                archivoAbierto = archivo.readlines()
                for linea in archivoAbierto:
                    libro = linea.strip().split(";")
                    listadoDeLibros.append(libro)
                archivoCorrecto = False
            return listadoDeLibros
        except FileNotFoundError:
            print("Archivo de libros no encontrado")
            nombreArchivoLibros = str(input("Ingrese el nombre correcto del archivo de libros"))
def abrirarchivoSocios(nombreArchivoSocios):
    """
    :param nombreArchivoSocios: abre el archivo de los socios
    :return: devuelve [] con cada socio (como lista)
    """
    listadoDeSocios = []
    archivoCorrecto = True
    while archivoCorrecto == True:
        try:
            with open(nombreArchivoSocios, "r") as archivo:
                    archivoAbierto = archivo.readlines()
                    for linea in archivoAbierto:
                        libro = linea.strip().split(";")
                        listadoDeSocios.append(libro)
                    archivoCorrecto = False
            return listadoDeSocios
        except FileNotFoundError:
            print("Archivo de socios no encontrado")
            nombreArchivoSocios = str(input("Ingrese el nombre correcto del archivo de socios"))
def guardararchivoSocios(nombreArchivoSocios, socios):
    with open("nuevo archivo socioooos.txt", "w") as archivo:
        for socio in socios:
            linea = str(socio)
            archivo.write(linea)
def guardararchivoLibros(nombreArchivoLibros, libros):
    with open("nuevo archivo librooos.txt", "w") as archivo:
        for libro in libros:
            linea = str(libro)
            archivo.write(linea)
def menu(opcionElegida, bibliotecaVM, libros, socios, nombreArchivoSocios, nombreArchivoLibros):
    if opcionElegida == 1: # MOSTRAR LIBROS
        print("LIBROS EN EL CATÁLOGO")
        bibliotecaVM.getLibros()
    elif opcionElegida == 2: # MOSTRAR USUARIOS
        print("USUARIOS REGISTRADOS")
        bibliotecaVM.getSocios()
    elif opcionElegida == 3: # BUSCAR SOCIO
        socioBuscado = bibliotecaVM.buscarsocio(str(input("Ingrese el nombre del socio que busca")))
        if socioBuscado:
            print(f"El nombre del socio es: {socioBuscado.getNombre()}, su N° de socio es: {socioBuscado.getId()} y su deuda es de $: {socioBuscado.getdeuda()}")
            print(f"Tiene alquilados: {socioBuscado.getLibrosAlquilados()}")
        else:
            print("El socio no existe")
    elif opcionElegida == 4: # BUSCAR LIBRO
        libroBuscado = bibliotecaVM.buscarlibro(str(input("Ingrese el nombre del libro que busca: ")))
        if libroBuscado:  # SI EL LIBRO ESTÁ EN EL CATÁLOGO INGRESA ACÁ
            print(f"El nombre del libro es: {libroBuscado.getName()} y es del año: {libroBuscado.anio}")
            print(f"La cantidad de ejemplares que tenemos son: {libroBuscado.getcantidadtotal()},y tenemos disponibles: {libroBuscado.getnoalquilados()}")
        else:  # EL LIBRO NO ESTÁ EN EL CATÁLOGO
            print("No tenemos dicho libro en el catálogo")
    elif opcionElegida == 5: # INGRESAR NUEVO SOCIO
        cantSocios = int(input("Ingrese cuantos socios agregará: "))
        for socio in range(cantSocios):
            socio = Socio(nombre=str(input("Nombre: ")), apellido=str(input("apellido: ")),
                          nick=str(input("nick: ")),
                          password=str(input("password: ")),
                          id=(int(input("Ingrese el n° de socio"))),
                          librosalquilados=0,
                          domicilio= str(input("domicilio: ")),
                          telefono= int(input("telefono")),
                          deuda=0)
            socios.append(socio)
        guardararchivoSocios(nombreArchivoSocios, socios)
    elif opcionElegida == 6: # INGRESAR NUEVO/S LIBRO/S
        for libro in range(int(input("Ingrese cuantas obras va a agregar a la biblioteca: "))):
            nombre = str(input("Nombre: "))
            autor = str(input("autor: "))
            editorial =str(input("editorial: "))
            anio = int(input("año: "))
            cantidadtotal = (int(input("Ingrese la cantidad de libros adquiridos de dicha obra")))
            libro = Libro(nombre=nombre, autor=autor, editorial=editorial,
                          anio=anio, cantidadtotal=cantidadtotal, noalquilados=cantidadtotal)
            libros.append(libro)
        guardararchivoLibros(nombreArchivoLibros, libros)
    else: print("Elija una opción correcta")

def main():
    nombreArchivoSocios = "listado de socios.txt"
    listadoDeSocios = abrirarchivoSocios(nombreArchivoSocios)
    socios = [] #LISTA DE SOCIOS (OBJETOS)

    for socio in listadoDeSocios:
        socioObjeto = Socio(nombre=socio[0], apellido=socio[1], nick=socio[2],
                      password=socio[3], id=socio[4], librosalquilados=socio[5], domicilio=socio[6], telefono=socio[7], deuda=socio[8])
        socios.append(socioObjeto) #Guardo cada OBJETO SOCIO en SOCIOS "LISTA DE OBJ SOCIO"

    nombreArchivoLibros = "listado de libros.txt"
    listadoDeLibros = abrirarchivolibros(nombreArchivoLibros)
    libros = [] #LISTA DE LIBROS (OBJETOS)

    for libro in listadoDeLibros:
        libroObjeto = Libro(nombre=libro[0], autor=libro[1], editorial=libro[2],
                      anio=libro[3], cantidadtotal=libro[4], noalquilados=libro[5])
        libros.append(libroObjeto) #Guardo cada OBJETO LIBRO en libros "LISTA DE OBJ LIBRO"

    bibliotecaVM = Biblioteca(libros, socios) #SE CREA UNA BIBLIOTECA Y SE LE PASA LISTA DE LIBROS(OBJETOS) y LISTA DE SOCIOS (OBJETOS)

    opcionElegida = int(input(f"Ingrese la opción que desee, para salir 0:\n "
                              f"1- MOSTRAR CATÁLOGO DE LIBROS\n"
                              f"2- MOSTRAR LISTADO DE SOCIOS\n"
                              f"3- BUSCAR SOCIO\n"
                              f"4- BUSCAR LIBRO\n"
                              f"5- INGRESAR NUEVO SOCIO\n"
                              f"6- INGRESAR NUEVOS LIBROS - DONACION O COMPRA\n"))
    menu(opcionElegida, bibliotecaVM, libros, socios, nombreArchivoSocios, nombreArchivoLibros)

if __name__ == '__main__':
    main()