#coding=utf=8
import unittest
from selenium import webdriver
#import HTMLTestRunner  #http://tungwaiyip.info/software/HTMLTestRunner.html 下载地址，来自yoyo
from selenium.webdriver.support import expected_conditions as EC # 含16中判断元素的方法,通常定义locator和text
from selenium.webdriver.support.wait import WebDriverWait    #显示等待  WebDriverWait和expected_conditions配合使用
# from selenium.webdriver.common.by import By

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
    def test11(self):     #unittest的方法以"test"开头才会被执行
        print("test11")
        assert (2>1)
    def test13(self):
        print("test13")
        assert(2>0)
    def test12(self):
        print("test12")
        #在继承unittest的类中才可以使用self.assertEqual
class login1:
    def page(self):
        self.driver=webdriver.Chrome( )
        self.driver.get("http://www.baidu.com")
        locator1=("id","kw")
        text1=(r"百度一下")
        a=self.driver.title
        #WebDriverWait(self.driver,10).until(EC.presence_of_element_located(locator1))#会发现异常
        #result=EC.text_to_be_present_in_element(locator1,text1)(self.driver) #判断文本，返回true或false
        b=self.driver.current_url
        print(b)
        time.sleep(2)
        self.driver.quit()
        return a     #打印函数时会输出此值
        #print(help(unittest))
if __name__=="__main__":
    print("hello")
    # login1=login1()
    # login1.page()
    #
    unittest.main()

