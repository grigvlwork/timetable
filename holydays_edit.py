# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'holydays_edit.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_holydays_form(object):
    def setupUi(self, holydays_form):
        holydays_form.setObjectName("holydays_form")
        holydays_form.resize(251, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(holydays_form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.holyday = QtWidgets.QDateEdit(holydays_form)
        self.holyday.setObjectName("holyday")
        self.horizontalLayout.addWidget(self.holyday)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.add_button = QtWidgets.QPushButton(holydays_form)
        self.add_button.setEnabled(True)
        self.add_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pics/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_button.setIcon(icon)
        self.add_button.setObjectName("add_button")
        self.horizontalLayout.addWidget(self.add_button)
        self.edit_button = QtWidgets.QPushButton(holydays_form)
        self.edit_button.setEnabled(True)
        self.edit_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pics/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_button.setIcon(icon1)
        self.edit_button.setObjectName("edit_button")
        self.horizontalLayout.addWidget(self.edit_button)
        self.save_button = QtWidgets.QPushButton(holydays_form)
        self.save_button.setEnabled(False)
        self.save_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("pics/ok.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_button.setIcon(icon2)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout.addWidget(self.save_button)
        self.del_button = QtWidgets.QPushButton(holydays_form)
        self.del_button.setEnabled(True)
        self.del_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("pics/del.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.del_button.setIcon(icon3)
        self.del_button.setObjectName("del_button")
        self.horizontalLayout.addWidget(self.del_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.holydays_list = QtWidgets.QListView(holydays_form)
        self.holydays_list.setObjectName("holydays_list")
        self.verticalLayout.addWidget(self.holydays_list)

        self.retranslateUi(holydays_form)
        QtCore.QMetaObject.connectSlotsByName(holydays_form)

    def retranslateUi(self, holydays_form):
        _translate = QtCore.QCoreApplication.translate
        holydays_form.setWindowTitle(_translate("holydays_form", "Праздничные дни"))