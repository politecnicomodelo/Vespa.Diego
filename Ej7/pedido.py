from datetime import date
class pedido (object):
    fecha_creacion=None
    persona=None
    hora_entrega=None
    plato=None
    nro_ped=None
    estado=None

    def setFecha(self,f):
        self.fecha_creacion=f

    def setPersona(self,p):
        self.persona=p

    def addHoraEntrega(self,h):
        self.hora_entrega=h

    def setNro(self,n):
        self.nro_ped=n

