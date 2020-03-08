# -*- coding:utf-8 _*-
#!/usr/bin/python3

#   author : YOYO
#   time :  2020/3/5 21:20
#   email : youyou.xu@enesource.com
#   project_name :  test_read_mysql 
#   file_name :  test_inOrUpElectricityPrice.py
#   function： 微服务之添加电价方案测试用例自动化

import json
import unittest
import common.contants
from libnew.ddtnew import ddt, data
from test_data.do_excel import DoExcel
from common.requestnew import Request

# 取出路径
# 获取测试用例
# 实例化repuest   之前是因为有多种请求方式的区别，现在实际只有post，看看是不是去掉这一步
# 获取测试环境URL
case_data = common.contants.case_data
datas = DoExcel(case_data, "Sheet1").read_data()


@ddt
class TestinOrUpElectricityPrice(unittest.TestCase):
    @data(*datas)
    def test_test(self,data):
        resp = Request().request(api_url=data.api, data=data.data)
        # 请求成功的情况下进行断言
        if resp.status_code == 200:
            actual_data = resp.text
            try:
                self.assertIn(data.expected, actual_data)
                result = "PASS"
            except AssertionError as e:
                result = "FAILED"
                print(e)
                raise e
            finally:
                DoExcel(case_data, "Sheet1").write_data(row=data.id+1, column=6, value=result)
        else:
            print("接口请求失败,用例执行错误")






