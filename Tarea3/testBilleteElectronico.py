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