import random
import pandas as pd
import time

# 要產生單字的數量
num_words = 20

# 單字的長度
word_length = 7

# 產生單字
def generate_word(words, length):
    # 選擇num_words個隨機單字
    return random.sample(words, length)

df = pd.read_excel(r'C:\Users\wordFrequency.xlsx',sheet_name='1 lemmas') 
worddf = df[['lemma']] # 只選擇單字的欄位
word_s = worddf.values.tolist() # 轉成series

# 每隔15秒隨機列印單字
while True:
    selected_words = generate_word(word_s,num_words)
    for word in selected_words:
        strword = '\n'.join(word) # 轉成string
        word = strword.strip()  # 移除單字前後的空白字元
        print(word)
    time.sleep(15)
