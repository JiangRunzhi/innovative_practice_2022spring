
from snownlp import SnowNLP
from cemotion import Cemotion
from math import exp
if __name__ == '__main__':
    inputs = open("testFile.txt", encoding='utf-8')
    scores = open("score.txt", encoding='utf-8')

    c = Cemotion()
    accumulative_c = 0
    accumulative_s = 0
    line = inputs.readline().strip('\n')
    score = scores.readline().strip('\n')

    while line:
        score = int(score)
        predict_c = c.predict(line)
        predict_s = SnowNLP(line).sentiments

        # 指数损失函数（exponential loss）
        accumulative_c += exp(abs(predict_c - score)*10) - 1
        accumulative_s += exp(abs(predict_s - score)*10) - 1
        print('"', line, '"\n', 'Cemotion预测值:{:6f}, \t\t\t\t    SnowNLP预测值:{:6f}, 目标值: {:d}'.format(predict_c, predict_s, score))
        print("Accumulative error of Cemotion: {:6f}".format(accumulative_c) , "  Accumulative error of SnowNLP: {:6f}".format(accumulative_s))
        print()
        line = inputs.readline().strip('\n')
        score = scores.readline().strip('\n')


    print("Accumulative error of Cemotion: {:6f}".format(accumulative_c))
    print("Accumulative error of SnowNLP: {:6f}".format(accumulative_s))
