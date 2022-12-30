from snownlp import SnowNLP

if __name__ == '__main__':
    s = SnowNLP(u'今晚夜色真美呀')
    sentiments = s.sentiments
    print(sentiments)