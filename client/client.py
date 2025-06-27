import pathlib
import os
from types import NoneType

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QBrush, QColor, QPen, QFont, QPolygonF
from PyQt5.QtWidgets import QGraphicsScene

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
        self.change_size(341, 300)
        self.setupUi(self)
        self.setWindowTitle('Клиент тестирования')
        self.lineEdit_2.setText('127.0.0.1')
        self.curr_ip = self.lineEdit_2.text()
        self.pushButton_2.clicked.connect(lambda: self.choose_operator(page_index=1))
        self.pushButton.clicked.connect(lambda: self.choose_operator(page_index=2))
        self.lineEdit.setText('')
        self.lineEdit_4.setText('1.conf')
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
            self.change_size(1450, 511)
            self.stackedWidget.setCurrentIndex(page_index)
            standard_num = self.lineEdit_4.text().split('.conf')[0]
            if standard_num == '1':
                self.textEdit.append('SYSTEM {')
                self.textEdit.append('	HOSTNAME=ip_ats_2')
                self.textEdit.append('}')
                self.textEdit.append('NETWORK {')
                self.textEdit.append('	IFACE {')
                self.textEdit.append('		IFACE_NAME=eth1')
                self.textEdit.append('		IP=172.16.2.1')
                self.textEdit.append('		NETMASK=255.255.255.0')
                self.textEdit.append('	}')
                self.textEdit.append('	ROUTE {')
                self.textEdit.append('		DEFAULT_GW=true')
                self.textEdit.append('		GATEWAY=172.16.2.2')
                self.textEdit.append('		NETMASK=255.255.255.0')
                self.textEdit.append('		IFACE_NAME=eth1')
                self.textEdit.append('	}')
                self.textEdit.append('}')
                self.textEdit.append('IPTABLES {')
                self.textEdit.append('	FORWARD {')
                self.textEdit.append('		ACTION=ACCEPT')
                self.textEdit.append('	}')
                self.textEdit.append('	INPUT {')
                self.textEdit.append('		ACTION=ACCEPT')
                self.textEdit.append('	}')
                self.textEdit.append('	OUTPUT {')
                self.textEdit.append('		ACTION=ACCEPT')
                self.textEdit.append('	}')
                self.textEdit.append('	PREROUTING {')
                self.textEdit.append('		ACTION=ACCEPT')
                self.textEdit.append('	}')
                self.textEdit.append('	POSTROUTING {')
                self.textEdit.append('		ACTION=ACCEPT')
                self.textEdit.append('	}')
                self.textEdit.append('}')
                self.textEdit.append('IAX {')
                self.textEdit.append('	GENERAL {')
                self.textEdit.append('		BANDWIDTH="low"')
                self.textEdit.append('		JITTERBUFFER=false')
                self.textEdit.append('		FORCEJITTERBUFFER=false')
                self.textEdit.append('		AUTOKILL=true')
                self.textEdit.append('		BINDADDR=172.16.2.1')
                self.textEdit.append('	}')
                self.textEdit.append('	IAX_ROUTE {')
                self.textEdit.append('		NAME="ip_ats_1"')
                self.textEdit.append('		TYPE="friend"')
                self.textEdit.append('		HOST="172.16.1.1"')
                self.textEdit.append('		CONTEXT="main"')
                self.textEdit.append('		TRUNK=true')
                self.textEdit.append('		ALLOW="alaw"')
                self.textEdit.append('		ALLOW="gsm"')
                self.textEdit.append('		ALLOW="ulaw"')
                self.textEdit.append('	}')
                self.textEdit.append('}')
                self.textEdit.append('SIP {')
                self.textEdit.append('	GENERAL {')
                self.textEdit.append('		CONTEXT="main"')
                self.textEdit.append('		BINDPORT=5060')
                self.textEdit.append('		BINDADDR=0.0.0.0')
                self.textEdit.append('		ALLOWOVERLAP=false')
                self.textEdit.append('		SRVLOOKUP=true')
                self.textEdit.append('		DISALLOW="all"')
                self.textEdit.append('		ALLOW="alaw"')
                self.textEdit.append('		ALLOW="ulaw"')
                self.textEdit.append('		ALLOW="g729"')
                self.textEdit.append('	}')
                self.textEdit.append('	PHONE {')
                self.textEdit.append('		TYPE="friend"')
                self.textEdit.append('		CONTEXT="main"')
                self.textEdit.append('		HOST="172.16.1.1"')
                self.textEdit.append('		NUMBER=1')
                self.textEdit.append('	}')
                self.textEdit.append('}')
                self.textEdit.append('ZAPTEL {')
                self.textEdit.append('	LOADZONE="ru"')
                self.textEdit.append('	DEFAULTZONE="ru"')
                self.textEdit.append('	FXOKS="63-110"')
                self.textEdit.append('	CHAN_E1 {')
                self.textEdit.append('		SPAN {')
                self.textEdit.append('			NUMBER=1')
                self.textEdit.append('			TIMING=1')
                self.textEdit.append('			LBO=0')
                self.textEdit.append('			FRAMING="ccs"')
                self.textEdit.append('			CODING="hdb3"')
                self.textEdit.append('		}')
                self.textEdit.append('		BCHAN="1-15,17-31"')
                self.textEdit.append('		HARDHDLC=16')
                self.textEdit.append('		SPAN {')
                self.textEdit.append('			NUMBER=2')
                self.textEdit.append('			TIMING=0')
                self.textEdit.append('			LBO=0')
                self.textEdit.append('			FRAMING="ccs"')
                self.textEdit.append('			CODING="hdb3"')
                self.textEdit.append('		}')
                self.textEdit.append('		BCHAN="32-46,48-62"')
                self.textEdit.append('		HARDHDLC=47')
                self.textEdit.append('	}')
                self.textEdit.append('}')
                self.textEdit.append('ZAPATA {')
                self.textEdit.append('	CONTEXT="main"')
                self.textEdit.append('	SWITCHTYPE="national"')
                self.textEdit.append('	ECHOCANCEL=true')
                self.textEdit.append('	ECHOCANCELWHENBRIDGED=true')
                self.textEdit.append(' OVERLAPDIAL=true')
                self.textEdit.append('	CHAN {')
                self.textEdit.append('		CONTEXT="main"')
                self.textEdit.append('		GROUP=3')
                self.textEdit.append('		SIGNALLING="fxo_ks"')
                self.textEdit.append('		CHANNEL="63-110"')
                self.textEdit.append('	}')
                self.textEdit.append('	CHAN {')
                self.textEdit.append('		CONTEXT="main"')
                self.textEdit.append('		GROUP=1')
                self.textEdit.append('		SIGNALLING="pri_cpe"')
                self.textEdit.append('		CHANNEL="1-15,17-31"')
                self.textEdit.append('	}')
                self.textEdit.append('	CHAN {')
                self.textEdit.append('		CONTEXT="main"')
                self.textEdit.append('		GROUP=2')
                self.textEdit.append('		SIGNALLING="pri_net"')
                self.textEdit.append('		CHANNEL="32-46,48-62"')
                self.textEdit.append('	}')
                self.textEdit.append('	CHAN {')
                self.textEdit.append('		 CONTEXT="main"')
                self.textEdit.append('         SIGNALLING="fxo_ks"')
                self.textEdit.append('         CALLERID=61921')
                self.textEdit.append('         CHANNEL="63"')
                self.textEdit.append('		}')
                self.textEdit.append('  CHAN {')
                self.textEdit.append('         CONTEXT="main"')
                self.textEdit.append('         SIGNALLING="fxo_ks"')
                self.textEdit.append('         CALLERID=61922')
                self.textEdit.append('         CHANNEL="64"')
                self.textEdit.append('		}')
                self.textEdit.append('}')
                self.textEdit.append('EXTENSIONS {')
                self.textEdit.append('	GENERAL {')
                self.textEdit.append('		STATIC=true')
                self.textEdit.append('		WRITEPROTECT=false')
                self.textEdit.append('		CLEARGLOBALVARS=false')
                self.textEdit.append('	}')
                self.textEdit.append('	EXTENGROUP {')
                self.textEdit.append('		NAME="main"')
                self.textEdit.append('		EXTEN="61921:Zap/63::"')
                self.textEdit.append('		EXTEN="61922:Zap/64::"')
                self.textEdit.append('		EXTEN="_619XX:IAX2/ip_ats_1::"')
                self.textEdit.append('		EXTEN="_619XX:SIP/1::"')
                self.textEdit.append('		EXTEN="_619XX:Zap/g1::"')
                self.textEdit.append('		}')
                self.textEdit.append('}')

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

    def draw_block(self, scene, x, y, bottom_text, bottom_left_text, middle_text, top_text, top_right_text, s_label,
                   m_label):
        from PyQt5.QtGui import QPolygonF

        font = QFont("Arial", 12)

        # Прямоугольник IAD
        scene.addRect(x, y + 360, 100, 50, QPen(Qt.black, 2), QBrush(QColor(192, 192, 192)))
        scene.addText(bottom_text, font).setPos(x + 30, y + 410)

        # Треугольник M
        polygon_m = QPolygonF([
            QPointF(x - 150, y + 370),
            QPointF(x - 90, y + 370),
            QPointF(x - 120, y + 320)
        ])
        scene.addPolygon(polygon_m, QPen(Qt.black, 2), QBrush(QColor(192, 192, 192)))
        scene.addText(m_label, font).setPos(x - 110, y + 320)
        scene.addText(bottom_left_text, font).setPos(x - 150, y + 370)

        # Треугольник S
        polygon_s = QPolygonF([
            QPointF(x - 90, y + 200),
            QPointF(x - 30, y + 200),
            QPointF(x - 60, y + 150)
        ])
        scene.addPolygon(polygon_s, QPen(Qt.black, 2), QBrush(QColor(192, 192, 192)))
        scene.addText(s_label, font).setPos(x - 110, y + 180)
        scene.addText(middle_text, font).setPos(x - 90, y + 200)
        scene.addText("Eth0", font).setPos(-60, 130)

        # овал сеть
        scene.addEllipse(x + 70, y + 130, 100, 50, QPen(Qt.black, 2), QBrush(QColor(192, 192, 192)))

        # Треугольник S1
        polygon_s1 = QPolygonF([
            QPointF(x + 290, y + 200),
            QPointF(x + 230, y + 200),
            QPointF(x + 260, y + 150)
        ])
        scene.addPolygon(polygon_s1, QPen(Qt.black, 2), QBrush(QColor(192, 192, 192)))
        scene.addText(s_label, font).setPos(x + 290, y + 170)
        scene.addText(middle_text, font).setPos(x + 230, y + 200)
        scene.addText("Eth0", font).setPos(210, 130)

        # Треугольник M1
        polygon_m1 = QPolygonF([
            QPointF(x + 450, y + 300),
            QPointF(x + 390, y + 300),
            QPointF(x + 420, y + 250)
        ])
        scene.addPolygon(polygon_m1, QPen(Qt.black, 2), QBrush(QColor(192, 192, 192)))
        scene.addText(m_label, font).setPos(x + 435, y + 250)
        scene.addText(bottom_left_text, font).setPos(x + 390, y + 300)

        # Треугольник DX 500C
        polygon_ksh = QPolygonF([
            QPointF(x + 300, y + 400),
            QPointF(x + 240, y + 400),
            QPointF(x + 270, y + 350)
        ])
        scene.addPolygon(polygon_ksh, QPen(Qt.black, 2), QBrush(QColor(192, 192, 192)))
        scene.addText('DX-500С', font).setPos(x + 240, y + 400)

        # Прямоугольник КШ-100
        scene.addRect(x + 180, y + 350, 25, 50, QPen(Qt.black, 2), QBrush(QColor(192, 192, 192)))
        scene.addText('КШ-100', font).setPos(x + 160, y + 400)

        # Прямоугольник маршрутизатор
        scene.addRect(x + 160, y + 250, 60, 30, QPen(Qt.black, 2), QBrush(QColor(192, 192, 192)))
        new_font = QFont("Arial", 16)
        scene.addText('→\n←', font).setPos(x + 180, y + 240)

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

        # Линии
        # M-S
        scene.addLine(-120, 320, -120, 170, QPen(Qt.black, 2))
        scene.addLine(-120, 170, -73, 170, QPen(Qt.black, 2))
        scene.addText("E1", font).setPos(-115, 140)


        # S-IA
        scene.addLine(-38, 185, 50, 185, QPen(Qt.black, 2))
        scene.addLine(50, 185, 50, 360, QPen(Qt.black, 2))
        scene.addText("Eth1", font).setPos(-30, 160)
        scene.addText("Eth1", font).setPos(10, 250)

        # S-Network
        scene.addLine(-53, 160, 70, 160, QPen(Qt.black, 2))

        # Network-S1
        scene.addLine(170, 160, 255, 160, QPen(Qt.black, 2))

        # S1-M1
        scene.addLine(269, 160, 420, 160, QPen(Qt.black, 2))
        scene.addLine(420, 160, 420, 250, QPen(Qt.black, 2))
        scene.addText("E1", font).setPos(350, 130)

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

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    w = MainClass()
    w.show()

    sys.exit(app.exec_())
