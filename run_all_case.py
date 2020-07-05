import unittest
import os
#https://blog.csdn.net/weixin_41149418/article/details/90375899 将适配python2的HTMLTestRunner修改为适配python3
#http://tungwaiyip.info/software/HTMLTestRunner.html 下载地址，来自yoyo,
#用例路径
#case_path=os.path.join(os.getcwd(),"demo1")
case_path=os.path.join(os.path.dirname(os.path.realpath(__file__)),"demo1")

#报告路径
#eport_path=os.path.join(os.getcwd(),"report")
def all_case():
    discover=unittest.defaultTestLoader.discover(case_path,pattern="test*.py",top_level_dir=None)
    #print(discover)
    return discover
if __name__=="__main__":
    #runner=unittest.TextTestRunner()
    #runner.run(all_case())
    import HTMLTestRunner
    report_path = os.path.join(os.getcwd(), "demo1","report")
    report_abspath=os.path.join(report_path,"result.html")
    #print(report_abspath)
    fp=open(report_abspath,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"测试结果如下",description=u"用例执行情况：")
    runner.run(all_case())
    fp.close()