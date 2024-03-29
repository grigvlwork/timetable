# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(398, 276)
        font = QtGui.QFont()
        font.setPointSize(10)
        main_window.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(main_window)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.year_label = QtWidgets.QLabel(main_window)
        self.year_label.setObjectName("year_label")
        self.gridLayout.addWidget(self.year_label, 0, 0, 1, 1)
        self.choose_year_button = QtWidgets.QPushButton(main_window)
        self.choose_year_button.setObjectName("choose_year_button")
        self.gridLayout.addWidget(self.choose_year_button, 0, 1, 1, 1)
        self.month_label = QtWidgets.QLabel(main_window)
        self.month_label.setObjectName("month_label")
        self.gridLayout.addWidget(self.month_label, 1, 0, 1, 1)
        self.choose_month_button = QtWidgets.QPushButton(main_window)
        self.choose_month_button.setObjectName("choose_month_button")
        self.gridLayout.addWidget(self.choose_month_button, 1, 1, 1, 1)
        self.teachers_button = QtWidgets.QPushButton(main_window)
        self.teachers_button.setObjectName("teachers_button")
        self.gridLayout.addWidget(self.teachers_button, 2, 0, 1, 1)
        self.work_weekends_button = QtWidgets.QPushButton(main_window)
        self.work_weekends_button.setObjectName("work_weekends_button")
        self.gridLayout.addWidget(self.work_weekends_button, 2, 1, 1, 1)
        self.holydays_button = QtWidgets.QPushButton(main_window)
        self.holydays_button.setObjectName("holydays_button")
        self.gridLayout.addWidget(self.holydays_button, 3, 0, 1, 1)
        self.directories_button = QtWidgets.QPushButton(main_window)
        self.directories_button.setObjectName("directories_button")
        self.gridLayout.addWidget(self.directories_button, 3, 1, 1, 1)
        self.workload_button = QtWidgets.QPushButton(main_window)
        self.workload_button.setObjectName("workload_button")
        self.gridLayout.addWidget(self.workload_button, 4, 0, 1, 1)
        self.sick_list_button = QtWidgets.QPushButton(main_window)
        self.sick_list_button.setObjectName("sick_list_button")
        self.gridLayout.addWidget(self.sick_list_button, 4, 1, 1, 1)
        self.vacation_button = QtWidgets.QPushButton(main_window)
        self.vacation_button.setObjectName("vacation_button")
        self.gridLayout.addWidget(self.vacation_button, 5, 0, 1, 1)
        self.replacement_button = QtWidgets.QPushButton(main_window)
        self.replacement_button.setObjectName("replacement_button")
        self.gridLayout.addWidget(self.replacement_button, 5, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.make_timetable_button = QtWidgets.QPushButton(main_window)
        self.make_timetable_button.setObjectName("make_timetable_button")
        self.verticalLayout.addWidget(self.make_timetable_button)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Предварительные настройки"))
        self.year_label.setText(_translate("main_window", "Текущий год ____"))
        self.choose_year_button.setText(_translate("main_window", "Выбрать"))
        self.month_label.setText(_translate("main_window", "Текущий месяц ______"))
        self.choose_month_button.setText(_translate("main_window", "Выбрать"))
        self.teachers_button.setText(_translate("main_window", "Учителя"))
        self.work_weekends_button.setText(_translate("main_window", "Рабочие выходные"))
        self.holydays_button.setText(_translate("main_window", "Праздники"))
        self.directories_button.setText(_translate("main_window", "Справочники"))
        self.workload_button.setText(_translate("main_window", "Учебная нагрузка"))
        self.sick_list_button.setText(_translate("main_window", "Больничные"))
        self.vacation_button.setText(_translate("main_window", "Отпуски"))
        self.replacement_button.setText(_translate("main_window", "Замены"))
        self.make_timetable_button.setText(_translate("main_window", "Перейти к табелю"))
