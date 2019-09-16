# -*- coding: utf-8 -*-
# jack_xie
# 一个文件上传的工具

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from professional.proWeek import Pro_week
from uipy.main import Ui_MainWindow

def main() -> Ui_MainWindow:
    MainWindow = QMainWindow()
    uiMains = Ui_MainWindow()
    uiMains.setupUi(MainWindow)
    MainWindow.show()
    return uiMains



if __name__ == '__main__':
    app = QApplication(sys.argv)
    uimain = main()
    Pro_week().showHostList(uimain)
    sys.exit(app.exec_())
    # sshClientCMd('1.32.255.214', 22, 'root', 'jyb-2018', 'ls /home/local/fhyl')
