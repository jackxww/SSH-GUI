# -*- coding: utf-8 -*-
# 文件操作
import os


class FileClass():
    # 获取setting文件夹下面的所有的txt文件
    def getHostList(path: str) -> []:
        files = os.listdir(path)
        return files


    #读取指定文件有多少行数据
    def readLines(address: str) -> int:
        count = 0
        thefile = open(address, 'r')
        while True:
            buffer = thefile.read(1024 * 8192)
            if not buffer:
                break
            count += buffer.count('\n')
        thefile.close()
        return count


    def file(line: int, address: str, message: str) -> bool:
        #判断文件是否存在， 不存在就创建一个
        my_open = open(address, 'w')
        # 在文件中写入一个字符串
        my_open.write(message)
        my_open.close()

        #检查是否正确写入
        my_open = open(address, 'r')
        my_infor = my_open.readlines()
        my_open.close()
        if my_infor[line] == message:
            return True
        else:
            return False