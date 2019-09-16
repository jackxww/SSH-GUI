# -*- coding: utf-8 -*-
import os


class Utils_file():
    #教验ip地址是否合法
    def is_ipv4(ip: str) -> bool:
        """
        检查ip是否合法
        :param: ip ip地址
        :return: True 合法 False 不合法
        """
        return True if [1] * 4 == [x.isdigit() and 0 <= int(x) <= 255 for x in ip.split(".")] else False

    # 判断指定路径下面的文件夹是否存在， 不存在就创建
    def make_path(p):
        if os.path.exists(p) == False:  # 判断文件夹是否存在
            os.mkdir(p)  # 创建文件夹
