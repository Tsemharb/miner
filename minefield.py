from PyQt5.QtWidgets import QWidget, QApplication, QSizePolicy, \
                            QPushButton, QToolButton, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon
import sys
from random import shuffle

class Minefield(QWidget):
    def __init__(self, mode):
        super().__init__()
        self.mines_map = self.create_mines_map(mode)
        self.setWindowTitle('Minefield')
        self.vertical_layout = QVBoxLayout(self)
        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(0)
        self.create_field(mode)


    def create_field(self, mode):
        c = 1
        for x in range(mode[0]):
            for y in range(mode[1]):
                button = QToolButton(self)
                button.setObjectName(str(c))
                if self.mines_map[c-1] == 1:
                    button.setIcon(QIcon('mine.png'))
                size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                size_policy.setHorizontalStretch(1)
                size_policy.setHorizontalStretch(1)
                #size_policy.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
                button.setSizePolicy(size_policy)
                self.grid_layout.addWidget(button, x, y)
                c = c + 1


        self.close_btn = QPushButton('close', self)
        self.vertical_layout.addItem(self.grid_layout)
        self.vertical_layout.addWidget(self.close_btn)
        self.show()


    def create_mines_map(self, mode):
        clean_cells = [0 for x in range(mode[0] * mode[1] - mode[2])]
        mines = [1 for x in range(mode[2])]
        mines_map = (mines + clean_cells)
        shuffle(mines_map)
        return mines_map


if __name__ == '__main__':
    app = QApplication(sys.argv)
    minefield = Minefield()
    sys.exit(app.exec_())