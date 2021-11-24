import random

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
import sys
from PyQt5 import uic


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.squares = 3
        self.offset = 130
        self.max_dim = 120
        self.min_dim = 30
        self.flag = False
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            painter = QPainter()
            painter.begin(self)
            painter.setPen(QColor('yellow'))
            for i in range(self.squares):
                self.paint_circle(painter, i)
        self.flag = False

    def paint_circle(self, painter: QPainter, time):
        x, y = 60 + (time * self.offset), 60
        w = h = int(random.randint(self.min_dim, self.max_dim) // 2)
        painter.drawEllipse(x, y, w, h)


def except_hook(a, b, c):
    sys.__excepthook__(a, b, c)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    f = Window()
    f.show()
    sys.exit(app.exec_())



