class persona (object):
    nombre=""
    apellido=""
    dni=None

    def setDni(self,d):
        self.dni=d

    def setNombre(self,n):
        self.nombre=n

    def setApellido(self,a):
        self.apellido=a

    def getDescuento(self):
        return 0