# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1342, 795)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(MainWindow)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.userlabel = QtWidgets.QLabel(MainWindow)
        self.userlabel.setMinimumSize(QtCore.QSize(50, 50))
        self.userlabel.setMaximumSize(QtCore.QSize(50, 50))
        self.userlabel.setText("")
        self.userlabel.setObjectName("userlabel")
        self.horizontalLayout_2.addWidget(self.userlabel)
        self.username = QtWidgets.QLabel(MainWindow)
        self.username.setMinimumSize(QtCore.QSize(100, 0))
        self.username.setObjectName("username")
        self.horizontalLayout_2.addWidget(self.username)
        self.logout = QtWidgets.QPushButton(MainWindow)
        self.logout.setMinimumSize(QtCore.QSize(40, 40))
        self.logout.setMaximumSize(QtCore.QSize(40, 40))
        self.logout.setText("")
        self.logout.setObjectName("logout")
        self.horizontalLayout_2.addWidget(self.logout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(5, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.sendmail = QtWidgets.QPushButton(MainWindow)
        self.sendmail.setMinimumSize(QtCore.QSize(120, 35))
        self.sendmail.setMaximumSize(QtCore.QSize(120, 35))
        self.sendmail.setObjectName("sendmail")
        self.verticalLayout_2.addWidget(self.sendmail, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.normal = QtWidgets.QPushButton(MainWindow)
        self.normal.setMinimumSize(QtCore.QSize(120, 35))
        self.normal.setMaximumSize(QtCore.QSize(120, 35))
        self.normal.setObjectName("normal")
        self.verticalLayout_2.addWidget(self.normal, 0, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.trash = QtWidgets.QPushButton(MainWindow)
        self.trash.setMinimumSize(QtCore.QSize(120, 35))
        self.trash.setMaximumSize(QtCore.QSize(120, 35))
        self.trash.setObjectName("trash")
        self.verticalLayout_2.addWidget(self.trash, 0, QtCore.Qt.AlignHCenter)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem3)
        self.checkblacklist = QtWidgets.QPushButton(MainWindow)
        self.checkblacklist.setMinimumSize(QtCore.QSize(120, 35))
        self.checkblacklist.setMaximumSize(QtCore.QSize(120, 35))
        self.checkblacklist.setObjectName("checkblacklist")
        self.verticalLayout_2.addWidget(self.checkblacklist, 0, QtCore.Qt.AlignHCenter)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem4)
        self.checkwhitelist = QtWidgets.QPushButton(MainWindow)
        self.checkwhitelist.setMinimumSize(QtCore.QSize(120, 35))
        self.checkwhitelist.setMaximumSize(QtCore.QSize(120, 35))
        self.checkwhitelist.setObjectName("checkwhitelist")
        self.verticalLayout_2.addWidget(self.checkwhitelist, 0, QtCore.Qt.AlignHCenter)
        spacerItem5 = QtWidgets.QSpacerItem(20, 300, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.checkmail = QtWidgets.QPushButton(MainWindow)
        self.checkmail.setMinimumSize(QtCore.QSize(120, 35))
        self.checkmail.setMaximumSize(QtCore.QSize(120, 35))
        self.checkmail.setObjectName("checkmail")
        self.horizontalLayout_9.addWidget(self.checkmail)
        self.moveto = QtWidgets.QPushButton(MainWindow)
        self.moveto.setMinimumSize(QtCore.QSize(120, 35))
        self.moveto.setMaximumSize(QtCore.QSize(120, 35))
        self.moveto.setObjectName("moveto")
        self.horizontalLayout_9.addWidget(self.moveto)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.blacklist = QtWidgets.QLineEdit(MainWindow)
        self.blacklist.setMinimumSize(QtCore.QSize(175, 30))
        self.blacklist.setMaximumSize(QtCore.QSize(175, 30))
        self.blacklist.setObjectName("blacklist")
        self.horizontalLayout_4.addWidget(self.blacklist)
        self.blackconfirm = QtWidgets.QPushButton(MainWindow)
        self.blackconfirm.setMinimumSize(QtCore.QSize(65, 30))
        self.blackconfirm.setMaximumSize(QtCore.QSize(65, 30))
        self.blackconfirm.setObjectName("blackconfirm")
        self.horizontalLayout_4.addWidget(self.blackconfirm)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.whitelist = QtWidgets.QLineEdit(MainWindow)
        self.whitelist.setMinimumSize(QtCore.QSize(175, 30))
        self.whitelist.setMaximumSize(QtCore.QSize(175, 30))
        self.whitelist.setObjectName("whitelist")
        self.horizontalLayout_3.addWidget(self.whitelist)
        self.whiteconfirm = QtWidgets.QPushButton(MainWindow)
        self.whiteconfirm.setMinimumSize(QtCore.QSize(65, 30))
        self.whiteconfirm.setMaximumSize(QtCore.QSize(65, 30))
        self.whiteconfirm.setObjectName("whiteconfirm")
        self.horizontalLayout_3.addWidget(self.whiteconfirm)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem6 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem6)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem7 = QtWidgets.QSpacerItem(20, 3, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem7)
        self.mailList = QtWidgets.QListWidget(MainWindow)
        self.mailList.setMinimumSize(QtCore.QSize(230, 500))
        self.mailList.setObjectName("mailList")
        self.verticalLayout.addWidget(self.mailList)
        spacerItem8 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem8)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_5.addLayout(self.horizontalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkmailwidget = QtWidgets.QWidget(MainWindow)
        self.checkmailwidget.setMinimumSize(QtCore.QSize(826, 775))
        self.checkmailwidget.setObjectName("checkmailwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.checkmailwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.titlelabel = QtWidgets.QLabel(self.checkmailwidget)
        self.titlelabel.setMinimumSize(QtCore.QSize(50, 30))
        self.titlelabel.setMaximumSize(QtCore.QSize(50, 30))
        self.titlelabel.setObjectName("titlelabel")
        self.horizontalLayout_7.addWidget(self.titlelabel)
        self.title = QtWidgets.QLabel(self.checkmailwidget)
        self.title.setMinimumSize(QtCore.QSize(750, 30))
        self.title.setMaximumSize(QtCore.QSize(16777215, 30))
        self.title.setText("")
        self.title.setObjectName("title")
        self.horizontalLayout_7.addWidget(self.title)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.senderlabel = QtWidgets.QLabel(self.checkmailwidget)
        self.senderlabel.setMinimumSize(QtCore.QSize(50, 30))
        self.senderlabel.setMaximumSize(QtCore.QSize(50, 30))
        self.senderlabel.setObjectName("senderlabel")
        self.horizontalLayout_6.addWidget(self.senderlabel)
        self.senderName = QtWidgets.QLabel(self.checkmailwidget)
        self.senderName.setMinimumSize(QtCore.QSize(750, 30))
        self.senderName.setMaximumSize(QtCore.QSize(16777215, 30))
        self.senderName.setText("")
        self.senderName.setObjectName("senderName")
        self.horizontalLayout_6.addWidget(self.senderName)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.content = QtWidgets.QTextBrowser(self.checkmailwidget)
        self.content.setEnabled(True)
        self.content.setMinimumSize(QtCore.QSize(750, 400))
        self.content.setObjectName("content")
        self.verticalLayout_4.addWidget(self.content)
        self.verticalLayout_3.addWidget(self.checkmailwidget)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.username.setText(_translate("MainWindow", "用户名XXXXX"))
        self.logout.setToolTip(_translate("MainWindow", "注销"))
        self.sendmail.setText(_translate("MainWindow", "写信"))
        self.normal.setText(_translate("MainWindow", "收件箱"))
        self.trash.setText(_translate("MainWindow", "垃圾箱"))
        self.checkblacklist.setText(_translate("MainWindow", "黑名单列表"))
        self.checkwhitelist.setText(_translate("MainWindow", "白名单列表"))
        self.checkmail.setText(_translate("MainWindow", "查看"))
        self.moveto.setText(_translate("MainWindow", "移至垃圾箱"))
        self.blacklist.setPlaceholderText(_translate("MainWindow", "添加黑名单"))
        self.blackconfirm.setText(_translate("MainWindow", "添加"))
        self.whitelist.setPlaceholderText(_translate("MainWindow", "添加白名单"))
        self.whiteconfirm.setText(_translate("MainWindow", "添加"))
        self.titlelabel.setText(_translate("MainWindow", "主题："))
        self.senderlabel.setText(_translate("MainWindow", "发件人："))
        self.content.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9.26733pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9.26733pt;\"><br /></p></body></html>"))
