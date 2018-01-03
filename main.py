import sys
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QWidget
from start_window import Ui_Form
from minefield import Minefield
import time


class StartForm(Ui_Form):
    def __init__(self, form):
        self.setupUi(form)
        self.center(form)
        # self.ok_btn.clicked.connect(self.create_minefield)
        self.ok_btn.clicked.connect(lambda: self.crr(form))
        form.show()

    def crr(self, form):
        # form.hide()
        # time.sleep(2)

        self.minefield = Minefield()
        #self.minefield.setParent(self)
        self.minefield.show()

        #time.sleep(3)
        #form.show()

    def center(self, form):
        qr = form.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        form.move(qr.topLeft())

    def create_minefield(self):
        if self.easy_rbtn.isChecked():
            mode = 1
        elif self.medium_rbtn.isChecked():
            mode = 2
        elif self.hard_rbtn.isChecked():
            mode = 3
        elif self.custom_rbtn.isChecked():
            mode = 4
        else:
            mode = 5
        self.mode_lbl.setText(str(mode))

        minefield = Minefield()
        minefield.setParent(self)
        minefield.show()


def main():
    app = QApplication(sys.argv)
    widget = QWidget()
    start_form = StartForm(widget)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()