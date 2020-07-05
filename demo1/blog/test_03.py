#coding:utf=8
import unittest
from selenium import webdriver
#import HTMLTestRunner  #http://tungwaiyip.info/software/HTMLTestRunner.html 下载地址，来自yoyo
import time
class login(unittest.TestCase):
    @classmethod
    #def setUp(self):
        #print("start")
    def setUpClass(cls):
        print("start")
    @classmethod
    def tearDownClass(cls):
        print("end")
    #def tearDown(self):
        #print("end")
    def test31(self):     #unittest的方法以"test"开头才会被执行
        print("test31")
        assert (2>1)
    def test33(self):
        print("test33")
        assert(2>0)
    def test32(self):
        print("test32")
        #在继承unittest的类中才可以使用self.assertEqual

if __name__=="__main__":

    unittest.main()
