import sys
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QWidget, QMessageBox, QGraphicsView
from start_window import Ui_Form
from minefield import Minefield
import time


class StartForm(Ui_Form):
    def __init__(self, form):
        self.setupUi(form)
        self.center(form)
        # self.ok_btn.clicked.connect(self.create_minefield)
        self.ok_btn.clicked.connect(lambda: self.create_minefield(form))
        form.show()

    def center(self, form):
        qr = form.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        form.move(qr.topLeft())

    def create_minefield(self, form):
        if self.easy_rbtn.isChecked():
            mode = (8, 8, 16)
        elif self.medium_rbtn.isChecked():
            mode = (16, 16, 40)
        elif self.hard_rbtn.isChecked():
            mode = (16, 30, 99)
        elif self.custom_rbtn.isChecked():
            mode = 4
        else:
            mode = 5

        if mode == 5:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText("Please, select the mode")
            self.msg.setStandardButtons(QMessageBox.Ok)
            self.msg.exec_()
        elif mode == 4:
            pass
        else:
            form.hide()
            self.minefield = Minefield(mode)
            self.minefield.close_btn.clicked.connect(lambda: self.destroy_minefield(form))
            self.minefield.show()

    def destroy_minefield(self, form):
        #self.minefield.setParent(None)
        del self.minefield
        form.show()


def main():
    app = QApplication(sys.argv)
    widget = QWidget()
    start_form = StartForm(widget)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()