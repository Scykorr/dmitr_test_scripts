# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teacher.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(980, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(30, 10, 911, 531))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(52, 90, 151, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.page_3)
        self.label_2.setGeometry(QtCore.QRect(110, 70, 47, 13))
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(52, 140, 151, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setGeometry(QtCore.QRect(90, 120, 91, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 180, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.stackedWidget.addWidget(self.page_3)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.tableWidget = QtWidgets.QTableWidget(self.page)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 541, 471))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.page)
        self.tableWidget_2.setGeometry(QtCore.QRect(570, 10, 301, 471))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.comboBox = QtWidgets.QComboBox(self.page)
        self.comboBox.setGeometry(QtCore.QRect(570, 490, 241, 22))
        self.comboBox.setObjectName("comboBox")
        self.pushButton_3 = QtWidgets.QPushButton(self.page)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 490, 131, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.page)
        self.pushButton_6.setGeometry(QtCore.QRect(820, 490, 75, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.pushButton = QtWidgets.QPushButton(self.page_2)
        self.pushButton.setGeometry(QtCore.QRect(544, 0, 141, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setGeometry(QtCore.QRect(20, 20, 47, 16))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(400, 20, 121, 16))
        self.label_4.setObjectName("label_4")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.page_2)
        self.tableWidget_3.setGeometry(QtCore.QRect(10, 40, 331, 491))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_4 = QtWidgets.QTableWidget(self.page_2)
        self.tableWidget_4.setGeometry(QtCore.QRect(350, 40, 331, 491))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(0)
        self.tableWidget_4.setRowCount(0)
        self.stackedWidget.addWidget(self.page_2)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_5 = QtWidgets.QLabel(self.page_4)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 91, 16))
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(self.page_4)
        self.textEdit.setGeometry(QtCore.QRect(10, 50, 371, 441))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_4 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 500, 131, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_5.setGeometry(QtCore.QRect(300, 10, 75, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.stackedWidget.addWidget(self.page_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 980, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "IP TFTP"))
        self.label_3.setText(_translate("MainWindow", "Папка на TFTP"))
        self.pushButton_2.setText(_translate("MainWindow", "Далее"))
        self.pushButton_3.setText(_translate("MainWindow", "Обновить"))
        self.pushButton_6.setText(_translate("MainWindow", "Добавить\n"
"эталон"))
        self.pushButton.setText(_translate("MainWindow", "назад"))
        self.label.setText(_translate("MainWindow", "Эталон"))
        self.label_4.setText(_translate("MainWindow", "Скрипт пользователя"))
        self.label_5.setText(_translate("MainWindow", "Добавить эталон"))
        self.pushButton_4.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_5.setText(_translate("MainWindow", "Назад"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
