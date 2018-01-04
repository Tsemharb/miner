from PyQt5.QtWidgets import QWidget, QApplication, QSizePolicy, \
                            QPushButton, QToolButton, QVBoxLayout, QGridLayout, QGraphicsView
from PyQt5.QtGui import QIcon, QPalette, QBrush, QColor, QMouseEvent
from PyQt5.QtCore import Qt, QEvent
import sys
import copy
from random import shuffle


class Minefield(QWidget):
    def __init__(self, mode):
        super().__init__()
        self.mines_map = self.create_mines_map(mode)
        self.game_map = copy.deepcopy(self.mines_map)
        self.setWindowTitle('Minefield')
        self.vertical_layout = QVBoxLayout(self)
        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(0)
        self.create_field(mode)

    def create_field(self, mode):
        self.buttons = []
        for x in range(mode[0]):
            buttons_row = []
            for y in range(mode[1]):
                button = QToolButton(self)
                button.installEventFilter(self)
                button.setObjectName(str(x) + ' ' + str(y))
                palette = QPalette()
                brush = QBrush(QColor(155, 155, 155))
                brush.setStyle(Qt.SolidPattern)
                palette.setBrush(QPalette.Active, QPalette.Button, brush)
                brush = QBrush(QColor(255, 255, 255))
                brush.setStyle(Qt.SolidPattern)
                palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
                button.setPalette(palette)
                button.clicked.connect(self.take_a_step)

                # if self.mines_map[x][y] == 1:
                #     button.setIcon(QIcon('mine.png'))
                size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                size_policy.setHorizontalStretch(1)
                size_policy.setHorizontalStretch(1)
                button.setSizePolicy(size_policy)
                self.grid_layout.addWidget(button, x, y)
                buttons_row.append(button)
            self.buttons.append(buttons_row)

        self.close_btn = QPushButton('close', self)
        self.vertical_layout.addItem(self.grid_layout)
        self.vertical_layout.addWidget(self.close_btn)
        self.show()

    def eventFilter(self, source, event):
        if event.type() == QEvent.MouseButtonPress:
            if event.button() == Qt.RightButton:
                self.toggle_a_flag(source)
        return super(Minefield, self).eventFilter(source, event)

    def take_a_step(self):
        sending_button = self.sender()
        sending_btn_coords = sending_button.objectName().split()
        if self.mines_map[int(sending_btn_coords[0])][int(sending_btn_coords[1])] == 1:
            self.behold_the_bombs()
            pass
        else:
            sending_button.setEnabled(False)


        print(sending_button.objectName().split())

    def behold_the_bombs(self):
        for x in range(len(self.mines_map)):
            for y in range(len(self.mines_map[0])):
                if self.mines_map[x][y] == 1:
                    self.buttons[x][y].setIcon(QIcon('mine.png'))

    def toggle_a_flag(self, source):
        if source.isEnabled():
            source_coords = source.objectName().split()
            if self.game_map[int(source_coords[0])][int(source_coords[1])] != 2:
                self.game_map[int(source_coords[0])][int(source_coords[1])] = 2
                source.setIcon(QIcon('flag.png'))
            else:
                self.game_map[int(source_coords[0])][int(source_coords[1])] = self.mines_map[int(source_coords[0])][int(source_coords[1])]
                source.setIcon(QIcon(None))

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