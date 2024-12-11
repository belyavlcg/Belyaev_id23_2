import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QPushButton, QSpinBox, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer, QPoint, Qt
from PyQt5.QtGui import QPainter, QColor, QBrush


class Particle:
    def __init__(self, x, y, radius, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = random.uniform(-speed, speed)
        self.speed_y = random.uniform(-speed, speed)

    def move(self, width, height):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x <= 0 or self.x >= width:
            self.speed_x *= -1
        if self.y <= 0 or self.y >= height:
            self.speed_y *= -1


class ParticleSimulation(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Симуляция хаотического движения частиц")
        self.setGeometry(100, 100, 800, 600)

        self.particles = []

        self.init_ui()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_simulation)

    def init_ui(self):
        layout = QVBoxLayout()

        self.count_slider = QSlider(Qt.Horizontal)
        self.count_slider.setMinimum(1)
        self.count_slider.setMaximum(100)
        self.count_slider.setValue(10)
        layout.addWidget(QLabel("Количество частиц:"))
        layout.addWidget(self.count_slider)

        self.speed_slider = QSlider(Qt.Horizontal)
        self.speed_slider.setMinimum(1)
        self.speed_slider.setMaximum(10)
        self.speed_slider.setValue(5)
        layout.addWidget(QLabel("Скорость частиц:"))
        layout.addWidget(self.speed_slider)

        self.radius_spinbox = QSpinBox()
        self.radius_spinbox.setMinimum(1)
        self.radius_spinbox.setMaximum(20)
        self.radius_spinbox.setValue(5)
        layout.addWidget(QLabel("Радиус частиц:"))
        layout.addWidget(self.radius_spinbox)

        self.start_button = QPushButton("Запустить анимацию")
        self.start_button.clicked.connect(self.start_animation)
        layout.addWidget(self.start_button)

        self.reset_button = QPushButton("Сбросить")
        self.reset_button.clicked.connect(self.reset_simulation)
        layout.addWidget(self.reset_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def paintEvent(self, event):
        painter = QPainter(self)
        for particle in self.particles:
            painter.setBrush(QBrush(QColor(0, 0, 255)))
            painter.drawEllipse(QPoint(int(particle.x), int(particle.y)), particle.radius, particle.radius)

    def update_simulation(self):
        for particle in self.particles:
            particle.move(self.width(), self.height())
        self.update()

    def start_animation(self):
        count = self.count_slider.value()
        speed = self.speed_slider.value()
        radius = self.radius_spinbox.value()

        for _ in range(count):
            x = random.randint(radius, self.width() - radius)
            y = random.randint(radius, self.height() - radius)
            self.particles.append(Particle(x, y, radius, speed))

        self.timer.start(50)

    def reset_simulation(self):
        self.particles.clear()
        self.timer.stop()
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    simulation = ParticleSimulation()
    simulation.show()
    sys.exit(app.exec_())
