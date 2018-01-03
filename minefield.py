from PyQt5.QtWidgets import QWidget, QApplication, QSizePolicy, \
                            QPushButton, QToolButton, QVBoxLayout, QGridLayout, QGraphicsView
from PyQt5.QtGui import QIcon, QMouseEvent
from PyQt5.QtCore import Qt, QEvent
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
        for x in range(mode[0]):
            for y in range(mode[1]):
                button = QToolButton(self)
                button.installEventFilter(self)
                button.setObjectName(str([x,y]))
                button.clicked.connect(self.take_a_step)

                button.setContextMenuPolicy(Qt.PreventContextMenu)
                button.customContextMenuRequested.connect(self.put_a_flag)
                if self.mines_map[x][y] == 1:
                    button.setIcon(QIcon('mine.png'))
                size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                size_policy.setHorizontalStretch(1)
                size_policy.setHorizontalStretch(1)
                button.setSizePolicy(size_policy)
                self.grid_layout.addWidget(button, x, y)

        self.close_btn = QPushButton('close', self)
        self.vertical_layout.addItem(self.grid_layout)
        self.vertical_layout.addWidget(self.close_btn)
        self.show()

    def eventFilter(self, source, event):
        if event.type() == QEvent.MouseButtonPress:
            if event.button() == Qt.RightButton:
                self.put_a_flag(source)
        return super(Minefield, self).eventFilter(source, event)

    def take_a_step(self):
        sending_button = self.sender()
        print(sending_button)
        print(sending_button.objectName())

    def put_a_flag(self, source):
        source.setIcon(QIcon('flag.png'))

    def create_mines_map(self, mode):
        clean_cells = [0 for x in range(mode[0] * mode[1] - mode[2])]
        mines = [1 for x in range(mode[2])]
        mines_list = (mines + clean_cells)
        shuffle(mines_list)
        mines_map = []
        for x in range(mode[0]):
            mines_row = mines_list[mode[1]*x: mode[1]*(x+1): 1]
            mines_map.append(mines_row)
            # print(mines_map)
        return mines_map


# class GraphicsView(QGraphicsView):
#     def mousePressEvent(self, event: QMouseEvent):
#         if event.button() == Qt.RightButton:
#             print('gotcha!!')
#         super(GraphicsView, self).mousePressEvent(event)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    minefield = Minefield()
    sys.exit(app.exec_())