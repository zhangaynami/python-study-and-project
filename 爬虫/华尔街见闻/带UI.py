# -*- codeing = utf-8 -*-
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton
import sys
import requests

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('My Crawler')
        self.setGeometry(100, 100, 400, 300)

        # 创建输入框和标签
        self.url_label = QLabel('Enter URL:', self)
        self.url_label.move(20, 20)
        self.url_edit = QLineEdit(self)
        self.url_edit.move(120, 20)
        self.url_edit.resize(250, 20)

        # 创建“爬取”按钮
        self.crawl_button = QPushButton('Crawl', self)
        self.crawl_button.move(20, 50)
        self.crawl_button.clicked.connect(self.crawl)

        # 创建文本框用于显示结果
        self.result_edit = QTextEdit(self)
        self.result_edit.move(20, 80)
        self.result_edit.resize(360, 200)

    def crawl(self):
        url = self.url_edit.text()
        # 爬虫代码
        response = requests.get(url)
        # 处理爬虫结果
        self.result_edit.setText(response.text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())