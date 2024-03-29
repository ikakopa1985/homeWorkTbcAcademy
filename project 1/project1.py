# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


from PyQt5.QtWidgets import QMessageBox 

username = '2020'
password = '2019'


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(669, 568)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 0, 641, 521))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.editUser = QtWidgets.QLineEdit(self.page1)
        self.editUser.setGeometry(QtCore.QRect(220, 251, 211, 41))
        self.editUser.setObjectName("editUser")
        self.submitButton = QtWidgets.QPushButton(self.page1)
        self.submitButton.setGeometry(QtCore.QRect(220, 420, 221, 41))
        self.submitButton.setObjectName("submitButton")
        self.editPass = QtWidgets.QLineEdit(self.page1)
        self.editPass.setGeometry(QtCore.QRect(222, 361, 221, 41))
        self.editPass.setObjectName("editPass")
        self.loginphoto = QtWidgets.QLabel(self.page1)
        self.loginphoto.setGeometry(QtCore.QRect(-10, 0, 661, 521))
        self.loginphoto.setText("")
        self.loginphoto.setPixmap(QtGui.QPixmap("media\\login1.jpg"))
        self.loginphoto.setObjectName("loginphoto")
        self.loginphoto.raise_()
        self.submitButton.raise_()
        self.editUser.raise_()
        self.editPass.raise_()
        self.stackedWidget.addWidget(self.page1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.singOutButton = QtWidgets.QPushButton(self.page_2)
        self.singOutButton.setGeometry(QtCore.QRect(260, 390, 111, 41))
        self.singOutButton.setObjectName("singOutButton")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(60, 70, 61, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(30, 0, 591, 401))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("media\\minion.jpg"))
        self.label_4.setObjectName("label_4")
        self.label_3.raise_()
        self.label_4.raise_()
        self.singOutButton.raise_()
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 669, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
    def singIn(self):
        if username != self.editUser.text()  or  password != self.editPass.text():
            self.message_box = QMessageBox(MainWindow)
            self.message_box.setWindowTitle("Warning")
            self.message_box.setIcon(QMessageBox.Warning)
            self.message_box.setText("Wrong Username or password")
            self.message_box.show()
        else:
            self.message_box = QMessageBox(MainWindow)
            self.message_box.setWindowTitle("Information")
            self.message_box.setIcon(QMessageBox.Information)
            self.message_box.setText("Wellcome Home")
            self.message_box.show()
            self.stackedWidget.setCurrentIndex(1)  
            
            
            #
    def singOut(self):
        self.stackedWidget.setCurrentIndex(0)  
        self.message_box = QMessageBox(MainWindow)
        self.message_box.setWindowTitle("Information")
        self.message_box.setIcon(QMessageBox.Information)
        self.message_box.setText("Good By")
        self.message_box.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.submitButton.setText(_translate("MainWindow", "Sing In"))
        self.singOutButton.setText(_translate("MainWindow", "Sing Out"))
        self.label_3.setText(_translate("MainWindow", "Wellcome "))
        self.submitButton.clicked.connect(self.singIn)   #
        self.singOutButton.clicked.connect(self.singOut)   #
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
