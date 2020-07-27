# -*- coding:utf-8 _*-
# !/usr/bin/python3

#   author : YOYO
#   time :  2020/3/5 21:20
#   email : youyou.xu@enesource.com
#   project_name :  test_read_mysql 
#   file_name :  TestMethod.py
#   function： 测试类

import unittest
import re
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
header = conf.get_value("HEAD", "headers")
# 温州政府
wenzhou_gov_url = conf.get_value("URL", "wenzhou_gov_url")
# 温州企业
wenzhou_ent_url = conf.get_value("URL", "wenzhou_ent_url")
# 节度使2.0线上
governor_url = conf.get_value("URL", "governor_url")


@ddt
class TestMethod(unittest.TestCase):
    # 这个类可以实现所有的单个接口post请求，所有的参数通过data传递进来；
    # 只需要维护Excel表格的用例
    @data(*cases)
    def test_request(self, case):

        # 根据用例title的前缀判断是拼接哪个环境的per_url
        if re.match(r"wenzhou_gov*", case.title):
            url = wenzhou_gov_url + case.api
        elif re.match(r"wenzhou_ent*", case.title):
            url = wenzhou_ent_url + case.api
        elif re.match(r"governor*", case.title):
            url = governor_url + case.api

        # 如果data格式不对，就转化一下,变成字典,再变成json        # 这样太麻烦了，直接使用原本的数据就可以，json格式就相当于是字典形式的字符串
        # if case.data is not None and type(case.data) == str:
        #     # data = json.loads(case.data)
        #     # data = json.dumps(data)
        my_logger = DoLog()
        my_logger.info("------------------------------------------------------------")
        my_logger.info("正在执行第{}条用例，请求参数：{}".format(case.id, case.data))
        if case.method == "POST" or case.method == "post":
            pass
            resp = requests.request(method="POST", url=url, headers=eval(header), data=case.data.encode("utf-8"))
        elif case.method == "GET" or case.method == "get":  # get请求时，params好像不能传递str，必须要去掉引号才行
            resp = requests.request(method="GET", url=url, params=eval(case.data))
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
            raise e2
        finally:
            if result != None:
                my_logger.info("******执行完成，回写数据*****")
                DoExcel(case_data, "Sheet1").write_data(row=case.id+1, column=6, value=result)










