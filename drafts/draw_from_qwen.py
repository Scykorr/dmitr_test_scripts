import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QVBoxLayout, QWidget
from PyQt5.QtGui import QPen, QBrush, QColor, QPainter, QPolygonF, QFont
from PyQt5.QtCore import Qt, QPointF

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Установка заголовка окна
        self.setWindowTitle("Diagram Drawing with PyQt5")
        self.setGeometry(100, 100, 800, 600)

        # Создание центрального виджета
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Создание вертикального компоновщика
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Создание сцены
        scene = QGraphicsScene(self)
        scene.setSceneRect(0, 0, 800, 600)  # Размер сцены

        # Создание представления
        view = QGraphicsView(scene)
        view.setRenderHint(QPainter.Antialiasing)  # Улучшение качества отрисовки
        layout.addWidget(view)

        # Определение стилей
        self.black_pen = QPen(Qt.black, 2)
        self.gray_brush = QBrush(QColor(192, 192, 192))

        # Рисование блоков
        self.draw_block(scene, 50, 100, "UATC", "ΔX-500С", "IP-ATC", "T-76С", "E+H1", "S", "M")
        self.draw_block(scene, 350, 100, "UATC", "ΔX-500С", "IP-ATC", "T-76С", "E+H1", "S", "M")
        self.draw_block(scene, 650, 100, "UATC", "ΔX-500С", "IP-ATC", "T-76С", "E+H1", "S", "M")

        # Добавление дополнительных элементов
        self.draw_additional_elements(scene)

    def draw_block(self, scene, x, y, bottom_text, bottom_left_text, middle_text, top_text, top_right_text, s_label, m_label):
        """
        Рисует один блок с заданными параметрами.
        """
        # Прямоугольник UATC
        uatc_rect = scene.addRect(x, y + 200, 150, 100, self.black_pen, self.gray_brush)
        uatc_text = scene.addText(bottom_text, QFont("Arial", 12))
        uatc_text.setPos(x + 20, y + 250)

        # Треугольник M
        polygon_m = QPolygonF([
            QPointF(x - 50, y + 200),
            QPointF(x + 100, y + 200),
            QPointF(x + 25, y + 100)
        ])
        m_triangle = scene.addPolygon(polygon_m, self.black_pen, self.gray_brush)
        m_text = scene.addText(m_label, QFont("Arial", 12))
        m_text.setPos(x + 50, y + 120)

        # Прямоугольник IP-ATC
        ip_atc_rect = scene.addRect(x + 150, y + 100, 150, 100, self.black_pen, self.gray_brush)
        ip_atc_text = scene.addText(middle_text, QFont("Arial", 12))
        ip_atc_text.setPos(x + 170, y + 150)

        # Треугольник S
        polygon_s = QPolygonF([
            QPointF(x + 150, y + 100),
            QPointF(x + 300, y + 100),
            QPointF(x + 225, y + 200)
        ])
        s_triangle = scene.addPolygon(polygon_s, self.black_pen, self.gray_brush)
        s_text = scene.addText(s_label, QFont("Arial", 12))
        s_text.setPos(x + 225, y + 120)

        # Треугольник E+H1
        polygon_eh1 = QPolygonF([
            QPointF(x + 150, y + 100),
            QPointF(x + 150, y),
            QPointF(x + 225, y + 50)
        ])
        eh1_triangle = scene.addPolygon(polygon_eh1, self.black_pen, self.gray_brush)
        eh1_text = scene.addText(top_right_text, QFont("Arial", 12))
        eh1_text.setPos(x + 160, y + 20)

        # Текст T-76С
        t_76c_text = scene.addText(top_text, QFont("Arial", 12))
        t_76c_text.setPos(x + 170, y + 120)

        # Текст ΔX-500С
        dx_500c_text = scene.addText(bottom_left_text, QFont("Arial", 12))
        dx_500c_text.setPos(x + 20, y + 300)

    def draw_additional_elements(self, scene):
        """
        Рисует дополнительные элементы: линии, тексты и другие фигуры.
        """
        # Линии сверху
        line_top_left = scene.addLine(50, 50, 300, 50, self.black_pen)
        line_top_right = scene.addLine(350, 50, 600, 50, self.black_pen)

        # Тексты сверху
        etho_text_left = scene.addText("Etho", QFont("Arial", 12))
        etho_text_left.setPos(250, 40)
        etho_text_right = scene.addText("Etho", QFont("Arial", 12))
        etho_text_right.setPos(550, 40)

        # Дополнительные элементы между блоками
        additional_rect = scene.addRect(300, 250, 50, 50, self.black_pen, self.gray_brush)
        additional_text = scene.addText("RTP", QFont("Arial", 12))
        additional_text.setPos(310, 260)

        sip_rect = scene.addRect(350, 300, 50, 50, self.black_pen, self.gray_brush)
        sip_text = scene.addText("SIP", QFont("Arial", 12))
        sip_text.setPos(360, 310)

        kuu_100_text = scene.addText("KUU-100", QFont("Arial", 12))
        kuu_100_text.setPos(400, 350)

        # Треугольник KUU-100
        polygon_kuu_100 = QPolygonF([
            QPointF(450, 300),
            QPointF(500, 300),
            QPointF(475, 250)
        ])
        kuu_100_triangle = scene.addPolygon(polygon_kuu_100, self.black_pen, self.gray_brush)
        kuu_100_text = scene.addText("KUU-100", QFont("Arial", 12))
        kuu_100_text.setPos(460, 260)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())