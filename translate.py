# 使用百度翻译API,使用了百度翻译目前给出的中英互译以及中日互译两种方式，就是百度翻译200万字以后得收费了
# encoding=utf-8

import http.client
import hashlib
import urllib
import random
import json
import time
import jieba
import nltk


# 中文翻译为英文
def trans_lang(q):
    trans_result = q
    appid = ''  # 填写你的appid
    secretKey = ''  # 填写你的密钥

    httpClient = None
    myurl = '/api/trans/vip/translate'  # 通用翻译API HTTP地址

    fromLang = 'zh'  # 中文原文
    toLang = 'en'  # 英文翻译
    salt = random.randint(32768, 65536)
    # 手动录入翻译内容，q存放
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + \
            '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
    # 建立会话，返回结果
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)
        trans_result = result['trans_result'][0]['dst']
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()
    return trans_result


# 英文翻译为中文，进行回译
def trans_lang1(q):
    trans_result = q
    appid = ''
    secretKey = ''

    httpClient = None
    myurl = '/api/trans/vip/translate'

    fromLang = 'en'
    toLang = 'zh'
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + \
            '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)
        trans_result = result['trans_result'][0]['dst']
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()
    return trans_result


def trans_lang2(q):
    trans_result = q
    appid = ''
    secretKey = ''

    httpClient = None
    myurl = '/api/trans/vip/translate'

    fromLang = 'zh'  # 原文中文
    toLang = 'jp'  # 译为日语
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + \
            '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)
        trans_result = result['trans_result'][0]['dst']
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()
    return trans_result


def trans_lang3(q):
    trans_result = q
    appid = ''
    secretKey = ''

    httpClient = None
    myurl = '/api/trans/vip/translate'

    fromLang = 'jp'
    toLang = 'zh'
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + \
            '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)
        trans_result = result['trans_result'][0]['dst']
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()
    return trans_result


def translate(trans_content):
    time_start = time.time()  # 记录开始时间
    # print(trans_lang1(trans_lang(trans_content)))
    # print(trans_lang3(trans_lang2(trans_content)))
    # function()   执行的程序
    time_end = time.time()  # 记录结束时间
    time_sum = time_end - time_start  # 计算的时间差为程序的执行时间，单位为秒/s
    # print(time_sum)
    data1 = trans_content
    data2 = trans_lang1(trans_lang(trans_content))
    data3 = trans_lang3(trans_lang2(trans_content))
    cut1 = jieba.lcut(data1)
    cut2 = jieba.lcut(data2)
    cut3 = jieba.lcut(data3)
    # print(cut1)
    # print(cut2)
    # print(cut3)
    BleuScore = nltk.translate.bleu_score.sentence_bleu([data1], data2)
    BleuScore1 = nltk.translate.bleu_score.sentence_bleu([data1], data3)
    return data1, data2, data3, BleuScore, BleuScore1
    # print(BleuScore)
    # print(BleuScore1)

