from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
import sys

class Minefield(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Second window')
        self.setGeometry(100,100,100,100)
        btn = QPushButton('try', self)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    minefield = Minefield()
    sys.exit(app.exec_())