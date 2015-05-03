'''
Created on 3/5/2015

@author: Arleyn Goncalves
         Edwin Murillo
'''

class BilleteraElectronica(object):
    def __init__(self,identificador,nombre,apellido,CI):
        self._identificador = identificador;
        self._nombre = nombre;
        self._apellido = apellido;
        self._CI = CI;
        self._saldo = 0;
        
if __name__ == '__main__':
    pass