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
        MainWindow.resize(987, 675)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(MainWindow)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.username = QtWidgets.QLabel(MainWindow)
        self.username.setMinimumSize(QtCore.QSize(200, 0))
        self.username.setObjectName("username")
        self.horizontalLayout_2.addWidget(self.username)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.logout = QtWidgets.QPushButton(MainWindow)
        self.logout.setMinimumSize(QtCore.QSize(100, 28))
        self.logout.setMaximumSize(QtCore.QSize(100, 28))
        self.logout.setObjectName("logout")
        self.horizontalLayout_2.addWidget(self.logout)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(5, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.sendmail = QtWidgets.QPushButton(MainWindow)
        self.sendmail.setMinimumSize(QtCore.QSize(100, 28))
        self.sendmail.setMaximumSize(QtCore.QSize(100, 28))
        self.sendmail.setObjectName("sendmail")
        self.verticalLayout_2.addWidget(self.sendmail, 0, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.normal = QtWidgets.QPushButton(MainWindow)
        self.normal.setMinimumSize(QtCore.QSize(100, 28))
        self.normal.setObjectName("normal")
        self.verticalLayout_2.addWidget(self.normal, 0, QtCore.Qt.AlignHCenter)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem3)
        self.trash = QtWidgets.QPushButton(MainWindow)
        self.trash.setMinimumSize(QtCore.QSize(100, 28))
        self.trash.setObjectName("trash")
        self.verticalLayout_2.addWidget(self.trash, 0, QtCore.Qt.AlignHCenter)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem4)
        self.checkblacklist = QtWidgets.QPushButton(MainWindow)
        self.checkblacklist.setMinimumSize(QtCore.QSize(100, 28))
        self.checkblacklist.setObjectName("checkblacklist")
        self.verticalLayout_2.addWidget(self.checkblacklist, 0, QtCore.Qt.AlignHCenter)
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem5)
        self.checkwhitelist = QtWidgets.QPushButton(MainWindow)
        self.checkwhitelist.setMinimumSize(QtCore.QSize(100, 28))
        self.checkwhitelist.setMaximumSize(QtCore.QSize(100, 28))
        self.checkwhitelist.setObjectName("checkwhitelist")
        self.verticalLayout_2.addWidget(self.checkwhitelist, 0, QtCore.Qt.AlignHCenter)
        spacerItem6 = QtWidgets.QSpacerItem(20, 300, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.blacklist = QtWidgets.QLineEdit(MainWindow)
        self.blacklist.setMinimumSize(QtCore.QSize(159, 25))
        self.blacklist.setMaximumSize(QtCore.QSize(159, 25))
        self.blacklist.setObjectName("blacklist")
        self.horizontalLayout_4.addWidget(self.blacklist)
        self.blackconfirm = QtWidgets.QPushButton(MainWindow)
        self.blackconfirm.setMinimumSize(QtCore.QSize(40, 25))
        self.blackconfirm.setMaximumSize(QtCore.QSize(40, 25))
        self.blackconfirm.setObjectName("blackconfirm")
        self.horizontalLayout_4.addWidget(self.blackconfirm)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.whitelist = QtWidgets.QLineEdit(MainWindow)
        self.whitelist.setMinimumSize(QtCore.QSize(159, 25))
        self.whitelist.setMaximumSize(QtCore.QSize(159, 25))
        self.whitelist.setObjectName("whitelist")
        self.horizontalLayout_3.addWidget(self.whitelist)
        self.whiteconfirm = QtWidgets.QPushButton(MainWindow)
        self.whiteconfirm.setMinimumSize(QtCore.QSize(40, 25))
        self.whiteconfirm.setMaximumSize(QtCore.QSize(40, 25))
        self.whiteconfirm.setObjectName("whiteconfirm")
        self.horizontalLayout_3.addWidget(self.whiteconfirm)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem7 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem7)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.mailList = QtWidgets.QListWidget(MainWindow)
        self.mailList.setMinimumSize(QtCore.QSize(750, 500))
        self.mailList.setObjectName("mailList")
        self.verticalLayout.addWidget(self.mailList)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.moveto = QtWidgets.QPushButton(MainWindow)
        self.moveto.setMinimumSize(QtCore.QSize(100, 28))
        self.moveto.setMaximumSize(QtCore.QSize(100, 28))
        self.moveto.setObjectName("movetotrash")
        self.horizontalLayout_5.addWidget(self.moveto, 0, QtCore.Qt.AlignRight)
        self.checkmail = QtWidgets.QPushButton(MainWindow)
        self.checkmail.setMinimumSize(QtCore.QSize(100, 28))
        self.checkmail.setMaximumSize(QtCore.QSize(100, 28))
        self.checkmail.setObjectName("checkmail")
        self.horizontalLayout_5.addWidget(self.checkmail, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem10 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem10)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.username.setText(_translate("MainWindow", "用户名XXXXX"))
        self.logout.setText(_translate("MainWindow", "退出"))
        self.sendmail.setText(_translate("MainWindow", "写信"))
        self.normal.setText(_translate("MainWindow", "收件箱"))
        self.trash.setText(_translate("MainWindow", "垃圾箱"))
        self.checkblacklist.setText(_translate("MainWindow", "黑名单列表"))
        self.checkwhitelist.setText(_translate("MainWindow", "白名单列表"))
        self.blacklist.setPlaceholderText(_translate("MainWindow", "添加黑名单"))
        self.blackconfirm.setText(_translate("MainWindow", "添加"))
        self.whitelist.setPlaceholderText(_translate("MainWindow", "添加白名单"))
        self.whiteconfirm.setText(_translate("MainWindow", "添加"))
        self.moveto.setText(_translate("MainWindow", "移至垃圾箱"))
        self.checkmail.setText(_translate("MainWindow", "查看"))
