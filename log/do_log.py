# -*- coding:utf-8 _*-
# !/usr/bin/python3

#   author : YOYO
#   time :  2020/3/9 21:17
#   email : youyou.xu@enesource.com
#   project_name :  test_read_mysql 
#   file_name :  do_log.py
#   function： 创建日志收集系统

import logging
from config_file.read_conf import ReadConf
import datetime


time = datetime.date.today()
# 获取配置文件里关于日志的数据
conf = ReadConf()
name = conf.get_value("LOG", "name")
in_level = conf.get_value("LOG", "in_level")
out_level = conf.get_value("LOG", "out_level")
out_file_level = conf.get_value("LOG", "out_file_level")
file_path = conf.get_value("LOG", "file_path") + name + str(time) + '.txt'
log_format = conf.get_value("LOG", "log_format")


class DoLog:

    def mylog(self, level, msg):
        # 创建一个日志收集器
        my_logger = logging.getLogger(name)
        # 给日志收集器指定收集级别
        my_logger.setLevel(in_level)
        # 设置输出格式
        formatter = logging.Formatter(log_format)
        # 输出渠道
        fh = logging.FileHandler(file_path, mode='a', encoding="utf-8")
        # 输出级别
        fh.setLevel(out_file_level)
        # 设置日志输出格式
        fh.setFormatter(formatter)
        # 对接
        my_logger.addHandler(fh)

        if level == "DEBUG":
            my_logger.debug(msg)
        elif level == "INFO":
            my_logger.info(msg)
        elif level == "ERROR":
            my_logger.error(msg)
        elif level == "WARNING":
            my_logger.warning(msg)
        else:
            my_logger.critical(msg)
        # 移除日志收集器
        my_logger.removeHandler(fh)

    def debug(self, msg):
        self.mylog("DEBUG", msg)

    def info(self, msg):
        self.mylog("INFO", msg)

    def error(self, msg):
        self.mylog("ERROR", msg)

    def warning(self, msg):
        self.mylog("WARNING", msg)

    def critical(self, msg):
        self.mylog("CRITICAL", msg)


if __name__ == "__main__":
    my_logger = DoLog()
    my_logger.debug("test日志信息")