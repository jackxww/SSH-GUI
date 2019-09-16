# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, qApp


class Ui_Form(QMainWindow):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(521, 350)
        Form.setFixedSize(521, 350)
        screen = QDesktopWidget().screenGeometry()
        size = Form.geometry()
        Form.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
        font = QtGui.QFont()
        font.setPointSize(12)
        Form.setFont(font)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(200, 40, 30, 30))
        self.label.setObjectName("label")
        self.editUrl = QtWidgets.QLineEdit(Form)
        self.editUrl.setGeometry(QtCore.QRect(240, 40, 110, 30))
        self.editUrl.setTabletTracking(False)
        self.editUrl.setText("")
        self.editUrl.setObjectName("editUrl")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(190, 80, 40, 30))
        self.label_2.setObjectName("label_2")
        self.edit_port = QtWidgets.QLineEdit(Form)
        self.edit_port.setGeometry(QtCore.QRect(240, 80, 110, 30))
        self.edit_port.setText("")
        self.edit_port.setObjectName("edit_port")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(22, 220, 106, 30))
        self.label_3.setObjectName("label_3")
        self.edit_logaddress = QtWidgets.QLineEdit(Form)
        self.edit_logaddress.setGeometry(QtCore.QRect(132, 220, 290, 30))
        self.edit_logaddress.setText("")
        self.edit_logaddress.setObjectName("edit_logaddress")
        self.openlog_btn = QtWidgets.QPushButton(Form)
        self.openlog_btn.setGeometry(QtCore.QRect(430, 220, 71, 30))
        self.openlog_btn.setObjectName("openlog_btn")
        self.btn_cancel = QtWidgets.QPushButton(Form)
        self.btn_cancel.setGeometry(QtCore.QRect(310, 280, 89, 30))
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_save = QtWidgets.QPushButton(Form)
        self.btn_save.setGeometry(QtCore.QRect(410, 280, 89, 30))
        self.btn_save.setObjectName("btn_save")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(160, 120, 70, 30))
        self.label_4.setObjectName("label_4")
        self.edit_account = QtWidgets.QLineEdit(Form)
        self.edit_account.setGeometry(QtCore.QRect(240, 120, 110, 30))
        self.edit_account.setText("")
        self.edit_account.setObjectName("edit_account")
        self.edit_pwd = QtWidgets.QLineEdit(Form)
        self.edit_pwd.setGeometry(QtCore.QRect(240, 160, 110, 30))
        self.edit_pwd.setText("")
        self.edit_pwd.setMaxLength(32766)
        self.edit_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edit_pwd.setObjectName("edit_pwd")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(160, 160, 70, 30))
        self.label_5.setObjectName("label_5")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "设置"))
        self.label.setText(_translate("Form", "url"))
        self.editUrl.setPlaceholderText(_translate("Form", "请输入ip地址"))
        self.label_2.setText(_translate("Form", "port"))
        self.edit_port.setPlaceholderText(_translate("Form", "请输入端口号"))
        self.label_3.setText(_translate("Form", "设置文件存放地址:"))
        self.edit_logaddress.setPlaceholderText(_translate("Form", "请输入设置文件存放地址"))
        self.openlog_btn.setText(_translate("Form", "open"))
        self.btn_cancel.setText(_translate("Form", "取消"))
        self.btn_save.setText(_translate("Form", "确定"))
        self.label_4.setText(_translate("Form", "  account"))
        self.edit_account.setPlaceholderText(_translate("Form", "请输入账号"))
        self.edit_pwd.setPlaceholderText(_translate("Form", "请输入密码"))
        self.label_5.setText(_translate("Form", "password"))
        # 取消按钮的操作
        # self.btn_cancel.clicked.connect(lambda :self.btnCancel())

    # 获取setting页面的所有的控件组件信息
    def getSettingMsg(self):
        return self.btn_cancel, self.btn_save, self.edit_account, \
               self.edit_pwd, self.edit_logaddress, self.edit_port, self.editUrl, self.openlog_btn