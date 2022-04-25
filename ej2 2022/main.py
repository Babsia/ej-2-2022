from menu import menuu
if __name__=='__main__':
    numeroV=input("ingrese el numero de viajero ")
    m=menuu()
    while(numeroV!='0'):
        print("seleccione una opcion")
        print("a.consultar millas")
        print("b.acumular millas")
        print("c.canjear millas")
        print("d.salir")
        op=input('')
        m.opcion(op,numeroV)
        numeroV=input("ingrese el numero de viajero ")