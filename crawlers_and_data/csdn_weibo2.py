import requests
import json
import re
from time import sleep
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
import jieba

def get_comment(num):
    url = 'https://m.weibo.cn/comments/hotflow?id=4745507782267013&mid=4745507782267013&max_id_type=' + str(num)

    response = requests.get(url)
    #print(response.content.decode())
    content  = json.loads(response.text) #把获得数据转换成字典格式
    #print(content)
    #print(content['data']['data'])
    for i in content['data']['data']:
        text= i['text']
        #print(text)
        label_filter = re.compile(r'<span class="url-icon">.*?</span>', re.S) 
        comment = re.sub(label_filter, '', text)#把一些链接去掉，保留纯文本内容。
        #print(comment)
        with open('weibo.txt', "a", encoding="utf8") as f:
            f.write(comment + '\n')


def GetWordCloud():
    path_txt = r'weibo.txt' #数据路径
    #path_img = r"C:\Users\Administrator\Desktop\timg .jpg" #图片路径（我使用的图片是索隆大大的，哈哈）
    f = open(path_txt, 'r', encoding='UTF-8').read()
    #background_image = np.array(Image.open(path_img))
    # 结巴分词，生成字符串，如果不通过分词，无法直接生成正确的中文词云,感兴趣的朋友可以去查一下，有多种分词模式
    # Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
    cut_text = " ".join(jieba.cut(f))

    wordcloud = WordCloud(
        # 设置字体，不然会出现口字乱码，文字的路径是电脑的字体一般路径，可以换成别的
        font_path="C:/Windows/Fonts/simfang.ttf",
        background_color="white"
        # mask参数=图片背景，必须要写上，另外有mask参数再设定宽高是无效的
        #,mask=background_image
        ).generate(cut_text)
    # 生成颜色值
    #image_colors = ImageColorGenerator(background_image)
    # 下面代码表示显示图片
    # plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
    # plt.axis("off")
    # plt.show()
    wordcloud.to_file("weibo.png")


if __name__ == '__main__':
   for i in range(2):
       get_comment(i)
       sleep(2)
       
# GetWordCloud()
# ————————————————
# 版权声明：本文为CSDN博主「sl01224318」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/sl01224318/article/details/98384298