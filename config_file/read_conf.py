# -*- coding:utf-8 _*-
#!/usr/bin/python3

#   author : YOYO
#   time :  2020/3/4 21:40
#   email : youyou.xu@enesource.com
#   project_name :  test_read_mysql 
#   file_name :  read_conf.py
#   function： 读取 配置文件里的内容

import configparser
from common import contants


class ReadConf:
    def __init__(self):
        # 创建实例
        self.cf = configparser.ConfigParser()
        self.cf.read(contants.conf, encoding="utf-8")

    # 获取一般值
    def get_value(self, section, option):
        return self.cf.get(section, option)

    # 获取int值
    def get_int_value(self, section, option):
        return self.cf.getint(section, option)

    # 获取布尔值
    def get_boolean_value(self, section, option):
        return self.cf.getboolean(section, option)


if __name__ == "__main__":
    print(ReadConf().get_value("LOG", "log_format"))