'''
Created on 15 janv. 2010

@author: thomas
'''
import unittest
from base.ServersPool import ServersPool

class Test(unittest.TestCase):


    def setUp(self):
        self.pool = ServersPool()
        self.pool.add('10.32.4.13', 22, 'test', 'test')
        self.pool.add('10.32.4.26', 22, 'test2', 'test2')


    def tearDown(self):
        pass


    def testMassEcho(self):
        self.assertEqual(self.pool.sendCommand('echo $USER'), ['test\n','test2\n'])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testMassEcho']
    unittest.main()