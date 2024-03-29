# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'workload.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_workload_dialog(object):
    def setupUi(self, workload_dialog):
        workload_dialog.setObjectName("workload_dialog")
        workload_dialog.resize(615, 438)
        self.verticalLayout = QtWidgets.QVBoxLayout(workload_dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.teachers_list = QtWidgets.QTableView(workload_dialog)
        self.teachers_list.setObjectName("teachers_list")
        self.verticalLayout.addWidget(self.teachers_list)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_teacher = QtWidgets.QPushButton(workload_dialog)
        self.add_teacher.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pics/addteacher.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_teacher.setIcon(icon)
        self.add_teacher.setObjectName("add_teacher")
        self.horizontalLayout.addWidget(self.add_teacher)
        self.edit_workload = QtWidgets.QPushButton(workload_dialog)
        self.edit_workload.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pics/editworkload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_workload.setIcon(icon1)
        self.edit_workload.setObjectName("edit_workload")
        self.horizontalLayout.addWidget(self.edit_workload)
        self.buttonBox = QtWidgets.QDialogButtonBox(workload_dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(workload_dialog)
        self.buttonBox.accepted.connect(workload_dialog.accept)
        self.buttonBox.rejected.connect(workload_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(workload_dialog)

    def retranslateUi(self, workload_dialog):
        _translate = QtCore.QCoreApplication.translate
        workload_dialog.setWindowTitle(_translate("workload_dialog", "Учебная нагрузка"))
        self.add_teacher.setToolTip(_translate("workload_dialog", "Добавить учителя"))
        self.edit_workload.setToolTip(_translate("workload_dialog", "Редактировать нагрузку"))
