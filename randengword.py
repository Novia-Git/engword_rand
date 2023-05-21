from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QLabel,QMainWindow,QListWidgetItem
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtGui import QDesktopServices, QFont
import random
import pandas as pd


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.labels = []
        for _ in range(20):
            label = QLabel(self)
            label.setOpenExternalLinks(True)
            layout.addWidget(label)
            self.labels.append(label)

        self.generate_words()

        btn = QPushButton('Generate Words', self)
        btn.clicked.connect(self.generate_words)
        layout.addWidget(btn)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setWindowTitle('Random Word Generator')
        self.show()
        

    def openWebPage(self, link):
        url = QUrl(link)
        QDesktopServices.openUrl(url)
        

    # 隨機產生20個單字
    def generate_words(self):
        # 要產生單字的數量
        num_words = 20
        # 讀取單字列表
        df = pd.read_excel(r'C:\User\wordFrequency.xlsx',sheet_name='1 lemmas') 
        worddf = df[['lemma']] # 只選擇單字的欄位
        word_s = worddf.values.tolist() # 轉成series
        selected_words = random.sample(word_s,num_words)

        # 產生20個隨機單字
        random_words =[]
        # random_words = [random.choice(selected_words) for _ in range(10)]
        for word in selected_words:
            strword = '\n'.join(word)
            random_words.append(strword)
        
        random.shuffle(random_words)
        for i in range(20):
            random_word = random_words[i]
            label = self.labels[i]
            label.setText(f'<a href="https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E-%E6%BC%A2%E8%AA%9E-%E7%B9%81%E9%AB%94/{random_word}">{random_word}</a>')            
            font = QFont()
            font.setPointSize(14)  # 設置字體大小為14
            label.setFont(font)     
    
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.resize(400, 600)
    window.show()
    app.exec_()
