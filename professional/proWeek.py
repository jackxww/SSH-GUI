# -*- coding: utf-8 -*-
# 业务实现
import os

from PyQt5.QtCore import QStringListModel

from uipy.main import Ui_MainWindow
from util.utils_file import FileClass


class Pro_week():
    # 获取setting文件夹下面的所有的txt文件 然后进行调用
    def showHostList(self,ui:Ui_MainWindow):
        dirs = os.getcwd() + '/setting/'
        hostList = FileClass.getHostList(dirs)
        slm = QStringListModel()
        # 设置模型列表视图，加载数据列表
        slm.setStringList(hostList)
        ui.list_host.setModel(slm)
