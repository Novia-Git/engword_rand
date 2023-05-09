from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget
from PyQt5.QtCore import QTimer
import random
import pandas as pd

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 創建界面元素
        self.list_widget = QListWidget()
        self.button = QPushButton('Generate Words')

        # 設置佈局
        layout = QVBoxLayout()
        layout.addWidget(self.list_widget)
        layout.addWidget(self.button)
        self.setLayout(layout)

        # 設置計時器，每15秒觸發一次產生隨機單字的功能
        self.timer = QTimer()
        self.timer.timeout.connect(self.generate_words)
        self.timer.start(15000)

        # 綁定按鈕事件，點擊按鈕時手動產生隨機單字
        self.button.clicked.connect(self.generate_words)

    # 定義函數，隨機產生10個單字
    def generate_words(self):
        # 要產生單字的數量
        num_words = 20
        # 讀取單字列表
        df = pd.read_excel(r'C:\異次元\wordFrequency.xlsx',sheet_name='1 lemmas') 
        worddf = df[['lemma']] # 只選擇單字的欄位
        word_s = worddf.values.tolist() # 轉成series
        selected_words = random.sample(word_s,num_words)
        # with open('words.txt', 'r') as f:
        #     words = f.read().splitlines()
        # 產生10個隨機單字
        random_words =[]
        # random_words = [random.choice(selected_words) for _ in range(10)]
        for word in selected_words:
            strword = '\n'.join(word)
            random_words.append(strword)
        # 在界面上顯示隨機單字
        self.list_widget.clear()
        self.list_widget.addItems(random_words)
       

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.resize(300, 600)
    window.show()
    app.exec_()
