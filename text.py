import numpy as np 
import pandas as pd 
from wordcloud import WordCloud, STOPWORDS
import jieba
import matplotlib.pyplot as plt
from PIL import Image


class TextMiner(object):
    def __init__(self, file_path="./results/error_data_cn.xlsx"):
        self.text = pd.read_excel(file_path, encoding="UTF-8")
        
    def get_text_str(self):
        text_list = []
        for i in range(0, self.text.shape[0]):
            temp = [self.text.iloc[i, 0]] * self.text.iloc[i, 1]
            text_list.extend(temp)

        return str(text_list)

    def text_analysis(self):
        text_str = self.get_text_str()
        stopwords = set(STOPWORDS)
        stopwords.add("原因")
        stopwords.add("延迟")
        stopwords.add("延误")
        stopwords.add("火车")
        stopwords.add("晚点")
        stopwords.add("旅行")
        stopwords.add("一次")
        stopwords.add("一列")
        stopwords.add("由于")
        stopwords.add("今天")
        stopwords.add("ICE")
        cn_sw = open("./data/cn_stopwords.txt", encoding="utf-8").readlines()
        for sw in cn_sw:
            stopwords.add(sw)
        self.stopwords = stopwords
        # Cutting
        self.cut_text = jieba.lcut(text_str)
        self.cut_text_wc = " ".join(self.cut_text)
        # Record word frequency
        counts = {}  
        for word in self.cut_text:     
            if word not in stopwords:       
                if len(word) == 1:              
                    continue          
                else:              
                    counts[word] = counts.get(word, 0) + 1  
        items = list(counts.items())  
        items.sort(key=lambda x:x[1], reverse=True)
        self.items = items
        with open("./results/cut_items.txt", "w") as f:
            for fp in items:
                f.write(str(fp))
                f.write("\n")
            print("data saved. ")
        
    def most_freq(self, num=20):
        print("The most frequent %d words are:"%num)
        for i in range(0, num):
            print(self.items[i])

    def create_word_cloud(self):
        # Creating word cloud
        font = "C:\Windows\Fonts\SimHei.ttf"
        image = np.array(Image.open("./data/ger.jpg"))
        word_cloud = WordCloud(background_color="white", max_words=80, font_path=font, 
                                collocations=False, stopwords=self.stopwords, 
                                width=600, height=300, mask=image, 
                                max_font_size=80, random_state=20)
        word_cloud.generate(self.cut_text_wc)
        
        plt.imshow(word_cloud, interpolation="bilinear")
        plt.axis("off")
        plt.savefig("./results/word_cloud.png", dpi=800)
        print("Word cloud saved. ")
        plt.show()
        

def run_text():
    tm = TextMiner()
    tm.text_analysis()
    tm.most_freq()
    tm.create_word_cloud()


if __name__ == "__main__":
    run_text()

