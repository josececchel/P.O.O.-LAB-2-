class Socio:
    def __init__(self, nombre, apellido, nick, password, id, librosalquilados, domicilio, telefono, deuda):
        self.nombre = nombre
        self.apellido = apellido
        self.nick = nick
        self.password = password
        self.id = id
        self.librosalquilados = librosalquilados
        self.domicilio = domicilio
        self.telefono = telefono
        self.deuda = deuda
        self.librosensupoder = []

    # GETTERS de SOCIO
    def getNombre(self):
        nombre = self.nombre
        return nombre
    def getApellido(self):
        apellido = self.apellido
        return apellido
    def getNick(self):
        nick = self.nick
        return nick
    def getPassword(self):
        password = self.password
        return password
    def getId(self):
        mensaje = f"{self.id}"
        return mensaje
    def getLibrosAlquilados(self):
        librosAlquilados = self.librosalquilados
        return librosAlquilados
    def getdomicilio(self):
        domicilio = self.domicilio
        return domicilio
    def gettelefono(self):
        telefono = self.telefono
        return telefono
    def getdeuda(self):
        deuda = self.deuda
        return deuda

    # SETTERS de SOCIO
    def setNombre(self, nuevoNombre):
        self.nombre = nuevoNombre
    def setApellido(self, nuevoApellido):
        self.apellido = nuevoApellido
    def setNick(self, nuevoNick):
        self.nick = nuevoNick
    def setPassword(self, nuevoPassword):
        self.password = nuevoPassword
    def setId(self, nuevoId):
        self.id = nuevoId
    def setLibrosAlquilados(self, cantAlquilada):
        self.librosalquilados = cantAlquilada
    def setdomicilio(self, nuevoDomicilio):
        self.domicilio = nuevoDomicilio
    def settelefono(self, nuevoTelefono):
        self.telefono = nuevoTelefono
    def setdeuda(self, nuevaDeuda):
        self.deuda = nuevaDeuda

    # STR
    def __str__(self):
        texto = f"{self.nombre};{self.apellido};{self.nick};{self.password};{self.id};{self.librosalquilados};{self.domicilio};{self.telefono};{self.deuda}\n"
        return texto