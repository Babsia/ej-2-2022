import csv
import re
from Viajerofrecuente import viajeroFrecuente
class manejador:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def CargarLista(self):
        archivo=open('viajeros.csv')
        reader=csv.reader(archivo,delimiter=',')
        for fila in reader:
            viajero=viajeroFrecuente(fila[0],fila[1],fila[2],fila[3],int(fila[4]))
            self.__lista.append(viajero)
    def buscar(self,num):
        for i in range(len(self.__lista)):
            if (self.__lista[i].getnum()==num):
                return self.__lista[i]
    def consultarmillas(self,num):
        return self.buscar(num).getmillas()
    def acumular(self,num,millas):
        return self.buscar(num).acumularmillas(millas)
    def canjear(self,num,millasc):
        return self.buscar(num).canje(millasc)
        
