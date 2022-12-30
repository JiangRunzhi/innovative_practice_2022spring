from snownlp import SnowNLP
from cemotion import Cemotion
from sql.input_sql import InputTool

file_input_name = 'prediction/bilibili_qian10.txt'
file_output_name = 'prediction/bilibili_qian10_out.txt'
encoding = 'utf-8'


def onlyCemotion(f) :
    out = ""
    c = Cemotion()
    line = f.readline().strip('\n')
    count_c = 0
    all_c = 0
    while line:
        line = line.strip('\n')

        predict_c = c.predict(line)

        count_c += 1
        all_c += predict_c

        out = out + '"'+ line+ '"\n'+ 'Cemotion预测值:{:6f}'.format(predict_c)+ '\n'
        print('"', line, '"\n', 'Cemotion预测值:{:6f}'.format(predict_c), '\n')
        while 1:
            line = f.readline()
            if line == '\n':
                continue
            break

    out = out + 'Cemotion预测值期望:{:6f}'.format(all_c/count_c)
    print('Cemotion预测值期望:{:6f}'.format(all_c/count_c))
    return out

def onlySnowNLP(f):
    out = ""
    line = f.readline()

    count_s = 0
    all_s = 0

    while line:
        line = line.strip('\n')
        predict_s = SnowNLP(line).sentiments

        count_s += 1
        all_s += predict_s

        out = out +'"'+ line+ '"\n'+ 'SnowNLP预测值:{:6f}'.format(predict_s)+ '\n'
        print('"', line, '"\n', 'SnowNLP预测值:{:6f}'.format(predict_s), '\n')
        while 1:
            line = f.readline()
            if line == '\n':
                continue
            break
    out = out + 'SnowNLP预测值期望:{:6f}'.format(all_s/count_s)
    print('SnowNLP预测值期望:{:6f}'.format(all_s/count_s))
    return out


def bothCemotionSnowNPL(f):
    out = ""
    c = Cemotion()
    line = f.readline()
    count_c = 0
    all_c = 0

    count_s = 0
    all_s = 0
    while line:
        line = line.strip('\n')
        predict_c = c.predict(line)
        predict_s = SnowNLP(line).sentiments

        count_c += 1
        all_c += predict_c
        count_s += 1
        all_s += predict_s


        out = out + '"'+ line+ '"\n'+ 'Cemotion预测值:{:6f}+ \t\t\t\t    SnowNLP预测值:{:6f}'.format(predict_c, predict_s)+'\n'
        # print('"', line, '"\n', 'Cemotion预测值:{:6f}, \t\t\t\t    SnowNLP预测值:{:6f}'.format(predict_c, predict_s)+'\n')
        while 1:
            line = f.readline()
            if line == '\n':
                continue
            break

    inputs =  InputTool()
    inputs.log_result(all_c/count_c, "全国", None, "Cemotion", "bilibili")
    inputs.log_result(all_s/count_s, "全国", None, "SnowNLP", "bilibili")
    inputs.finish_log()

    out = out + 'Cemotion预测值期望:{:6f}, \t\t\t\tSnowNLP预测值期望:{:6f}'.format(all_c/count_c, all_s/count_s)
    print('Cemotion预测值期望:{:6f}, \t\t\t\tSnowNLP预测值期望:{:6f}'.format(all_c/count_c, all_s/count_s))
    return out

def dataPersistence(out):
    f = open(file_output_name,'wt' ,encoding=encoding,)
    f.write(out)
    f.flush()
    f.close()

if __name__ == '__main__':
    f = open(file_input_name, encoding=encoding)
    out = bothCemotionSnowNPL(f)
    dataPersistence(out)
