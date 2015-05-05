'''
Created on 4/5/2015

@author: personal
'''
import unittest
import BilleteraElectronica

class Test(unittest.TestCase):


    def testBilleteraExist(self):
        pass
    
    def testCrearBilletera(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704");
        saldo = Arleyn.saldo();
        self.assertEqual(0,saldo);
        
    def testAgregarCredito(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704");
        saldo = Arleyn.recargar(100,'27/12/1992','01');
        self.assertEqual(100,saldo);
        
    def testAgregarCredito2(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704");
        saldo = Arleyn.recargar(100,'27/12/1992','01');
        saldo1 = Arleyn.recargar(550,'27/12/1992','01');
        self.assertEqual(650,saldo1);