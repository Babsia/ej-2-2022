import os

from manejadorviajero import manejador

class menuu:
    __switcher=None
    __M=None

    def __init__(self):
        self.__switcher = { 
            'a':self.opcion1,
            'b':self.opcion2,
            'c':self.opcion3,
            'd':self.salir
            }
        self.__M=manejador()
        self.__M.CargarLista()

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op,num):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func(num)

    def salir(self,num):
        print('Salir')

    def opcion1(self,num):
        print("opcion a")
        print("la cantidad de millas del viajero es: {}".format (self.__M.consultarmillas(num)))
        

    def opcion2(self,num):
        print("opcion b")
        print("opcion b")
        millas=int(input("Ingrese La cantidad de millas para acumular "))
        print("la cantidad de millas del viajero es: {}".format (self.__M.acumular(num,millas)))
        
        pass
    def opcion3(self,num):
        print("opcion c")
        millasc=int(input("Ingrese La cantidad de millas para canjear "))
        print("la cantidad de millas del viajero es: {}".format (self.__M.canjear(num,millasc)))
        pass