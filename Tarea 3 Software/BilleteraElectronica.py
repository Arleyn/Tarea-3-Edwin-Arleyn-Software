'''
Created on 3/5/2015
@author: Arleyn Goncalves
         Edwin Murillo
'''

class DatosCreditos(object):
    def __init__(self):
        self._lista_recargas = [];
        
    def Almacenar(self,cantidad,fecha,identificar):
        self._listas_recargas.append((cantidad,fecha,identificar));
        

class DatosDebitos(object):
    def __init__(self):
        self._lista_consumos = [];
    
    def Almacenar(self,cantidad,fecha,identificar):
        self._listas_consumos.append((cantidad,fecha,identificar))
        
        
class BilleteraElectronica(object):
    def __init__(self,identificador,nombre,apellido,CI):
        self._identificador = identificador;
        self._nombre = nombre;
        self._apellido = apellido;
        self._CI = CI;
        self._saldo = 0;
        self._Consumo = DatosDebitos();
        self._Creditos = DatosCreditos();
                
    def saldo(self):
        print(self._saldo);
        
    def recargar(self,cantidad,):
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