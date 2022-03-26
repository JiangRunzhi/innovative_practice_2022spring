# innovative_practice_2022spring

主流社交平台的情感比较分析



先使用爬虫获取各个网站的数据，

再使用机器学习对文本进行分类

多维度分析数据得出结论

就像一次数学建模



## 关于情感分析

### 准备工作

- 使用[情感分析库](https://github.com/Cyberbolt/Cemotion.git)，此处感谢[Cyberbolt](https://github.com/Cyberbolt/Cemotion/commits?author=Cyberbolt)
- 根据[Cemotion 基于NLP的 中文情感倾向分析库 -电光笔记 (cyberlight.xyz)](https://www.cyberlight.xyz/passage/cemotion-nlp)进行调用

### 踩坑记录

该库需要`tensorflow`的支持，首次运行时可能会发现`tensorflow`缺失`.dll`（动态链接库），解决方案是百度缺失的`.dll`然后放到`C:\windows\system32下`即可

在调用`Cemotion()`时会检查模型文件`.h5`和中文词典`.dict`是否存在，用pip install cemotion下载的库文件是缺失这两个文件的，当发现缺失文件后，本来是由库中的函数`download_from_url`来负责下载缺失的文件的，但是不知道为什么会下载失败。

我的解决方案是手动下载，然后放到指定的位置供库调用。

- 模型文件`rnn_emotion_x86_1.0.h5`放在cemotion\models\下

- 字典文件`big_Chinese_Words_Map.dict`放到/models/requirements\下

- （模型文件，字典文件已上传，在prediction\missing_file\下）

