"""Functions adding noise to text"""
import jieba
import random
import utils
import nltk

punctuation = [
    "！", "？", "｡", "＂", "＃", "＄", "％", "＆", "＇", "（", "）", "＊", "＋", "，", "－",
    "／", "：", "；", "＜", "＝", "＞", "＠", "［", "＼", "］", "＾", '＿', "｀", "｛", "｜",
    "｝", "～", "｢", "｣", "､", "、", "〃", "》", "「", "」", "『", "』", "【", "】", "〔",
    "〕", "〖", "〗", "〘", "〙", "〚", "〛", "〜", "〝", "〞", "〟", "–", "‘", "‛", "”",
    "„", "‟", "…", "‧", "﹏", "."
]


# 冗余错误
def redundant_token(s, probability=0.163):
    lst_word_level = []  # 整个语料分词后合成的总的列表
    lst_word = []  # 整个语料分词后每个句子的列表
    D1 = {}  # 整个语料分词后的词表D1
    D2 = {}  # 整个语料字符级分词后的词表D2

    # 加载语料Cm
    for row in s:
        lst_row = row.split('\n')[0].replace(' ', '')
        row_split_word_level = list(jieba.cut(lst_row))  # 每行分词后的列表
        lst_word.append(row_split_word_level)
        for split_word_ in row_split_word_level:
            lst_word_level.append(split_word_)  # 整个语料分词后合成的列表
    for word in lst_word_level:
        if word not in punctuation:
            D1[word] = D1.get(word, 0) + 1
    noise_word = lst_word.copy()  # 存放加噪后句子的列表
    for s_ in noise_word:  # 遍历语料中的每个句子S*
        idx = int(random.random() * len(s_))
        idx2 = int(random.random() * len(s_))
        idx3 = int(random.random() * len(s_))
        if s_[idx] not in punctuation:
            k = random.random()  # 获取一个随机数k
            if k >= probability:
                continue
            else:
                w1 = random.choice(list(D1))  # 从D1左侧随机取一个单词w1
                s_[idx] = w1 + s_[idx]  # 在w左侧添加w1
        if s_[idx2] not in punctuation:
            k = random.random()  # 获取一个随机数k
            if k >= probability:
                continue
            else:
                w1 = random.choice(list(D1))  # 从D1左侧随机取一个单词w1
                s_[idx2] = w1 + s_[idx2]  # 在w左侧添加w1
        if s_[idx3] not in punctuation:
            k = random.random()  # 获取一个随机数k
            if k >= probability:
                continue
            else:
                w1 = random.choice(list(D1))  # 从D1左侧随机取一个单词w1
                s_[idx3] = w1 + s_[idx3]  # 在w左侧添加w1
    c_tmp = []  # 临时语料
    lst_char_level = []  # 整个语料按字符级分词后合成的列表
    lst_char = []  # 整个语料按字符级分词后每句的列表
    for _s in noise_word:
        c_tmp.append(''.join(_s))  # 将加噪的句子放入临时语料库c_tmp
    for _s in c_tmp:
        tmp = []
        for _w in _s:
            lst_char.append(_w)
            tmp.append(_w)
        lst_char_level.append(tmp)
    for word in lst_char:
        if word not in punctuation:
            D2[word] = D2.get(word, 0) + 1
    noise_char = lst_char_level.copy()  # 存放加字符噪后句子的列表
    for s_ in noise_char:  # 遍历c_tmp语料中的每个句子S*
        idx = int(random.random() * len(s_))
        idx2 = int(random.random() * len(s_))
        idx3 = int(random.random() * len(s_))
        if s_[idx] not in punctuation:
            k = random.random()  # 获取一个随机数k
            if k >= probability:
                continue
            else:
                w2 = random.choice(list(D2))  # 从D2左侧随机取一个单词w2
                s_[idx] = w2 + s_[idx]  # 在w左侧添加w2
        if s_[idx2] not in punctuation:
            k = random.random()  # 获取一个随机数k
            if k >= probability:
                continue
            else:
                w2 = random.choice(list(D2))  # 从D2左侧随机取一个单词w2
                s_[idx2] = w2 + s_[idx2]  # 在w左侧添加w2
        if s_[idx3] not in punctuation:
            k = random.random()  # 获取一个随机数k
            if k >= probability:
                continue
            else:
                w2 = random.choice(list(D2))  # 从D2左侧随机取一个单词w2
                s_[idx3] = w2 + s_[idx3]  # 在w左侧添加w2
    c_noise = []  # 最终的噪声语料库
    for _s in noise_char:
        c_noise.append(''.join(_s))  # 将加字符级噪的句子放入最终语料库c_noise
    return ''.join(c_noise)
    "*********冗余错误加噪完成*********"


# 缺词错误
def missing_token(s, probability=0.163):
    lst_word_level = []  # 整个语料分词后合成的总的列表
    lst_word = []  # 整个语料分词后每个句子的列表

    # 加载语料Cm
    for row in s:
        lst_row = row.split('\n')[0].replace(' ', '')
        row_split_word_level = list(jieba.cut(lst_row))  # 每行分词后的列表
        lst_word.append(row_split_word_level)
        for split_word_ in row_split_word_level:
            lst_word_level.append(split_word_)  # 整个语料分词后合成的列表

    noise_word = lst_word.copy()  # 存放加噪后句子的列表
    for s_ in noise_word:  # 遍历语料中的每个句子S*
        idx = int(random.random() * len(s_))
        if -len(s_) < idx < len(s_):
            if s_[idx] not in punctuation and idx < len(s_):
                k = random.random()  # 获取一个随机数k
                if k >= probability:
                    continue
                else:
                    del (s_[idx])  # 删除w
    c_tmp = []  # 临时语料
    lst_char_level = []  # 整个语料按字符级分词后合成的列表
    lst_char = []  # 整个语料按字符级分词后每句的列表
    for _s in noise_word:
        c_tmp.append(''.join(_s))  # 将加噪的句子放入临时语料库c_tmp
    for _s in c_tmp:
        tmp = []
        for _w in _s:
            lst_char.append(_w)
            tmp.append(_w)
        lst_char_level.append(tmp)
    noise_char = lst_char_level.copy()  # 存放加字符噪后句子的列表
    for s_ in noise_char:  # 遍历c_tmp语料中的每个句子S*
        idx = int(random.random() * len(s_))
        if idx < len(s_):
            if s_[idx] not in punctuation and idx < len(s_):
                k = random.random()  # 获取一个随机数k
                if k >= probability:
                    continue
                else:
                    if s_ is not None:
                        del (s_[idx])  # 删除w
    c_noise = []  # 最终的噪声语料库
    for _s in noise_char:
        c_noise.append(''.join(_s))  # 将加字符级噪的句子放入最终语料库c_noise
    return ''.join(c_noise)
    "*********缺词错误加噪完成*********"


# 词序错误
def ordering_token(s, probability=0.163):
    lst_word_level = []  # 整个语料分词后合成的总的列表
    lst_word = []  # 整个语料分词后每个句子的列表

    # 加载语料Cm
    for row in s:
        lst_row = row.split('\n')[0].replace(' ', '')
        row_split_word_level = list(jieba.cut(lst_row))  # 每行分词后的列表
        lst_word.append(row_split_word_level)
        for split_word_ in row_split_word_level:
            lst_word_level.append(split_word_)  # 整个语料分词后合成的列表
    noise_word = lst_word.copy()  # 存放加噪后句子的列表
    for s_ in noise_word:  # 遍历语料中的每个句子S*
        idx = int(random.random() * len(s_))
        idx2 = int(random.random() * len(s_))
        idx3 = int(random.random() * len(s_))
        if s_[idx] not in punctuation:
            k = random.random()  # 获取一个随机数k
            if k >= probability:
                continue
            else:
                i_ = random.randint(0, len(s_) - 1)  # 取一个大小在0到每个句子长度-1之间的随机数
                if s_[i_] not in punctuation:
                    s_[idx] = s_[i_]  # 相互交换顺序
                    s_[i_] = s_[idx]
        if s_[idx2] not in punctuation:
            k = random.random()  # 获取一个随机数k
            if k >= probability:
                continue
            else:
                i_ = random.randint(0, len(s_) - 1)  # 取一个大小在0到每个句子长度-1之间的随机数
                if s_[i_] not in punctuation:
                    s_[idx2] = s_[i_]  # 相互交换顺序
                    s_[i_] = s_[idx2]
        if s_[idx3] not in punctuation:
            k = random.random()  # 获取一个随机数k
            if k >= probability:
                continue
            else:
                i_ = random.randint(0, len(s_) - 1)  # 取一个大小在0到每个句子长度-1之间的随机数
                if s_[i_] not in punctuation:
                    s_[idx3] = s_[i_]  # 相互交换顺序
                    s_[i_] = s_[idx3]
    c_tmp = []  # 临时语料
    lst_char_level = []  # 整个语料按字符级分词后合成的列表
    lst_char = []  # 整个语料按字符级分词后每句的列表
    for _s in noise_word:
        c_tmp.append(''.join(_s))  # 将加噪的句子放入临时语料库c_tmp
    for _s in c_tmp:
        tmp = []
        for _w in _s:
            lst_char.append(_w)
            tmp.append(_w)
        lst_char_level.append(tmp)
    noise_char = lst_char_level.copy()  # 存放加字符噪后句子的列表
    for s_ in noise_char:  # 遍历c_tmp语料中的每个句子S*
        idx = int(random.random() * len(s_))
        idx2 = int(random.random() * len(s_))
        idx3 = int(random.random() * len(s_))
        if s_[idx] not in punctuation:
            k = random.random()  # 获取一个随机数k
            if k >= probability:
                continue
            else:
                i_ = random.randint(0, len(s_) - 1)  # 取一个大小在0到每个句子长度-1之间的随机数
                if s_[i_] not in punctuation:
                    s_[idx] = s_[i_]  # 相互交换顺序
                    s_[i_] = s_[idx]
                else:
                    i__ = random.randint(0,
                                         len(s_) - 1)  # 取一个大小在0到每个句子长度-1之间的随机数
                    if s_[i__] not in punctuation:
                        s_[idx] = s_[i__]  # 相互交换顺序
                        s_[i__] = s_[idx]
        if s_[idx2] not in punctuation:
            k = random.random()  # 获取一个随机数k
            if k >= probability:
                continue
            else:
                i_ = random.randint(0, len(s_) - 1)  # 取一个大小在0到每个句子长度-1之间的随机数
                if s_[i_] not in punctuation:
                    s_[idx2] = s_[i_]  # 相互交换顺序
                    s_[i_] = s_[idx2]
                else:
                    i__ = random.randint(0,
                                         len(s_) - 1)  # 取一个大小在0到每个句子长度-1之间的随机数
                    if s_[i__] not in punctuation:
                        s_[idx2] = s_[i__]  # 相互交换顺序
                        s_[i__] = s_[idx2]
        if s_[idx3] not in punctuation:
            k = random.random()  # 获取一个随机数k
            if k >= probability:
                continue
            else:
                i_ = random.randint(0, len(s_) - 1)  # 取一个大小在0到每个句子长度-1之间的随机数
                if s_[i_] not in punctuation:
                    s_[idx3] = s_[i_]  # 相互交换顺序
                    s_[i_] = s_[idx3]
                else:
                    i__ = random.randint(0,
                                         len(s_) - 1)  # 取一个大小在0到每个句子长度-1之间的随机数
                    if s_[i__] not in punctuation:
                        s_[idx3] = s_[i__]  # 相互交换顺序
                        s_[i__] = s_[idx3]
    c_noise = []  # 最终的噪声语料库
    for _s in noise_char:
        c_noise.append(''.join(_s))  # 将加字符级噪的句子放入最终语料库c_noise
    return ''.join(c_noise)
    "*********词序错误加噪完成*********"


# 选词错误
def selection_token(s, probability=0.163):
    lst_word_level = []  # 整个语料分词后合成的总的列表
    lst_word = []  # 整个语料分词后每个句子的列表
    D1 = {}  # 整个语料分词后的词表D1
    D2 = {}  # 整个语料字符级分词后的词表D2

    # 加载语料Cm
    for row in s:
        lst_row = row.split('\n')[0].replace(' ', '')
        row_split_word_level = list(jieba.cut(lst_row))  # 每行分词后的列表
        lst_word.append(row_split_word_level)
        for split_word_ in row_split_word_level:
            lst_word_level.append(split_word_)  # 整个语料分词后合成的列表
    for word in lst_word_level:
        if word not in punctuation:
            D1[word] = D1.get(word, 0) + 1
    noise_word = lst_word.copy()  # 存放加噪后句子的列表
    for s_ in noise_word:  # 遍历语料中的每个句子S*
        idx = int(random.random() * len(s_))
        idx2 = int(random.random() * len(s_))
        idx3 = int(random.random() * len(s_))
        if s_[idx] not in punctuation:
            k = random.random()  # 获取一个随机数k
            if k >= probability:
                continue
            else:
                w1 = random.choice(list(D1))  # 从D1随机取一个单词w1
                s_[idx] = w1  # 用别的单词替代w
        if s_[idx2] not in punctuation:
            k = random.random()  # 获取一个随机数k
            if k >= probability:
                continue
            else:
                w1 = random.choice(list(D1))  # 从D1随机取一个单词w1
                s_[idx2] = w1  # 用别的单词替代w
        if s_[idx3] not in punctuation:
            k = random.random()  # 获取一个随机数k
            if k >= probability:
                continue
            else:
                w1 = random.choice(list(D1))  # 从D1随机取一个单词w1
                s_[idx3] = w1  # 用别的单词替代w
    c_tmp = []  # 临时语料
    lst_char_level = []  # 整个语料按字符级分词后合成的列表
    lst_char = []  # 整个语料按字符级分词后每句的列表
    for _s in noise_word:
        c_tmp.append(''.join(_s))  # 将加噪的句子放入临时语料库c_tmp
    for _s in c_tmp:
        tmp = []
        for _w in _s:
            lst_char.append(_w)
            tmp.append(_w)
        lst_char_level.append(tmp)
    for word in lst_char:
        if word not in punctuation:
            D2[word] = D2.get(word, 0) + 1
    noise_char = lst_char_level.copy()  # 存放加字符噪后句子的列表
    # 错误字加噪
    for s_ in noise_char:  # 遍历c_tmp语料中的每个句子S*
        idx = int(random.random() * len(s_))
        idx2 = int(random.random() * len(s_))
        idx3 = int(random.random() * len(s_))
        if s_[idx] not in punctuation:
            k = random.random()  # 获取一个随机数k
            if k >= probability:
                continue
            else:
                w1 = random.choice(list(D2))  # 从词表中任意选择一个字
                s_[idx] = w1
        if s_[idx2] not in punctuation:
            k = random.random()  # 获取一个随机数k
            if k >= probability:
                continue
            else:
                w1 = random.choice(list(D2))  # 从词表中任意选择一个字
                s_[idx2] = w1
        if s_[idx3] not in punctuation:
            k = random.random()  # 获取一个随机数k
            if k >= probability:
                continue
            else:
                w1 = random.choice(list(D2))  # 从词表中任意选择一个字
                s_[idx3] = w1
    # 同音字加噪
    for s_ in noise_char:  # 遍历c_tmp语料中的每个句子S*
        idx = int(random.random() * len(s_))
        idx2 = int(random.random() * len(s_))
        idx3 = int(random.random() * len(s_))
        if s_[idx] not in punctuation:
            k = random.random()  # 获取一个随机数k
            if k >= probability:
                continue
            else:
                w2 = utils.homophones_char(s_[idx])  # 从词表中找出w的同音字
                if w2 is not None:
                    s_[idx] = w2
                else:
                    s_[idx] = s_[idx]
        if s_[idx2] not in punctuation:
            k = random.random()  # 获取一个随机数k
            if k >= probability:
                continue
            else:
                w2 = utils.homophones_char(s_[idx2])  # 从词表中找出w的同音字
                if w2 is not None:
                    s_[idx2] = w2
        if s_[idx3] not in punctuation:
            k = random.random()  # 获取一个随机数k
            if k >= probability:
                continue
            else:
                w2 = utils.homophones_char(s_[idx3])  # 从词表中找出w的同音字
                if w2 is not None:
                    s_[idx3] = w2
    # 形近字加噪
    for s_ in noise_char:  # 遍历c_tmp语料中的每个句子S*
        idx = int(random.random() * len(s_))
        idx2 = int(random.random() * len(s_))
        idx3 = int(random.random() * len(s_))
        if s_[idx] not in punctuation:
            k = random.random()  # 获取一个随机数k
            if k >= probability:
                continue
            else:
                w2 = utils.similar_form_characters(s_[idx])  # 从词表中找出w的形近字
                if w2 is not None:
                    s_[idx] = w2
        if s_[idx2] not in punctuation:
            k = random.random()  # 获取一个随机数k
            if k >= probability:
                continue
            else:
                w2 = utils.similar_form_characters(s_[idx2])  # 从词表中找出w的形近字
                if w2 is not None:
                    s_[idx2] = w2
        if s_[idx3] not in punctuation:
            k = random.random()  # 获取一个随机数k
            if k >= probability:
                continue
            else:
                w2 = utils.similar_form_characters(s_[idx3])  # 从词表中找出w的形近字
                if w2 is not None:
                    s_[idx3] = w2
    c_noise = []  # 最终的噪声语料库
    for _s in noise_char:
        c_noise.append(''.join(_s))  # 将加字符级噪的句子放入最终语料库c_noise
    return ''.join(c_noise)
    "*********选词错误加噪完成*********"


def noise(s):
    BleuScore3 = nltk.translate.bleu_score.sentence_bleu([s], redundant_token(s))
    BleuScore4 = nltk.translate.bleu_score.sentence_bleu([s], missing_token(s))
    BleuScore5 = nltk.translate.bleu_score.sentence_bleu([s], ordering_token(s))
    BleuScore6 = nltk.translate.bleu_score.sentence_bleu([s], selection_token(s))
    return redundant_token(s), missing_token(s), ordering_token, selection_token, BleuScore3, BleuScore4, BleuScore5, BleuScore6
