# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'work_weekends_edit.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_work_weekends_form(object):
    def setupUi(self, work_weekends_form):
        work_weekends_form.setObjectName("work_weekends_form")
        work_weekends_form.resize(244, 279)
        self.verticalLayout = QtWidgets.QVBoxLayout(work_weekends_form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(work_weekends_form)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.work_weekend = QtWidgets.QDateEdit(work_weekends_form)
        self.work_weekend.setEnabled(False)
        self.work_weekend.setObjectName("work_weekend")
        self.horizontalLayout_2.addWidget(self.work_weekend)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(work_weekends_form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.day_of_week = QtWidgets.QComboBox(work_weekends_form)
        self.day_of_week.setEnabled(False)
        self.day_of_week.setObjectName("day_of_week")
        self.horizontalLayout_3.addWidget(self.day_of_week)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_button = QtWidgets.QPushButton(work_weekends_form)
        self.add_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pics/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_button.setIcon(icon)
        self.add_button.setObjectName("add_button")
        self.horizontalLayout.addWidget(self.add_button)
        self.edit_button = QtWidgets.QPushButton(work_weekends_form)
        self.edit_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pics/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_button.setIcon(icon1)
        self.edit_button.setObjectName("edit_button")
        self.horizontalLayout.addWidget(self.edit_button)
        self.save_button = QtWidgets.QPushButton(work_weekends_form)
        self.save_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("pics/ok.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_button.setIcon(icon2)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout.addWidget(self.save_button)
        self.del_button = QtWidgets.QPushButton(work_weekends_form)
        self.del_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("pics/del.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.del_button.setIcon(icon3)
        self.del_button.setObjectName("del_button")
        self.horizontalLayout.addWidget(self.del_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.work_days_list = QtWidgets.QListView(work_weekends_form)
        self.work_days_list.setObjectName("work_days_list")
        self.verticalLayout.addWidget(self.work_days_list)

        self.retranslateUi(work_weekends_form)
        QtCore.QMetaObject.connectSlotsByName(work_weekends_form)

    def retranslateUi(self, work_weekends_form):
        _translate = QtCore.QCoreApplication.translate
        work_weekends_form.setWindowTitle(_translate("work_weekends_form", "Рабочие выходные"))
        self.label.setText(_translate("work_weekends_form", "Рабочий выходной"))
        self.label_2.setText(_translate("work_weekends_form", "За какой день недели"))