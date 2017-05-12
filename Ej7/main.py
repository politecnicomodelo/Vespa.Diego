import datetime
from persona import persona
from alumno import alumno
from profesor import profesor
from plato import plato
from pedido import pedido
listaplatos=[]
listapersonas=[]
listapedidos=[]
while (True):
    a=input("Pulse\n"
            "A para agregar \n "
            "M para modificar \n "
            "E para eliminar\n "
            "S para guardar \n"
            "D para mostrar los pedidos del dia")
    if(a == "a"):
        a=input("Pulse A para agregar alumno\n "
                "P para agregar profesor\n "
                "Q para agregar pedido\n "
                "R para agregar plato \n")
        if (a=="a"):
            alumnocreado = alumno()
            a = input("Ingrese el nombre ")
            alumnocreado.setNombre(str(a))
            a = input("Ingrese el apellido ")
            alumnocreado.setApellido(str(a))
            a = input("Ingrese la division ")
            alumnocreado.setDivision(str(a))
            a = input("Ingrese el DNI ")
            alumnocreado.setDni(str(a))
            listapersonas.append(alumnocreado)
        elif (a == "p"):
            profesorcreado = profesor()
            a = input("Ingrese el nombre ")
            profesorcreado.setNombre(str(a))
            a = input("Ingrese el apellido ")
            profesorcreado.setApellido(str(a))
            a = input("Ingrese el descuento ")
            profesorcreado.addDesc(str(a))
            a = input("Ingrese el DNI ")
            profesorcreado.setDni(str(a))
            listapersonas.append(profesorcreado)
        elif (a == "q"):
            pedidocreado=pedido()
            d=int (input("Ingrese el dia de creacion "))
            m=int (input("Ingrese el mes de creacion "))
            an = int (input("Ingrese el ano de creacion "))
            pedidocreado.fecha_creacion=date(an , m, d)
            a = input("Ingrese el DNI de la personas que realizo el pedido ")
            for item in listapersonas:
                if (item.dni==a):
                    pedidocreado.setPersona(item)
            d = input ("Ingrese el dia de entrega")
            m = input("Ingrese el mes de entrega")
            an = input("Ingrese el ano de entrega")
            pedidocreado.addHoraEntrega=date(an, m ,d)
            a = input("Ingrese el nombre del plato a pedir")
            for item in listaplatos:
                if(item.nombre==a):
                    pedidocreado.plato(item)
            a = input("Ingrese el numero de pedido")
            listapersonas.append(pedidocreado)

        elif (a == "r"):
            platocreado=plato()
            a = input("Ingrese el nombre del plato ")
            platocreado.setNombre(str(a))
            a = input("Ingrese el precio del plato ")
            platocreado.setPrecio(str(a))
            listaplatos.append(platocreado)

    elif (a=="m"):
        a=input("Presione A para modificar alumno o profesor \n "
                "Presione Q para modificar el pedido \n "
                "Presione R para modificar el plato \n")
        if(a== "a"):
            for item in listapersonas:
                print(item.dni + "-" + item.nombre + " " + item.apellido)
            a=input("Ingrese el DNI de la persona a modificar")
            for item in listapersonas:
                if(item.dni==a):
                    if(type(item) is alumno):
                        a=input("Ingrese el nuevo nombre del alumno")
                        item.nombre=a
                        a=input("Ingrese el nuevo apellido del alumno")
                        item.apellido=a
                        a=input("Ingrese el nuevo DNI del alumno")
                        item.dni=a
                        a=input("Ingrese la nueva division en la que esta el alumno")
                        item.division=a

                    elif (type(item)is profesor):
                        a=input("Ingrese el nuevo nombre del profesor")
                        item.nombre=a
                        a=input("Ingrese el nuevo apellido del profesor")
                        item.apellido=a
                        a=input("Ingrese el nuevo DNI del profesor")
                        item.dni=a
                        a=input("Ingrese el nuevo descuento que se le aplicara al profesor")
                        item.descuento=a

        elif(a=="q"):
            for item in listapedidos:
                print(item.nro_ped)
            a=input("Ingrese el numero de pedido a modificar")
            for item in listapedidos:
                if (item.nro_ped == a):
                    d=input("Ingrese el nuevo dia de entrega del pedido")
                    m = input("Ingrese el nuevo mes de entrega del pedido")
                    an = input("Ingrese el nuevo ano de entrega del pedido")
                    item.addHoraEntrega = date(an, m, d)

        elif(a=="r"):
            for item in listaplatos:
                print(item.nombre + "-" + item.precio)
            a=input("Ingrese el nombre del plato a modificar")
            for item in listaplatos:
                if(item.nombre == a):
                    a=input("Ingrese el nuevo nombre del plato")
                    item.nombre=a
                    a=input("Ingrese el nuevo precio del plato")
                    item.precio=a

    elif (a=="e"):
        a=input("Presione A para eliminar persona \n "
                "Presione Q para eliminar el pedido \n "
                "Presione R para eliminar el plato \n")
        if(a=="a"):
            a=input("Ingrese el DNI de la persona a eliminar")
            for item in listapersonas:
                if(item.dni==a):
                    listapersonas.remove(item)

        elif(a=="q"):
            a=input("Ingrese el numero de pedido a eliminar")
            for item in listapedidos:
                if(item.nro_ped==a):
                    listapedidos.remove(item)

        elif(a=="r"):
            a=input("Ingrese el nombre del plato a eliminar")
            for item in listaplatos:
                if(item.nombre==a):
                    listaplatos.remove(item)

    elif (a=="s"):
        al = open("al.txt","w")
        for item in listapersonas:
            if(type(item)is alumno):
                al.write(str(item.dni)+ "| ")
                al.write(str(item.nombre) + "| ")
                al.write(str(item.apellido) + "| ")
                al.write(str(item.division) + "| " "\n")
        al.close()
        pr = open("pr.txt", "w")
        for item in listapersonas:
            if (type(item) is profesor):
                pr.write(str(item.dni) + "| ")
                pr.write(str(item.nombre) + "| ")
                pr.write(str(item.apellido) + "| ")
                pr.write(str(item.descuento) + "\n")
        pr.close()

        pe = open("pe.txt","w")
        for item in listapedidos:
            pe.write(str(item.nro_ped)+"| ")
            pe.write(str(item.persona.nombre)+"| ")
            pe.write(str(item.persona.nombre)+"| ")
            if(type(item)is profesor):
                pe.write(str(item.persona.desuento)+"| ")
            pe.write(str(item.plato.nombre)+"| ")
            pe.write(str(item.plato.precio)+"| ")
            pe.write(str(item.hora_entrega)+"| ")
            pe.write(str(item.fecha_creacion)+"\n")
            pe.close()

        pl = open("pl.txt","w")
        for item in listaplatos:
            pl.write(str(item.nombre)+"| ")
            pl.write(str(item.precio)+"\n")
            pl.close()


    elif(a=="d"):
        for item in listapedidos:
            if(item.fecha_creacion==datetime.today().date()):

