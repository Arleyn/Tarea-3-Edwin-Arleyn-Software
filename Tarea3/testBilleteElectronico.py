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
        
    def testConsumirCredito(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704");
        saldo = Arleyn.recargar(100,'27/12/1992','01');
        saldo1 = Arleyn.consumir(50,'28/12/1992','02')
        self.assertEqual(50,saldo1);
        
    def testConsumirCredito2(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704");
        saldo = Arleyn.recargar(100,'27/12/1992','01');
        saldo1 = Arleyn.consumir(50,'28/12/1992','02')
        saldo2 = Arleyn.consumir(45,'28/12/1992','02')
        self.assertEqual(5,saldo2);
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()