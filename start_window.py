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
        Form.resize(254, 263)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 10, 231, 239))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.easy_rbtn = QtWidgets.QRadioButton(self.layoutWidget)
        self.easy_rbtn.setObjectName("easy_rbtn")
        self.verticalLayout.addWidget(self.easy_rbtn)
        self.medium_rbtn = QtWidgets.QRadioButton(self.layoutWidget)
        self.medium_rbtn.setObjectName("medium_rbtn")
        self.verticalLayout.addWidget(self.medium_rbtn)
        self.hard_rbtn = QtWidgets.QRadioButton(self.layoutWidget)
        self.hard_rbtn.setObjectName("hard_rbtn")
        self.verticalLayout.addWidget(self.hard_rbtn)
        self.custom_rbtn = QtWidgets.QRadioButton(self.layoutWidget)
        self.custom_rbtn.setObjectName("custom_rbtn")
        self.verticalLayout.addWidget(self.custom_rbtn)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.ok_btn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok_btn.sizePolicy().hasHeightForWidth())
        self.ok_btn.setSizePolicy(sizePolicy)
        self.ok_btn.setObjectName("ok_btn")
        self.verticalLayout_2.addWidget(self.ok_btn, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.easy_rbtn.setText(_translate("Form", "&8x8, 16 mines"))
        self.medium_rbtn.setText(_translate("Form", "&16x16, 40 mines"))
        self.hard_rbtn.setText(_translate("Form", "16x30, &99 mines"))
        self.custom_rbtn.setText(_translate("Form", "&custom"))
        self.ok_btn.setText(_translate("Form", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

