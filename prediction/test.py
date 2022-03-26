# -*- codeing = utf-8 -*-
# @Time : 2022-03-26 20:41
# @Auther : Tankkupper
# @File : t.py
# @Software : PyCharm
import cemotion
from cemotion import Cemotion

if __name__ == '__main__':
    str_text1 = '配置顶级，不解释，手机需要的各个方面都很完美'

    str_text2 = '院线看电影这么多年以来，这是我第一次看电影睡着了。简直是史上最大烂片！没有之一！侮辱智商！大家小心警惕！千万不要上当！再也不要看了！'

    str_text3 = '智哥最帅'

    str_text4 = '我喜欢你！'

    str_text5 = '我是傻逼'

    str_text6 = '李浩博喜欢段安琪！！！'

    str_text7 = '段安琪喜欢李浩博！！！！！！'

    str_text8 = '俄罗斯向乌克兰宣战！！！'
    c = Cemotion()

    print('"', str_text1, '"\n', '预测值:{:6f}'.format(c.predict(str_text1)), '\n')

    print('"', str_text2, '"\n', '预测值:{:6f}'.format(c.predict(str_text2)), '\n')

    print('"', str_text3, '"\n', '预测值:{:6f}'.format(c.predict(str_text3)), '\n')

    print('"', str_text4, '"\n', '预测值:{:6f}'.format(c.predict(str_text4)), '\n')

    print('"', str_text5, '"\n', '预测值:{:6f}'.format(c.predict(str_text5)), '\n')

    print('"', str_text6, '"\n', '预测值:{:6f}'.format(c.predict(str_text6)), '\n')

    print('"', str_text7, '"\n', '预测值:{:6f}'.format(c.predict(str_text7)), '\n')

    print('"', str_text8, '"\n', '预测值:{:6f}'.format(c.predict(str_text8)), '\n')

    print('''''',"预测值越高表示情感倾向置信度越偏积极噢！情感倾向置信度为区间[0,1]")

