# -*- coding:utf-8 _*-
# !/usr/bin/python3

#   author : YOYO
#   time :  2020/3/4 21:19
#   email : youyou.xu@enesource.com
#   project_name :  ningmengban_API_test.git 
#   file_name :  contants.py
#   function： 规定各个文件的路径，可让其他地方直接引用


import os

# 项目根目录
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 配置文件路径
conf_dir = os.path.join(base_dir, "config_file")
conf = os.path.join(conf_dir, "conf.ini")

# 测试用例文件夹
test_data_dir = os.path.join(base_dir, "test_data")
case_data = os.path.join(test_data_dir, "testdata.xlsx")

# 测试报告路径
result_dir = os.path.join(base_dir, "test_result")
report_dir = os.path.join(result_dir, "test_report.html")



