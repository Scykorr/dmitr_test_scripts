import pathlib
import os
from types import NoneType

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QBrush, QColor, QPen, QFont, QPolygonF
from PyQt5.QtWidgets import QGraphicsScene, QMessageBox

from GUI.client import Ui_MainWindow
import socket


def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip


class MainClass(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.file_name = None
        self.change_size(341, 341)
        self.setupUi(self)
        self.setWindowTitle('Клиент тестирования')
        self.lineEdit_2.setText('127.0.0.1')
        self.curr_ip = self.lineEdit_2.text()
        self.pushButton_2.clicked.connect(lambda: self.choose_operator(page_index=1))
        self.pushButton.clicked.connect(lambda: self.choose_operator(page_index=2))
        self.lineEdit.setText('')
        self.lineEdit_4.setText('1.conf')
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
        self.pushButton_4.clicked.connect(self.get_schema_answer)
        self.pushButton_4.setVisible(False)
        self.pushButton_3.clicked.connect(self.get_variant_scheme)
        user_file_name = list()

    def check_user_file_name(self, filename):
        os.system(f'tftp {self.lineEdit_2.text()} GET {filename}.conf')
        return os.path.exists(f'{filename}.conf')

    def choose_operator(self, page_index):
        self.curr_ip = self.lineEdit_2.text()
        self.file_name = '_'.join(self.lineEdit.text().split())
        result_repeat = self.check_user_file_name(self.file_name)

        if self.lineEdit.text() == "":
            err_dialog = QtWidgets.QErrorMessage(self)
            err_dialog.showMessage("Заполните поле ФИО!")
        elif result_repeat:
            err_dialog = QtWidgets.QErrorMessage(self)
            err_dialog.showMessage("Данный пользователь уже прошел тестирование!")
            os.remove(f'{self.file_name}.conf')
        elif page_index == 1 and self.lineEdit.text() != "":
            self.change_size(1450, 731)
            self.stackedWidget.setCurrentIndex(page_index)
            standard_num = self.lineEdit_4.text().split('.conf')[0]
            os.system(f'tftp {self.lineEdit_2.text()} GET {self.lineEdit_17.text()}')
            with open(f'{self.lineEdit_17.text()}', 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    self.textEdit.append(line.replace('\n', ''))
            os.remove(f'{self.lineEdit_17.text()}')
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
        elif page_index == 2:
            self.change_size(1083, 575)
            pathlib.Path(f'{self.file_name}.conf').touch()
            pathlib.Path(f'{self.file_name}.conf').write_text(self.textEdit.toPlainText())
            os.system(f'tftp {self.curr_ip} PUT {self.file_name}.conf')
            self.stackedWidget.setCurrentIndex(page_index)
            os.system(f'tftp {self.curr_ip} GET {self.file_name}.conf')
            with open(f'{self.file_name}.conf', 'r') as f:
                text = f.read()

            file_name_etalon = self.lineEdit_4.text()
            os.system(f'tftp {self.curr_ip} GET {file_name_etalon}')
            # print(self.curr_ip)
            # print(file_name_etalon)
            with open(f'{file_name_etalon}', 'r') as f_etalon:
                et_text = f_etalon.read()

            # init tableWidgets

            etalon_text_list = et_text.split('\n')
            etalon_table = self.tableWidget_2
            etalon_table.setRowCount(len(etalon_text_list))
            etalon_table.setColumnCount(1)
            etalon_table.setHorizontalHeaderLabels(["Строки скрипта"])

            for index_el, el in enumerate(etalon_text_list):
                etalon_table.setItem(index_el, 0, QtWidgets.QTableWidgetItem(str(el)))

            user_text_list = text.split('\n')
            user_table = self.tableWidget
            if len(user_text_list) < len(etalon_text_list):
                user_list_len = len(etalon_text_list)
            elif len(user_text_list) > len(etalon_text_list):
                etalon_text_list += [''] * (len(user_text_list) - len(etalon_text_list))
                user_list_len = len(user_text_list)
            else:
                user_list_len = len(user_text_list)
            user_table.setRowCount(user_list_len)
            user_table.setColumnCount(1)
            user_table.setHorizontalHeaderLabels(["Строки скрипта"])

            for index_el, el in enumerate(user_text_list):
                user_table.setItem(index_el, 0, QtWidgets.QTableWidgetItem(str(el)))

            pathlib.Path(f'{self.file_name}.conf').unlink()
            pathlib.Path(f'{file_name_etalon}').unlink()
            self.check_answer(etalon_text_list)
            self.tableWidget.resizeColumnsToContents()
            self.tableWidget_2.resizeColumnsToContents()

    def change_size(self, width, height):
        self.setFixedWidth(width)
        self.setFixedHeight(height)

    def check_answer(self, etalon_text_list):
        user_table = self.tableWidget
        etalon_table = self.tableWidget_2
        for el_index in range(len(etalon_text_list)):
            user_text = ''
            etalon_text = ''
            print()
            if type(user_table.item(el_index, 0)) == NoneType:
                user_table.setItem(el_index, 0, QtWidgets.QTableWidgetItem(str('')))
            else:
                user_text = user_table.item(el_index, 0).text()
            if type(etalon_table.item(el_index, 0)) == NoneType:
                etalon_table.setItem(el_index, 0, QtWidgets.QTableWidgetItem(str('')))
            else:
                etalon_text = etalon_table.item(el_index, 0).text()
            if user_text != etalon_text:
                user_table.item(el_index, 0).setBackground(QtGui.QColor(255, 0, 0))

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

       #КШ-100-DX-500C
        scene.addLine(205, 370, 258, 370, QPen(Qt.black, 2))
        scene.addText("E1", font).setPos(220, 348)


        # # Тексты сверху
        # scene.addText("Etho", font).setPos(250, 40)
        # scene.addText("Etho", font).setPos(550, 40)

        # # Дополнительные элементы между блоками
        # scene.addRect(300, 250, 50, 50, QPen(Qt.black, 2), QBrush(QColor(192, 192, 192)))
        # scene.addText("RTP", font).setPos(310, 260)
        #
        # scene.addRect(350, 300, 50, 50, QPen(Qt.black, 2), QBrush(QColor(192, 192, 192)))
        # scene.addText("SIP", font).setPos(360, 310)
        #
        # scene.addText("KUU-100", font).setPos(400, 350)
        #
        # # Треугольник KUU-100
        # polygon_kuu = QPolygonF([
        #     QPointF(450, 300),
        #     QPointF(500, 300),
        #     QPointF(475, 250)
        # ])
        # scene.addPolygon(polygon_kuu, QPen(Qt.black, 2), QBrush(QColor(192, 192, 192)))
        # scene.addText("KUU-100", font).setPos(460, 260)


    def get_schema_answer(self):
        file_name = '_'.join(self.lineEdit.text().split())
        file_name = 'schema_' + file_name + '.conf'
        with open(file_name, 'w') as f:
            fields_list = [self.lineEdit_5.text(), self.lineEdit_6.text(), self.lineEdit_7.text(),
                           self.lineEdit_8.text(), self.lineEdit_9.text(), self.lineEdit_10.text(),
                           self.lineEdit_11.text(), self.lineEdit_12.text(), self.lineEdit_13.text(),
                           self.lineEdit_14.text(), self.lineEdit_15.text(), self.lineEdit_16.text(),
                           self.lineEdit_33.text(), self.lineEdit_34.text(), self.lineEdit_35.text(),
                           self.lineEdit_36.text(), self.lineEdit_37.text(), self.lineEdit_38.text(),
                           self.lineEdit_39.text(), self.lineEdit_40.text(), self.lineEdit_41.text(),
                           self.lineEdit_42.text(), self.lineEdit_43.text(), self.lineEdit_44.text(), ]
            res_text = '\n'.join(fields_list)
            f.write(res_text)
        os.system(f'tftp {self.curr_ip} PUT {file_name}')
        os.remove(file_name)
        QMessageBox.information(self, "Информация", "Ответ отправлен на проверку!")

    def get_variant_scheme(self):
        filename_schema_etalon = 'scheme_etalon.txt'
        os.system(f'tftp {self.curr_ip} GET {filename_schema_etalon}')
        with open(filename_schema_etalon, 'r') as f_etalon:
            lines = [line.strip() for line in f_etalon.readlines()]
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
