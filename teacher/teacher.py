import pathlib
import os
import time
from datetime import datetime
from time import sleep
from types import NoneType

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPen, QFont, QColor, QBrush
from PyQt5.QtWidgets import QHeaderView, QGraphicsScene

from GUI.teacher import Ui_MainWindow
import shutil


class MainClass(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.file_name = None
        self.change_size(341, 300)
        self.setupUi(self)
        self.setWindowTitle('Проверка тестирования')
        self.pushButton_2.clicked.connect(lambda: self.choose_operator(page_index=1))
        self.lineEdit_3.setText('C:\Program Files\Tftpd64')
        self.pushButton.clicked.connect(lambda: self.choose_operator(page_index=1))
        self.users_files_table = self.tableWidget
        self.users_files_table.doubleClicked.connect(lambda: self.choose_operator(page_index=2))
        self.users_files_table.clicked.connect(
            lambda: self.show_checked_user_script(user_script_file=self.users_files_table.currentItem().text()))
        self.comboBox.currentTextChanged.connect(self.show_standard_file)
        # self.lineEdit_2.setText('10.125.20.250')
        # self.lineEdit_2.setText('192.168.1.14')
        self.lineEdit_2.setText('127.0.0.1')
        self.ip_address = self.lineEdit_2.text()
        self.pushButton_3.clicked.connect(lambda: self.choose_operator(page_index=1))
        self.pushButton_6.clicked.connect(lambda: self.choose_operator(page_index=3))
        self.pushButton_5.clicked.connect(lambda: self.choose_operator(page_index=1))
        self.pushButton_9.clicked.connect(lambda: self.choose_operator(page_index=4))
        self.pushButton_7.clicked.connect(lambda: self.choose_operator(page_index=1))
        self.pushButton_4.clicked.connect(self.add_standard)
        self.pushButton_8.clicked.connect(self.add_user_config)
        self.lineEdit_13.textChanged.connect(self.draw_scheme)
        self.lineEdit_14.textChanged.connect(self.draw_scheme)
        self.lineEdit_15.textChanged.connect(self.draw_scheme)
        self.lineEdit_16.textChanged.connect(self.draw_scheme)
        self.lineEdit_33.textChanged.connect(self.draw_scheme)
        self.lineEdit_34.textChanged.connect(self.draw_scheme)
        self.lineEdit_35.textChanged.connect(self.draw_scheme)
        self.lineEdit_36.textChanged.connect(self.draw_scheme)
        self.lineEdit_37.textChanged.connect(self.draw_scheme)
        self.lineEdit_38.textChanged.connect(self.draw_scheme)
        self.lineEdit_39.textChanged.connect(self.draw_scheme)
        self.lineEdit_40.textChanged.connect(self.draw_scheme)
        self.lineEdit_41.textChanged.connect(self.draw_scheme)
        self.lineEdit_42.textChanged.connect(self.draw_scheme)
        self.lineEdit_43.textChanged.connect(self.draw_scheme)
        self.lineEdit_44.textChanged.connect(self.draw_scheme)
        self.pushButton_10.clicked.connect(self.add_scheme_config)
        self.pushButton_13.clicked.connect(self.show_schema_etalon)
        self.pushButton_11.clicked.connect(lambda: self.choose_operator(page_index=5))
        self.pushButton_12.clicked.connect(lambda: self.choose_operator(page_index=1))
        # self.get_files_amout()
        # self.get_files_amount_var()

    def choose_operator(self, page_index):
        if page_index == 1:
            self.stackedWidget.setCurrentIndex(page_index)
            self.change_size(1400, 991)
            if self.comboBox.currentText() == '':
                self.get_standard_files()
            if self.comboBox_2.currentText() == '':
                self.get_standard_files_var()
            self.show_standard_file()
            self.get_user_files()
            self.draw_scheme()
        elif page_index == 2:
            if '.conf' in self.users_files_table.currentItem().text():
                self.change_size(1400, 700)
                self.stackedWidget.setCurrentIndex(page_index)
                self.show_user_script(self.users_files_table.currentItem().text())
        elif page_index == 3:
            self.change_size(448, 561)
            self.stackedWidget.setCurrentIndex(page_index)
        elif page_index == 4:
            self.change_size(448, 561)
            self.stackedWidget.setCurrentIndex(page_index)
        elif page_index == 5:
            self.change_size(1400, 991)
            self.stackedWidget.setCurrentIndex(page_index)

    def get_standard_files(self):

        standard_file_amount = int(self.get_files_amout())

        for number in range(1, standard_file_amount + 1):
            # os.system(f'tftp {self.lineEdit_2.text()} GET {number}.txt')
            # shutil.copy2(f'{number}.txt', self.lineEdit_3.text())
            # os.remove(f'{number}.txt')
            os.system(f'tftp {self.lineEdit_2.text()} GET {number}.conf')
            shutil.copy2(f'{number}.conf', self.lineEdit_3.text())
            os.remove(f'{number}.conf')

        directory = self.lineEdit_3.text()

        files = list()

        files += os.listdir(directory)
        standard_files = list()

        for file in files:
            for el in range(31):
                if str(el) in file and '.conf' in file and 'var_' not in file:
                    standard_files.append(file)
                    break

        self.comboBox.clear()
        self.comboBox.addItems(standard_files)

    def get_standard_files_var(self):

        standard_file_amount = int(self.get_files_amount_var())

        for number in range(1, standard_file_amount + 1):
            # os.system(f'tftp {self.lineEdit_2.text()} GET {number}.txt')
            # shutil.copy2(f'{number}.txt', self.lineEdit_3.text())
            # os.remove(f'{number}.txt')
            os.system(f'tftp {self.lineEdit_2.text()} GET var_{number}.conf')
            time.sleep(0.5)
            shutil.copy2(f'var_{number}.conf', self.lineEdit_3.text())
            os.remove(f'var_{number}.conf')

        directory = self.lineEdit_3.text()

        files = list()

        files += os.listdir(directory)
        standard_files = list()

        for file in files:
            for el in range(31):
                if str(el) in file and '.conf' in file and 'var_' in file:
                    standard_files.append(file)
                    break

        self.comboBox_2.clear()
        self.comboBox_2.addItems(standard_files)

    def get_user_files(self):
        directory = self.lineEdit_3.text()
        files = list()

        files += os.listdir(directory)
        users_files = list()
        for file in files:
            print(file.split('.conf'))
            if '.conf' in file and file.split('.conf')[0] not in map(str, range(31)) and 'var_' not in file:
                users_files.append(file)
        self.users_files_table.setColumnCount(5)
        self.users_files_table.setRowCount(len(users_files))
        self.users_files_table.setHorizontalHeaderLabels(
            ["Строки скрипта", "Ош.\nстрок", "Лишние\nстроки", "Ош.\nсимволов", "Время сохранения файла"])
        header = self.users_files_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)

        file_name_standard = self.comboBox.currentText()
        if file_name_standard == '':
            file_name_standard = '1.conf'
        os.system(f'tftp {self.lineEdit_2.text()} GET {file_name_standard}')
        with open(f'{file_name_standard}', 'r') as f_standard:
            st_text = f_standard.read()

        standard_text_list = st_text.split('\n')

        for index_el, el in enumerate(users_files):
            filename = f"{self.lineEdit_3.text()}\\{el}"
            mtime = os.path.getmtime(filename)
            mtime_readable = datetime.fromtimestamp(mtime)
            self.users_files_table.setItem(index_el, 0, QtWidgets.QTableWidgetItem(str(el)))
            self.users_files_table.setItem(index_el, 4, QtWidgets.QTableWidgetItem(str(mtime_readable)))
            os.system(f'tftp {self.lineEdit_2.text()} GET {file_name_standard}')
            with open(f'{filename}', 'r') as f_user:
                usr_text = f_user.read()
            user_text_list = usr_text.split('\n')
            if len(user_text_list) > len(standard_text_list):
                self.users_files_table.setItem(index_el, 2, QtWidgets.QTableWidgetItem(
                    str(len(user_text_list) - len(standard_text_list))))
            else:
                self.users_files_table.setItem(index_el, 2, QtWidgets.QTableWidgetItem(str(0)))
            counter_error_strings = 0
            counter_error_symbols = 0
            if len(user_text_list) < len(standard_text_list):
                user_text_list += [''] * (len(standard_text_list) - len(user_text_list))
            user_text_edge = user_text_list[:len(standard_text_list)]
            for i_el, elem in enumerate(standard_text_list):
                if elem != user_text_edge[i_el]:
                    counter_error_strings += 1
                    for i_symb, letter in enumerate(elem):
                        if len(elem) > len(user_text_edge[i_el]):
                            user_text_edge[i_el] += 'a' * (len(elem) - len(user_text_edge[i_el]))
                        if letter != user_text_edge[i_el][i_symb]:
                            counter_error_symbols += 1
            self.users_files_table.setItem(index_el, 1, QtWidgets.QTableWidgetItem(str(counter_error_strings)))
            self.users_files_table.setItem(index_el, 3, QtWidgets.QTableWidgetItem(str(counter_error_symbols)))
        pathlib.Path(f'{file_name_standard}').unlink()

    def show_standard_file(self):
        file_name_standard = self.comboBox.currentText()
        if file_name_standard == '':
            file_name_standard = '1.conf'
        os.system(f'tftp {self.lineEdit_2.text()} GET {file_name_standard}')
        with open(f'{file_name_standard}', 'r') as f_standard:
            st_text = f_standard.read()

        self.tableWidget_2.clear()
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setColumnCount(0)

        # init tableWidgets

        standard_text_list = st_text.split('\n')

        # second standard widget

        standard_table_second = self.tableWidget_3
        standard_table_second.setRowCount(len(standard_text_list))
        standard_table_second.setColumnCount(1)
        standard_table_second.setHorizontalHeaderLabels(["Строки скрипта"])

        for index_el, el in enumerate(standard_text_list):
            standard_table_second.setItem(index_el, 0, QtWidgets.QTableWidgetItem(str(el)))
        standard_table_second.resizeColumnsToContents()
        pathlib.Path(f'{file_name_standard}').unlink()

        self.get_user_files()

    def show_user_script(self, user_script_file):
        self.tableWidget_4.clear()
        if '.conf' in user_script_file:
            file_name_standard = self.comboBox.currentText()
            os.system(f'tftp {self.lineEdit_2.text()} GET {file_name_standard}')
            with open(f'{file_name_standard}', 'r') as f_standard:
                st_text = f_standard.read()

            # init tableWidgets

            standard_text_list = st_text.split('\n')

            os.system(f'tftp {self.lineEdit_2.text()} GET {user_script_file}')
            with open(f'{user_script_file}', 'r') as f:
                text = f.read()

            user_text_list = text.split('\n')
            user_table = self.tableWidget_4
            if len(user_text_list) < len(standard_text_list):
                user_list_len = len(standard_text_list)
            else:
                user_list_len = len(user_text_list)
            user_table.setRowCount(user_list_len)
            user_table.setColumnCount(1)
            user_table.setHorizontalHeaderLabels(["Строки скрипта"])

            for index_el, el in enumerate(user_text_list):
                user_table.setItem(index_el, 0, QtWidgets.QTableWidgetItem(str(el)))

            pathlib.Path(f'{user_script_file}').unlink()
            pathlib.Path(f'{file_name_standard}').unlink()
            self.check_answer(standard_text_list, user_text_list)
            user_table.resizeColumnsToContents()

    def check_answer(self, etalon_text_list, user_list):
        user_table = self.tableWidget_4
        etalon_table = self.tableWidget_3
        if len(user_list) > len(etalon_text_list):
            etalon_text_list += [''] * (len(user_list) - len(etalon_text_list))
            etalon_table.setRowCount(len(user_list))
        for el_index in range(len(etalon_text_list)):
            user_text = ''
            print()
            if type(user_table.item(el_index, 0)) == NoneType:
                user_table.setItem(el_index, 0, QtWidgets.QTableWidgetItem(str('')))
            else:
                user_text = user_table.item(el_index, 0).text()

            etalon_text = ''
            if type(etalon_table.item(el_index, 0)) == NoneType:
                etalon_table.setItem(el_index, 0, QtWidgets.QTableWidgetItem(str('')))
            else:
                etalon_text = etalon_table.item(el_index, 0).text()

            if user_text != etalon_text:
                user_table.item(el_index, 0).setBackground(QtGui.QColor(255, 0, 0))
        user_table.resizeColumnsToContents()

    def change_size(self, width, height):
        self.setFixedWidth(width)
        self.setFixedHeight(height)

    def show_checked_user_script(self, user_script_file):
        self.tableWidget_2.clear()
        if self.users_files_table.currentColumn() == 0:
            file_name_standard = self.comboBox.currentText()
            os.system(f'tftp {self.lineEdit_2.text()} GET {file_name_standard}')
            with open(f'{file_name_standard}', 'r') as f_standard:
                st_text = f_standard.read()

            # init tableWidgets

            standard_text_list = st_text.split('\n')

            # os.system(f'tftp {self.lineEdit_2.text()} GET {user_script_file}')
            os.system(f'tftp 127.0.0.1 GET {user_script_file}')
            with open(f'{user_script_file}', 'r') as f:
                text = f.read()

            user_text_list = text.split('\n')
            user_table = self.tableWidget_2
            if len(user_text_list) < len(standard_text_list):
                user_list_len = len(standard_text_list)
            else:
                user_list_len = len(user_text_list)
            user_table.setRowCount(user_list_len)
            user_table.setColumnCount(1)
            user_table.setHorizontalHeaderLabels(["Строки скрипта"])

            for index_el, el in enumerate(user_text_list):
                if type(user_table.item(index_el, 0)) == NoneType:
                    user_table.setItem(index_el, 0, QtWidgets.QTableWidgetItem(str('')))
                user_table.setItem(index_el, 0, QtWidgets.QTableWidgetItem(str(el)))
            user_table.resizeColumnsToContents()
            pathlib.Path(f'{user_script_file}').unlink()
            pathlib.Path(f'{file_name_standard}').unlink()
            self.checked_user_script(standard_text_list, user_text_list)

    def checked_user_script(self, etalon_text_list, user_list):
        user_table = self.tableWidget_2

        if len(user_list) > len(etalon_text_list):
            etalon_text_list += [''] * (len(user_list) - len(etalon_text_list))
        for el_index in range(len(etalon_text_list)):
            user_text = ''
            print()
            if type(user_table.item(el_index, 0)) == NoneType:
                user_table.setItem(el_index, 0, QtWidgets.QTableWidgetItem(str('')))
            else:
                user_text = user_table.item(el_index, 0).text()

            etalon_text = etalon_text_list[el_index]

            if user_text != etalon_text:
                user_table.item(el_index, 0).setBackground(QtGui.QColor(255, 0, 0))
        user_table.resizeColumnsToContents()

    def add_standard(self):
        path_file_name = self.lineEdit_3.text()
        files = list()
        files += os.listdir(path_file_name)
        standard_files = list()
        for file in files:
            for el in range(31):
                if str(el) in file:
                    standard_files.append(file)
        num = len(standard_files) + 1
        file_name = f'{num}.conf'
        pathlib.Path(f'{file_name}').touch()
        pathlib.Path(f'{file_name}').write_text(self.textEdit.toPlainText())
        os.system(f'tftp {self.ip_address} PUT {file_name}')
        self.textEdit.clear()
        pathlib.Path(f'{file_name}').unlink()
        self.update_files_amount()
        self.get_standard_files()

    def add_user_config(self):
        path_file_name = self.lineEdit_3.text()
        files = list()
        files += os.listdir(path_file_name)
        standard_files = list()
        for file in files:
            for el in range(31):
                if 'var_' + str(el) in file:
                    standard_files.append(file)
        num = len(standard_files) + 1
        print(num)
        file_name = f'var_{num}.conf'
        print(file_name)
        pathlib.Path(f'{file_name}').touch()
        pathlib.Path(f'{file_name}').write_text(self.textEdit_2.toPlainText())
        os.system(f'tftp {self.ip_address} PUT {file_name}')
        self.textEdit_2.clear()
        pathlib.Path(f'{file_name}').unlink()
        print(file_name)
        self.update_files_amount_var()
        self.get_standard_files_var()

    def get_files_amout(self):
        print(self.lineEdit_2.text())
        os.system(f'tftp {self.lineEdit_2.text()} get files_amount.txt')
        time.sleep(0.5)
        print(f'tftp {self.lineEdit_2.text()} get files_amount.txt')
        with open(f'files_amount.txt', 'r') as f_amount:
            f_amount_result = f_amount.read().split()[0]
        os.remove(f'files_amount.txt')
        return f_amount_result

    def get_files_amount_var(self):
        os.system(f'tftp {self.lineEdit_2.text()} get files_amount_var.txt')
        with open(f'files_amount_var.txt', 'r') as f_amount:
            f_amount_result = f_amount.read().split()[0]
        os.remove(f'files_amount_var.txt')
        return f_amount_result

    def update_files_amount(self):
        os.system(f'tftp {self.lineEdit_2.text()} get files_amount.txt')
        with open(f'files_amount.txt', 'r') as f_amount:
            f_amount_result = f_amount.read().split()[0]
        with open(f'files_amount.txt', 'w') as f_amount:
            f_amount.write(str(int(f_amount_result) + 1))
        os.system(f'tftp {self.lineEdit_2.text()} put files_amount.txt')
        os.remove(f'files_amount.txt')

    def update_files_amount_var(self):
        os.system(f'tftp {self.lineEdit_2.text()} get files_amount_var.txt')
        with open(f'files_amount_var.txt', 'r') as f_amount:
            f_amount_result = f_amount.read().split()[0]
        with open(f'files_amount_var.txt', 'w') as f_amount:
            f_amount.write(str(int(f_amount_result) + 1))
        os.system(f'tftp {self.lineEdit_2.text()} put files_amount_var.txt')
        os.remove(f'files_amount_var.txt')

    def draw_scheme(self):
        # === Очистка старой сцены (если была) ===
        if hasattr(self, 'scene'):
            self.scene.clear()
        else:
            self.scene = QGraphicsScene()

        # === Настройка стилей ===
        black_pen = QPen(Qt.black, 2)
        gray_brush = QBrush(QColor(192, 192, 192))

        # === Рисование блоков ===
        self.draw_block(self.scene, 0, 0, "IAD", "ЦАТС\nDX-500С", "IP-ATC\nT-76С", "T-76С", "E+H1", "S", "M")
        # self.draw_block(self.scene, 350, 100, "UATC", "ΔX-500С", "IP-ATC", "T-76С", "E+H1", "S", "M")
        # self.draw_block(self.scene, 650, 100, "UATC", "ΔX-500С", "IP-ATC", "T-76С", "E+H1", "S", "M")

        # === Добавление дополнительных элементов ===
        self.draw_additional_elements(self.scene)

        # === Привязка сцены к view ===
        self.graphicsView.setScene(self.scene)
        self.graphicsView.setRenderHint(QtGui.QPainter.Antialiasing)
        self.graphicsView_2.setScene(self.scene)
        self.graphicsView_2.setRenderHint(QtGui.QPainter.Antialiasing)
        self.graphicsView_3.setScene(self.scene)
        self.graphicsView_3.setRenderHint(QtGui.QPainter.Antialiasing)

    def draw_block(self, scene, x, y, bottom_text, bottom_left_text, middle_text, top_text, top_right_text, s_label,
                   m_label):
        from PyQt5.QtGui import QPolygonF

        font = QFont("Arial", 12)

        # Прямоугольник IAD
        polygon_iad = QPolygonF([
            QPointF(x - 90, y + 400),
            QPointF(x - 30, y + 400),
            QPointF(x - 60, y + 350)
        ])
        scene.addPolygon(polygon_iad, QPen(Qt.black, 2), QBrush(QColor(192, 192, 192)))
        scene.addText(bottom_text, font).setPos(x - 75, y + 400)

        # Треугольник M
        polygon_m = QPolygonF([
            QPointF(x - 250, y + 200),
            QPointF(x - 190, y + 200),
            QPointF(x - 220, y + 150)
        ])
        scene.addPolygon(polygon_m, QPen(Qt.black, 2), QBrush(QColor(192, 192, 192)))
        scene.addText(m_label, font).setPos(x - 215, y + 135)
        scene.addText('DX-500C\n     №1', font).setPos(x - 255, y + 200)

        # Треугольник S
        polygon_s = QPolygonF([
            QPointF(x - 90, y + 200),
            QPointF(x - 30, y + 200),
            QPointF(x - 60, y + 150)
        ])
        scene.addPolygon(polygon_s, QPen(Qt.black, 2), QBrush(QColor(192, 192, 192)))
        scene.addText(s_label, font).setPos(x - 90, y + 135)
        scene.addText('IP ATC\nT-76C №1', font).setPos(x - 90, y + 200)
        scene.addText("Eth0", font).setPos(-55, 135)

        # numbers S
        scene.addLine(-60, 150, -40, 100, QPen(Qt.black, 2))
        scene.addLine(-60, 150, -80, 100, QPen(Qt.black, 2))
        scene.addRect(x - 90, y + 73, 25, 25, QPen(Qt.black, 2), QBrush(QColor(192, 192, 192)))
        scene.addRect(x - 50, y + 73, 25, 25, QPen(Qt.black, 2), QBrush(QColor(192, 192, 192)))

        # numbers S1
        scene.addLine(260, 150, 280, 100, QPen(Qt.black, 2))
        scene.addLine(260, 150, 240, 100, QPen(Qt.black, 2))
        scene.addRect(x + 230, y + 73, 25, 25, QPen(Qt.black, 2), QBrush(QColor(192, 192, 192)))
        scene.addRect(x + 270, y + 73, 25, 25, QPen(Qt.black, 2), QBrush(QColor(192, 192, 192)))

        # коммутатор 1
        polygon_k1 = QPolygonF([
            QPointF(x - 150, y + 300),
            QPointF(x - 100, y + 300),
            QPointF(x - 120, y + 330),
            QPointF(x - 170, y + 330)
        ])
        scene.addPolygon(polygon_k1, QPen(Qt.black, 2), QBrush(QColor(192, 192, 192)))
        scene.addText('→', font).setPos(x - 147, y + 296)
        scene.addText('←', font).setPos(x - 147, y + 306)

        # овал сеть
        scene.addEllipse(x + 30, y + 150, 100, 50, QPen(Qt.black, 2), QBrush(QColor(192, 192, 192)))
        scene.addText("ТСКП", font).setPos(55, 160)

        # Треугольник S1
        polygon_s1 = QPolygonF([
            QPointF(x + 290, y + 200),
            QPointF(x + 230, y + 200),
            QPointF(x + 260, y + 150)
        ])
        scene.addPolygon(polygon_s1, QPen(Qt.black, 2), QBrush(QColor(192, 192, 192)))
        scene.addText(s_label, font).setPos(x + 270, y + 135)
        scene.addText('IP ATC\nT-76C №2', font).setPos(x + 230, y + 200)
        scene.addText("Eth0", font).setPos(210, 135)

        # Треугольник M1
        polygon_m1 = QPolygonF([
            QPointF(x + 450, y + 200),
            QPointF(x + 390, y + 200),
            QPointF(x + 420, y + 150)
        ])
        scene.addPolygon(polygon_m1, QPen(Qt.black, 2), QBrush(QColor(192, 192, 192)))
        scene.addText(m_label, font).setPos(x + 390, y + 135)
        scene.addText('DX-500C\n     №2', font).setPos(x + 385, y + 200)

        # Треугольник DX 500C
        polygon_ksh = QPolygonF([
            QPointF(x + 300, y + 400),
            QPointF(x + 240, y + 400),
            QPointF(x + 270, y + 350)
        ])
        scene.addPolygon(polygon_ksh, QPen(Qt.black, 2), QBrush(QColor(192, 192, 192)))
        scene.addText('DX-500C\n     №3', font).setPos(x + 240, y + 400)

        # Прямоугольник КШ-100
        scene.addRect(x + 180, y + 350, 25, 50, QPen(Qt.black, 2), QBrush(QColor(192, 192, 192)))
        scene.addText('КШ-100', font).setPos(x + 160, y + 400)

        # коммутатор 2
        polygon_k1 = QPolygonF([
            QPointF(x + 180, y + 250),
            QPointF(x + 230, y + 250),
            QPointF(x + 210, y + 280),
            QPointF(x + 160, y + 280)
        ])
        scene.addPolygon(polygon_k1, QPen(Qt.black, 2), QBrush(QColor(192, 192, 192)))
        scene.addText('→', font).setPos(x + 183, y + 245)
        scene.addText('←', font).setPos(x + 183, y + 254)

        # # Прямоугольник IP-ATC
        # scene.addRect(x + 150, y + 100, 150, 100, QPen(Qt.black, 2), QBrush(QColor(192, 192, 192)))
        # scene.addText(middle_text, font).setPos(x + 170, y + 150)

        # # Треугольник E+H1
        # polygon_eh1 = QPolygonF([
        #     QPointF(x + 150, y + 100),
        #     QPointF(x + 150, y),
        #     QPointF(x + 225, y + 50)
        # ])
        # scene.addPolygon(polygon_eh1, QPen(Qt.black, 2), QBrush(QColor(192, 192, 192)))
        # scene.addText(top_right_text, font).setPos(x + 160, y + 20)

        # # Текст T-76С
        # scene.addText(top_text, font).setPos(x + 170, y + 120)

        # # Текст ΔX-500С
        # scene.addText(bottom_left_text, font).setPos(x + 20, y + 300)

    def draw_additional_elements(self, scene):
        font = QFont("Arial", 12)

        # изменяемые подписи
        # IP ATC T-76C №1

        # IP ATC T-76C №2

        # SIP,RPT Слева

        # SIP,RPT Справа

        # IP ATC T-76C №1 порты
        scene.addText(self.lineEdit_13.text(), font).setPos(-103, 110)
        scene.addText(self.lineEdit_14.text(), font).setPos(-50, 110)

        # IP ATC T-76C №2 порты
        scene.addText(self.lineEdit_15.text(), font).setPos(220, 110)
        scene.addText(self.lineEdit_16.text(), font).setPos(270, 110)

        # IP ATC T-76C №1 номера
        scene.addText(self.lineEdit_33.text() + '-\n' + self.lineEdit_34.text(), font).setPos(-100, 30)

        # IP ATC T-76C №2 номера
        scene.addText(self.lineEdit_35.text() + '-\n' + self.lineEdit_36.text(), font).setPos(220, 30)

        # DX-500C №1 номера
        scene.addText(self.lineEdit_37.text() + '-\n' + self.lineEdit_38.text(), font).setPos(-270, 110)

        # DX-500C №2 номера
        scene.addText(self.lineEdit_39.text() + '-\n' + self.lineEdit_40.text(), font).setPos(410, 110)

        # DX-500C №3 номера
        scene.addText(self.lineEdit_41.text() + '-\n' + self.lineEdit_42.text(), font).setPos(260, 310)

        # IAD номера
        scene.addText(self.lineEdit_43.text() + '-\n' + self.lineEdit_44.text(), font).setPos(-70, 310)

        # Линии
        # M-S
        scene.addLine(-212, 160, -68, 160, QPen(Qt.black, 2))
        scene.addText("E1", font).setPos(-155, 135)

        # S-коммутатор
        scene.addLine(-120, 195, -89, 195, QPen(Qt.black, 2))
        scene.addLine(-120, 195, -120, 300, QPen(Qt.black, 2))
        scene.addText("Eth1", font).setPos(-125, 170)

        # коммутатор-IAD
        scene.addLine(-130, 330, -130, 360, QPen(Qt.black, 2))
        scene.addLine(-150, 330, -150, 380, QPen(Qt.black, 2))
        scene.addLine(-130, 360, -68, 360, QPen(Qt.black, 2))
        scene.addLine(-150, 380, -80, 380, QPen(Qt.black, 2))
        scene.addText("SIP", font).setPos(-115, 335)
        scene.addText("RTP", font).setPos(-140, 377)

        # S-Network
        scene.addLine(-53, 160, 41, 160, QPen(Qt.black, 2))

        # Network-S1
        scene.addLine(122, 160, 255, 160, QPen(Qt.black, 2))

        # S1-M1
        scene.addLine(269, 160, 412, 160, QPen(Qt.black, 2))
        scene.addText("E1", font).setPos(330, 135)

        # S1-маршрутизатор
        scene.addLine(190, 190, 235, 190, QPen(Qt.black, 2))
        scene.addLine(190, 190, 190, 250, QPen(Qt.black, 2))
        scene.addText("Eth1", font).setPos(150, 210)

        # маршрутизатор-КШ-100
        scene.addLine(185, 280, 185, 350, QPen(Qt.black, 2))
        scene.addLine(200, 280, 200, 350, QPen(Qt.black, 2))
        scene.addText("SIP", font).setPos(150, 300)
        scene.addText("RTP", font).setPos(200, 300)

        # КШ-100-DX-500C
        scene.addLine(205, 370, 258, 370, QPen(Qt.black, 2))
        scene.addText("E1", font).setPos(220, 348)

    def add_scheme_config(self):
        filename_schema_etalon = 'scheme_etalon.txt'
        with open(filename_schema_etalon, 'w') as f_etalon:
            fields_list = list()
            fields_list = [self.lineEdit_5.text(), self.lineEdit_6.text(), self.lineEdit_7.text(),
                           self.lineEdit_8.text(), self.lineEdit_9.text(), self.lineEdit_10.text(),
                           self.lineEdit_11.text(), self.lineEdit_12.text(), self.lineEdit_13.text(),
                           self.lineEdit_14.text(), self.lineEdit_15.text(), self.lineEdit_16.text(),
                           self.lineEdit_33.text(), self.lineEdit_34.text(), self.lineEdit_35.text(),
                           self.lineEdit_36.text(), self.lineEdit_37.text(), self.lineEdit_38.text(),
                           self.lineEdit_39.text(), self.lineEdit_40.text(), self.lineEdit_41.text(),
                           self.lineEdit_42.text(), self.lineEdit_43.text(), self.lineEdit_44.text(), ]
            res_text = '\n'.join(fields_list)
            f_etalon.write(res_text)
        os.system(f'tftp {self.ip_address} PUT {filename_schema_etalon}')
        os.remove('scheme_etalon.txt')

    def show_schema_etalon(self):
        filename_schema_etalon = 'scheme_etalon.txt'
        os.system(f'tftp {self.ip_address} GET {filename_schema_etalon}')
        with open(filename_schema_etalon, 'r') as f_etalon:
            lines = [line.strip() for line in f_etalon.readlines()]
            print(lines)
        self.lineEdit_5.setText(lines[0])
        self.lineEdit_6.setText(lines[1])
        self.lineEdit_7.setText(lines[2])
        self.lineEdit_8.setText(lines[3])
        self.lineEdit_9.setText(lines[4])
        self.lineEdit_10.setText(lines[5])
        self.lineEdit_11.setText(lines[6])
        self.lineEdit_12.setText(lines[7])
        self.lineEdit_13.setText(lines[8])
        self.lineEdit_14.setText(lines[9])
        self.lineEdit_15.setText(lines[10])
        self.lineEdit_16.setText(lines[11])
        self.lineEdit_33.setText(lines[12])
        self.lineEdit_34.setText(lines[13])
        self.lineEdit_35.setText(lines[14])
        self.lineEdit_36.setText(lines[15])
        self.lineEdit_37.setText(lines[16])
        self.lineEdit_38.setText(lines[17])
        self.lineEdit_39.setText(lines[18])
        self.lineEdit_40.setText(lines[19])
        self.lineEdit_41.setText(lines[20])
        self.lineEdit_42.setText(lines[21])
        self.lineEdit_43.setText(lines[22])
        self.lineEdit_44.setText(lines[23])
        os.remove('scheme_etalon.txt')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    w = MainClass()
    w.show()

    sys.exit(app.exec_())
