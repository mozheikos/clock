# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_clock(object):
    def setupUi(self, clock):
        clock.setObjectName("clock")
        clock.resize(200, 70)
        clock.setMinimumSize(QtCore.QSize(200, 70))
        clock.setMaximumSize(QtCore.QSize(200, 70))
        clock.setWindowOpacity(1.0)
        clock.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(clock)
        self.centralwidget.setObjectName("centralwidget")
        self.time_screen = QtWidgets.QLabel(self.centralwidget)
        self.time_screen.setGeometry(QtCore.QRect(0, 30, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Ani")
        font.setPointSize(24)
        self.time_screen.setFont(font)
        self.time_screen.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(78, 154, 6);")
        self.time_screen.setFrameShape(QtWidgets.QFrame.Box)
        self.time_screen.setFrameShadow(QtWidgets.QFrame.Plain)
        self.time_screen.setLineWidth(0)
        self.time_screen.setTextFormat(QtCore.Qt.AutoText)
        self.time_screen.setScaledContents(True)
        self.time_screen.setAlignment(QtCore.Qt.AlignCenter)
        self.time_screen.setObjectName("time_screen")
        self.date_screen = QtWidgets.QLabel(self.centralwidget)
        self.date_screen.setGeometry(QtCore.QRect(0, 0, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.date_screen.setFont(font)
        self.date_screen.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(78, 154, 6);")
        self.date_screen.setAlignment(QtCore.Qt.AlignCenter)
        self.date_screen.setObjectName("date_screen")
        clock.setCentralWidget(self.centralwidget)

        self.retranslateUi(clock)
        QtCore.QMetaObject.connectSlotsByName(clock)

    def retranslateUi(self, clock):
        _translate = QtCore.QCoreApplication.translate
        clock.setWindowTitle(_translate("clock", "clock"))
        self.time_screen.setText(_translate("clock", "00:00:00"))
        self.date_screen.setText(_translate("clock", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    clock = QtWidgets.QMainWindow()
    ui = Ui_clock()
    ui.setupUi(clock)
    clock.show()
    sys.exit(app.exec_())
