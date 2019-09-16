# -*- coding: utf-8 -*-
# 信息结构体，包括解析json

class hostStr(object):
    class Struct(object):
        def __init__(self, ip: str, port: int, account: str, pwd: str):
            self.ip = ip
            self.port = port
            self.account = account
            self.pwd = pwd

    def make_struct(self, ip: str, port: int, account: str, pwd: str):
        return self.Struct(ip, port, account, pwd)

    # json解析
    def analyzeJson(self, json: str):
        decodedjson = json.loads(json)
        print(decodedjson)