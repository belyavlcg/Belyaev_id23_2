import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt, QTimer, QPointF


class Circle(QWidget):
    def __init__(self, change_angle=0.05):
        super().__init__()
        self.title = "Lab1"
        self.top = 150
        self.left = 150
        self.width = 600
        self.height = 600
        self.radius = 200
        self.angle = 0
        self.change_angle = change_angle
        self.init_window()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.change_position)
        self.timer.start(50)

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def change_position(self):
        self.angle += self.change_angle
        if self.angle >= 2 * math.pi:
            self.angle = 0
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setPen(QPen(Qt.black, 8, Qt.SolidLine))
        painter.drawEllipse(100, 100, 2 * self.radius, 2 * self.radius)

        x = self.width // 2 + self.radius * math.cos(self.angle)
        y = self.height // 2 + self.radius * math.sin(self.angle)

        painter.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
        painter.setPen(QPen(Qt.blue, 8, Qt.SolidLine))
        painter.drawEllipse(QPointF(x, y), 10, 10)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Circle(change_angle=0.05)
    sys.exit(app.exec())
