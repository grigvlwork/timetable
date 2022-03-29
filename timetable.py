# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timetable.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_timetable_view(object):
    def setupUi(self, timetable_view):
        timetable_view.setObjectName("timetable_view")
        timetable_view.resize(1800, 838)
        self.verticalLayout = QtWidgets.QVBoxLayout(timetable_view)
        self.verticalLayout.setObjectName("verticalLayout")
        self.timetable = QtWidgets.QTableView(timetable_view)
        self.timetable.setObjectName("timetable")
        self.verticalLayout.addWidget(self.timetable)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.out_to_excel = QtWidgets.QPushButton(timetable_view)
        self.out_to_excel.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pics/toExcel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.out_to_excel.setIcon(icon)
        self.out_to_excel.setIconSize(QtCore.QSize(50, 50))
        self.out_to_excel.setObjectName("out_to_excel")
        self.horizontalLayout.addWidget(self.out_to_excel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(timetable_view)
        QtCore.QMetaObject.connectSlotsByName(timetable_view)

    def retranslateUi(self, timetable_view):
        _translate = QtCore.QCoreApplication.translate
        timetable_view.setWindowTitle(_translate("timetable_view", "Просмотр табеля"))
        self.out_to_excel.setToolTip(_translate("timetable_view", "Передать в Excel"))