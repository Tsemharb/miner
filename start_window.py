# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(170, 198)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(9, 10, 148, 176))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.easy_rbtn = QtWidgets.QRadioButton(self.widget)
        self.easy_rbtn.setObjectName("easy_rbtn")
        self.verticalLayout.addWidget(self.easy_rbtn)
        self.medium_rbtn = QtWidgets.QRadioButton(self.widget)
        self.medium_rbtn.setObjectName("medium_rbtn")
        self.verticalLayout.addWidget(self.medium_rbtn)
        self.hard_rbtn = QtWidgets.QRadioButton(self.widget)
        self.hard_rbtn.setObjectName("hard_rbtn")
        self.verticalLayout.addWidget(self.hard_rbtn)
        self.custom_rbtn = QtWidgets.QRadioButton(self.widget)
        self.custom_rbtn.setObjectName("custom_rbtn")
        self.verticalLayout.addWidget(self.custom_rbtn)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.ok_btn = QtWidgets.QPushButton(self.widget)
        self.ok_btn.setMaximumSize(QtCore.QSize(167, 40))
        self.ok_btn.setObjectName("ok_btn")
        self.verticalLayout_2.addWidget(self.ok_btn)
        self.mode_lbl = QtWidgets.QLabel(self.widget)
        self.mode_lbl.setText("")
        self.mode_lbl.setObjectName("mode_lbl")
        self.verticalLayout_2.addWidget(self.mode_lbl)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.easy_rbtn.setText(_translate("Form", "8x8, 16 mines"))
        self.medium_rbtn.setText(_translate("Form", "16x16, 40 mines"))
        self.hard_rbtn.setText(_translate("Form", "30x16, 99 mines"))
        self.custom_rbtn.setText(_translate("Form", "custom"))
        self.ok_btn.setText(_translate("Form", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

