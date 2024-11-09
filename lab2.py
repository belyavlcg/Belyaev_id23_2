import sys
import random
import configparser
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QTimer, Qt


class RainDrop:
    def __init__(self, x, y, length, speed, angle):
        self.x = x
        self.y = y
        self.length = length
        self.speed = speed
        self.angle = angle

    def move(self):
        self.y += self.speed
        self.x += self.speed * self.angle


class RainWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.drops = []

        self.color = QColor('#3498db')

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.movement_rain)
        self.timer.start(30)

        self.setWindowTitle("lab2")
        self.setGeometry(100, 100, 800, 600)

    def movement_rain(self):
        for _ in range(int(random.uniform(0, 5))):
            x = random.randint(0, self.width())
            y = 0
            length = random.uniform(5, 15)
            speed = random.uniform(2, 10)
            angle = random.uniform(-0.1, 0.1)

            new_drop = RainDrop(x, y, length, speed, angle)
            self.drops.append(new_drop)

        for drop in self.drops:
            drop.move()

        self.drops = [drop for drop in self.drops if drop.y < self.height()]

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(self.color)

        for drop in self.drops:
            painter.drawLine(int(drop.x), int(drop.y), int(drop.x + drop.length * drop.angle),
                             int(drop.y + drop.length))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RainWidget()
    window.show()
    sys.exit(app.exec_())


