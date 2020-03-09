# -*- coding:utf-8 _*-
#!/usr/bin/python3

#   author : YOYO
#   time :  2020/3/5 21:20
#   email : youyou.xu@enesource.com
#   project_name :  test_read_mysql 
#   file_name :  TestMethod.py
#   function： 微服务之添加电价方案测试用例自动化

import unittest
import json
import requests
import common.contants
from config_file.read_conf import ReadConf
from libnew.ddtnew import ddt, data
from test_data.do_excel import DoExcel

# 读取数据
case_data = common.contants.case_data
datas = DoExcel(case_data, "Sheet1").read_data()
# 获取测试环境URL和headers
conf = ReadConf()
dev_url = conf.get_value("URL", "url")
header = conf.get_value("HEAD", "headers")


@ddt
class TestMethod(unittest.TestCase):
    # 这个类可以实现所有的单个接口post请求，所有的参数通过data传递进来；
    # 只需要维护Excel表格的用例
    @data(*datas)
    def test_request(self, data):
        # 拼接URL字段
        url = dev_url + data.api
        # 如果data格式不对，就转化一下,变成字典
        if data.data is not None and type(data.data) == str:
            data.data = json.dumps(data.data)

            resp = requests.request(method="POST", url=url, headers=eval(header), data=data.data)
            # 请求成功的情况下进行断言
            if resp.status_code == 200:
                actual_data = resp.text
                try:
                    self.assertIn(data.expected, actual_data)
                    result = "PASS"
                except AssertionError as e:
                    result = "FAILED"
                    raise e
                finally:
                    DoExcel(case_data, "Sheet1").write_data(row=data.id+1, column=6, value=result)
            else:
                print("接口请求失败,用例执行错误")






