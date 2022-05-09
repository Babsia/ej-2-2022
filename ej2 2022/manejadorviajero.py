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
        i = 0
        while (i < len(self.__lista) and self.__lista[i].getnum() != num):
            i += 1
        if i == len(self.__lista):
            i = -1
        return i
    def consultarmillas(self,num):
        i=self.buscar(num)
        valor=None
        if i != -1:
           valor=self.__lista[i].getmillas() 
        return valor
    def acumular(self,num,millas):
        return self.__lista[self.buscar(num)].acumularmillas(millas)
    def canjear(self,num,millasc):
        return self.__lista[self.buscar(num)].canje(millasc)
        
