# -*- coding:utf-8 _*-
#!/usr/bin/python3

#   author : YOYO
#   time :  2020/3/5 21:20
#   email : youyou.xu@enesource.com
#   project_name :  test_read_mysql 
#   file_name :  TestMethod.py
#   function： 测试类

import unittest
import json
import requests
import common.contants
from config_file.read_conf import ReadConf
from libnew.ddtnew import ddt, data
from test_data.do_excel import DoExcel
from log.do_log import DoLog

# 读取数据
case_data = common.contants.case_data
cases = DoExcel(case_data, "Sheet1").read_data()

# 获取测试环境URL和headers
conf = ReadConf()
per_url = conf.get_value("URL", "wenzhou_url")
header = conf.get_value("HEAD", "headers")


@ddt
class TestMethod(unittest.TestCase):
    # 这个类可以实现所有的单个接口post请求，所有的参数通过data传递进来；
    # 只需要维护Excel表格的用例
    @data(*cases)
    def test_request(self, case):
        # 拼接URL字段
        url = per_url + case.api
        # 如果data格式不对，就转化一下,变成字典,再变成json        # 这样太麻烦了，直接使用原本的数据就可以，json格式就相当于是字典形式的字符串
        # if case.data is not None and type(case.data) == str:
        #     # data = json.loads(case.data)
        #     # data = json.dumps(data)
        my_logger = DoLog()
        my_logger.info("*********************")
        my_logger.info("正在执行第{}条用例，请求参数：{}".format(case.id, case.data))
        resp = requests.request(method="POST", url=url, headers=eval(header), data=case.data)
        # 请求成功的情况下进行断言
        # if resp.status_code == 200:
        #     actual_data = resp.text
        try:
            actual_data = resp.text

            self.assertIn(case.expected, actual_data)
            result = "PASS"
        except AssertionError as e1:
            my_logger.error(e1)
            result = "FAILED"
            print("用例执行失败")
            raise e1
        except Exception as e2:
            print("请求状态：{}".format(resp.status_code))
            print("接口请求失败")
            my_logger.error("执行失败\n 错误信息：{}".format(e2))
        finally:
            my_logger.info("******回写数据*****")
            DoExcel(case_data, "Sheet1").write_data(row=case.id+1, column=6, value=result)










