# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c3.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DFAWindow(object):
    def setupUi(self, DFAWindow):
        DFAWindow.setObjectName("DFAWindow")
        DFAWindow.resize(1197, 853)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("cest.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        DFAWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(DFAWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 1091, 791))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("DFA.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        DFAWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DFAWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1197, 26))
        self.menubar.setObjectName("menubar")
        DFAWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DFAWindow)
        self.statusbar.setObjectName("statusbar")
        DFAWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DFAWindow)
        QtCore.QMetaObject.connectSlotsByName(DFAWindow)

    def retranslateUi(self, DFAWindow):
        _translate = QtCore.QCoreApplication.translate
        DFAWindow.setWindowTitle(_translate("DFAWindow", "DFA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DFAWindow = QtWidgets.QMainWindow()
    ui = Ui_DFAWindow()
    ui.setupUi(DFAWindow)
    DFAWindow.show()
    sys.exit(app.exec_())
