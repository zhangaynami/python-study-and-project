# -*- codeing = utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()

    #窗口标题
    w.setWindowTitle("第一个程序")
    #暂时窗口
    w.show()
    #程序循环等待
    app.exec_()