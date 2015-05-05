#-*- coding:UTF-8 -*-
import unittest
import BilleteraElectronica
from decimal import Decimal


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
        Arleyn.recargar(100,'27/12/1992','01');
        saldo = Arleyn.recargar(550,'27/12/1992','01');
        self.assertEqual(650,saldo);
        
    def testConsumirCredito(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704");
        Arleyn.recargar(100,'27/12/1992','01');
        saldo = Arleyn.consumir(50,'28/12/1992','02')
        self.assertEqual(50,saldo);
        
    def testConsumirCredito2(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704");
        Arleyn.recargar(100,'27/12/1992','01')
        Arleyn.consumir(50,'28/12/1992','02')
        saldo = Arleyn.consumir(45,'28/12/1992','02')
        self.assertEqual(5,saldo);
        
    def testSinSaldo(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704")
        self.assertRaises(Exception, lambda: Arleyn.consumir(50,'28/12/1992','02'))
        
    def testSaldoMenorConsumo(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704")
        Arleyn.recargar(100,'27/12/1992','01')
        self.assertRaises(Exception, lambda: Arleyn.consumir(150,'28/12/1992','02'))
        
    def testSaldoRecargaNegativa(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704")
        self.assertRaises(Exception, lambda: Arleyn.recargar(-150,'28/12/1992','02'))
        
    def testSaldoRecargaNegativa2(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704")
        Arleyn.recargar(100,'27/12/1992','01')
        self.assertRaises(Exception, lambda: Arleyn.recargar(-150,'28/12/1992','02'))
        
    def testSaldoConsumoNegativo(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704")
        self.assertRaises(Exception, lambda: Arleyn.consumir(-150,'28/12/1992','02'))
        
    def testSaldoConsumoNegativo2(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704")
        Arleyn.recargar(100,'27/12/1992','01')
        self.assertRaises(Exception, lambda: Arleyn.consumir(-50,'28/12/1992','02'))
        
    def testRecargar0(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704");
        self.assertRaises(Exception, lambda: Arleyn.recargar(0,'28/12/1992','02'))
        
    def testConsumir0(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704");
        self.assertRaises(Exception, lambda: Arleyn.consumir(0,'28/12/1992','02'))
        
    def testConsumir2(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704");
        Arleyn.recargar(100,'28/12/1992','02')
        self.assertRaises(Exception, lambda: Arleyn.consumir(0,'28/12/1992','02'))
        
    def testRecargarDecimales(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704");
        saldo = Arleyn.recargar(10.6,'28/12/1992','02')
        self.assertEqual(10.6,saldo);
        
    def testConsumirDecimales(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704");
        Arleyn.recargar(100,'28/12/1992','02')
        saldo = Arleyn.consumir(Decimal('99.9'),'28/12/1992','02')
        self.assertEqual(Decimal('0.1'),saldo);
        
    def testConsumirDecimales2(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704");
        Arleyn.recargar(100,'28/12/1992','02')
        saldo = Arleyn.consumir(Decimal(99.5),'28/12/1992','02')
        self.assertEqual(Decimal(0.5),saldo);
        
    def testRecargoConsumoExacto(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704");
        Arleyn.recargar(100,'28/12/1992','02')
        saldo = Arleyn.consumir(100,'28/12/1992','02')
        self.assertEqual(0,saldo);
        
        
# DEcimales
# Combo

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()