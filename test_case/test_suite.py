# -*- coding:utf-8 _*-
#!/usr/bin/python3

#   author : YOYO
#   time :  2020/3/8 16:20
#   email : youyou.xu@enesource.com
#   project_name :  test_read_mysql 
#   file_name :  test_suite.py
#   function： 测试套件，执行测试用例

import unittest
from libnew import HTMLTestRunnerNew
from test_case.test_inOrUpElectricityPrice import TestinOrUpElectricityPrice
from common import contants
import datetime

suite = unittest.TestSuite()
loader = unittest.TestLoader()

suite.addTest(loader.loadTestsFromTestCase(TestinOrUpElectricityPrice))

report = contants.report_dir
test_time = datetime.date.today()

with open(report, "wb") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title=str(test_time) + "测试报告", tester="YOYO")

    runner.run(suite)


