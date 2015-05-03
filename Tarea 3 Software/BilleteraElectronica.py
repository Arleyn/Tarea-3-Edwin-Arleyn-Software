'''
Created on 3/5/2015
@author: Arleyn Goncalves
         Edwin Murillo
'''

lista_recargas = [];
lista_consumos = [];

class DatosCreditos(object):
    def __init__(self,cantidad,fecha,identificador):
        self._cantidad = cantidad;
        self._fecha = fecha;
        self._identificador = identificador;

class DatosDebitos(object):
    def __init__(self,cantidad,fecha,identificador):
        self._cantidad = cantidad;
        self._fecha = fecha;
        self._identificador = identificador;
        
class BilleteraElectronica(object):
    def __init__(self,identificador,nombre,apellido,CI):
        self._identificador = identificador;
        self._nombre = nombre;
        self._apellido = apellido;
        self._CI = CI;
        self._saldo = 0;
        
    def saldo(self):
        print(self._saldo);
        
    def recargar(self,cantidad):
        if cantidad <= 0:
            raise Exception("La cantidad a recargar tiene que se mayor a 0");
        else:
            self._saldo += cantidad;
            return self._saldo;
        
    def consumir(self,cantidad):
        if self._saldo < cantidad:
            raise Exception("No tiene saldo suficiente");
        elif cantidad <= 0:
            raise Exception("La cantidad a consumir tiene que ser mayor a 0");
        else:
            self._saldo -= cantidad;
        
if __name__ == '__main__':
    pass