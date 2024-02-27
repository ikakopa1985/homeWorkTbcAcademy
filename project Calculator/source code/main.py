import sys
import os
import math
import time
from PyQt5.QtWidgets import QMessageBox 

os.system("pyuic5 calculator.ui -o design.py")

from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from design import Ui_MainWindow



class MainWidget(QtWidgets.QMainWindow, Ui_MainWindow):
    def calculateFunction(self):
        self.errorLabel.setText('')
        try:
            if shape_name == 'wre':
                r1 = eval(self.r1.text())
                if r1 > 0:
                    area = (round((3.14 * r1 * r1) ,2 ))
                    self.lcd_r_area.display(area)
                    length = (round(( 2 * 3.14 * r1) ,2 ))
                    self.lcd_r_perimeter.display(length)
                else:
                    raise Exception("შეიყვანეთ მონაცემები სწორად" )
            if shape_name == 'samkutxedi':
                a = self.s1.value()
                b = self.s2.value()
                c = self.s3.value()
                if a == 0 or b == 0 or c == 0:
                    raise Exception("შეიყვანეთ მონაცემები სწორად" )
                else:
                    s = (a + b + c) / 2
                    area = round(math.sqrt(s * (s - a) * (s - b) * (s - c)),2)
                    self.lcd_s_area.display(area)
                    self.lcd_s_perimeter.display(a + b + c)
            if shape_name == 'trapecia':
                a, b, c, d = self.st1.value(),self.st2.value(),self.st3.value(),self.st4.value()  
                if a == 0 or b == 0 or c == 0 or d == 0:
                    raise Exception("შეიყვანეთ მონაცემები სწორად" )
                else:
                    base1 = min(a, b)
                    base2 = max(a, b) if a != base1 else max(c, d)
                    h = ((c ** 2) - ((base2 - base1) ** 2) + (d ** 2)) / (2 * (c - (base2 - base1)))
                    area = 0.5 * (base1 + base2) * h
                    self.lcd_tr_area.display(area)
                    self.lcd_tr_perimeter.display(a + b + c + d)
            if shape_name == 'kvadrati':
                s = self.s_kv.value()
                if s == 0:
                    raise Exception("შეიყვანეთ მონაცემები სწორად" )
                else:
                    self.lcd_kv_area.display(s * s)
                    self.lcd_kv_perimeter.display(s * 4)
        except Exception as e:
            print(" error :", e)
            self.errorLabel.setStyleSheet("color: red;")
            self.errorLabel.setText(str(e))
            
            

    
    def backFunc(self):
        self.errorLabel.setText('')
        self.stackedWidget.setCurrentWidget(self.main)
        self.calculate.setEnabled(False)

    def __init__(self):
        super().__init__()
        loadUi('calculator.ui', self)
        self.setupUi(self)
        self.stackedWidget.setCurrentWidget(self.main)
        self.select.clicked.connect(self.select_shape)
        self.back.clicked.connect(self.backFunc)
        self.calculate.clicked.connect(self.calculateFunction)

    def select_shape(self):
        global shape_name
        shape_name = self.shape_group.checkedButton().objectName()
        self.stackedWidget.setCurrentWidget(
            getattr(self, f'{shape_name}_page', self.main)
        )
        self.calculate.setEnabled(True)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWidget()
    window.show()

    sys.exit(app.exec_())
