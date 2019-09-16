# -*- coding: utf-8 -*-
import json
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget, QMainWindow, qApp, QFileDialog, QWidget, QListView

from mode.host_str import hostStr
from uipy.setting import Ui_Form
from util.utils import Utils_file
from util.utils_file import FileClass


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(640, 480)
        MainWindow.setFixedSize(640, 480)
        screen = QDesktopWidget().screenGeometry()
        size = MainWindow.geometry()
        MainWindow.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
        self.message = 'aaaa'
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(2, 147, 221, 427))
        self.treeView.setObjectName("treeView")
        self.btn_connction = QtWidgets.QPushButton(self.centralwidget)
        self.btn_connction.setEnabled(True)
        self.btn_connction.setGeometry(QtCore.QRect(2, 430, 100, 25))
        self.btn_connction.setObjectName("btn_connction")
        self.btn_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.btn_refresh.setEnabled(True)
        self.btn_refresh.setGeometry(QtCore.QRect(112, 430, 110, 25))
        self.btn_refresh.setObjectName("btn_refresh")
        self.up_file = QtWidgets.QLineEdit(self.centralwidget)
        self.up_file.setGeometry(QtCore.QRect(227, 2, 346, 30))
        self.up_file.setObjectName("up_file")
        self.btn_up = QtWidgets.QPushButton(self.centralwidget)
        self.btn_up.setEnabled(True)
        self.btn_up.setGeometry(QtCore.QRect(576, 2, 60, 30))
        self.btn_up.setObjectName("btn_up")
        self.treeView_2 = QtWidgets.QTreeView(self.centralwidget)
        self.treeView_2.setGeometry(QtCore.QRect(227, 36, 410, 192))
        self.treeView_2.setObjectName("treeView_2")
        self.text_u_msg = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_u_msg.setGeometry(QtCore.QRect(227, 232, 410, 196))
        self.text_u_msg.setObjectName("text_u_msg")
        self.up_progress = QtWidgets.QProgressBar(self.centralwidget)
        self.up_progress.setGeometry(QtCore.QRect(510, 432, 128, 23))
        self.up_progress.setProperty("value", 24)
        self.up_progress.setObjectName("up_progress")
        self.up_file_msg = QtWidgets.QLabel(self.centralwidget)
        self.up_file_msg.setGeometry(QtCore.QRect(231, 432, 275, 20))
        self.up_file_msg.setObjectName("up_file_msg")
        self.list_host = QtWidgets.QListView(self.centralwidget)
        self.list_host.setGeometry(QtCore.QRect(2, 2, 221, 140))
        self.list_host.setObjectName("list_host")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menuSSH = QtWidgets.QMenu(self.menubar)
        self.menuSSH.setObjectName("menuSSH")
        MainWindow.setMenuBar(self.menubar)
        self.setting = QtWidgets.QAction(MainWindow)
        self.setting.setObjectName("setting")
        self.setting.triggered.connect(lambda: self.showDialog())
        self.exit = QtWidgets.QAction(MainWindow)
        self.exit.setObjectName("exit")
        self.exit.triggered.connect(qApp.quit)

        # self.statusBar()
        self.menuSSH.addSeparator()
        self.menuSSH.addAction(self.setting)
        self.menuSSH.addAction(self.exit)
        self.menubar.addAction(self.menuSSH.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def showDialog(self):
        self.settingShow = QMainWindow()
        self.settingQWin = Ui_Form()
        self.settingQWin.setupUi(self.settingShow)
        self.settingShow.show()

        # 开始对设置的控件属性进行获取
        self.btn_cancel, self.btn_save, self.edit_account, \
        self.edit_pwd, self.edit_logaddress, self.edit_port, self.editUrl, self.openlog_btn = self.settingQWin.getSettingMsg()

        # 取消按钮的操作
        self.btn_cancel.clicked.connect(lambda: self.btnCancel())
        # 打开日志文件存放的地方
        self.openlog_btn.clicked.connect(lambda: self.openLogAddress())
        # 保存操作
        self.btn_save.clicked.connect(lambda: self.saveSetting())

    #打开日志文件存放的地方
    def openLogAddress(self):
        fileName1, filetype = QFileDialog.getOpenFileName(self,
                                                          "选取文件",
                                                          "./",
                                                          "All Files (*);;Text Files (*.txt)")
        self.edit_logaddress.setText(fileName1)
        print(fileName1,filetype)

    # 保存设置
    def saveSetting(self):
        # 获取IP地址
        self.ip = self.editUrl.text()
        # 端口号
        self.port = self.edit_port.text()
        # 账号
        self.account = self.edit_account.text()
        # 密码
        self.pwd = self.edit_pwd.text()

        # 判断ip地址是否合法
        if not Utils_file.is_ipv4(self.ip):
            QtWidgets.QMessageBox.information(self,
                                              "说明", "IP地址不合法！", QtWidgets.QMessageBox.Ok)
            return
        # 判断端口是数字
        if not self.port.isdigit():
            QtWidgets.QMessageBox.information(self,
                                              "说明", "端口号不合法！", QtWidgets.QMessageBox.Ok)
            return
        # 判断账号是否为空
        if self.account.__len__()==0:
            QtWidgets.QMessageBox.information(self,
                                              "说明", "账号不能为空！", QtWidgets.QMessageBox.Ok)
            return
        # 判断密码是否为空
        if self.pwd.__len__()==0:
            QtWidgets.QMessageBox.information(self,
                                              "说明", "密码不能为空！", QtWidgets.QMessageBox.Ok)
            return

        dirs = os.getcwd()+'/setting/'
        if not os.path.exists(dirs):
            os.makedirs(dirs)
        fileName = dirs+'/'+self.ip+'.txt'

        #将文件以json格式写入文本
        settingStr = hostStr().make_struct(self.ip, self.port, self.account, self.pwd).__dict__
        mySettingJson = json.dumps(settingStr)

        #先获取当前文件中有多少行数据
        # fileLine = FileClass.readLines(fileName)
        #开始写入文本
        wBool =  FileClass.file(0, fileName, mySettingJson)
        if not wBool:
            QtWidgets.QMessageBox.information(self,
                                              "说明", " 写入错误！", QtWidgets.QMessageBox.Ok)
            return
        #保存完毕之后  开始关闭
        self.btnCancel()

    #关闭FORM窗口
    def btnCancel(self):
        self.settingShow.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UpFile"))
        self.btn_connction.setText(_translate("MainWindow", "connection"))
        self.btn_refresh.setText(_translate("MainWindow", "refresh"))
        self.up_file.setPlaceholderText(_translate("MainWindow", "上传文件的路径"))
        self.btn_up.setText(_translate("MainWindow", "open"))
        self.up_file_msg.setText(_translate("MainWindow", self.message))
        self.menuSSH.setTitle(_translate("MainWindow", "SSH"))
        self.setting.setText(_translate("MainWindow", "setting"))
        self.setting.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.exit.setText(_translate("MainWindow", "exit"))
        self.exit.setShortcut(_translate("MainWindow", "Ctrl+Q"))

    # 开始显示查询到的值
    def showHostLists(self) -> QListView:
       return self.list_host