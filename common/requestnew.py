# -*- coding:utf-8 _*-
#!/usr/bin/python3

#   author : YOYO
#   time :  2020/3/8 14:17
#   email : youyou.xu@enesource.com
#   project_name :  test_read_mysql 
#   file_name :  requestnew.py
#   function： 封装request类，完成读取测试环境URL，请求方式和请求头以及处理request的返回数据问题

from config_file.read_conf import ReadConf
import requests
import json

# 获取配置文件里的数据
conf = ReadConf()
dev_url = conf.get_value("URL", "url")
header = conf.get_value("HEAD", "headers")


class Request:
    def __init__(self):
        self.method = "POST"
        # 实例化session
        # self.session = requests.sessions.session()

    def request(self,api_url, data):
        # 拼接成完整的URL
        url = dev_url + api_url
        #如果data格式不对，就转化一下
        if data is not None and type(data) == str:
            data = json.dumps(data)
        try:
            resp = requests.request(method=self.method, url=url, json=data, headers=eval(header)) #headers是字典格式，从配置文件里取出来都是字符串，所以要转化一下
            return resp
        except Exception as e:
            print(e)



if __name__ == "__main__":
    r = Request()
    resp = r.request("/workflow/user/queryUser",data={"userId":"${userId_bm_1}"})
    print(resp.json())
    print(resp.text)
    print(type(resp.text))
