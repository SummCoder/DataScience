from bs4 import BeautifulSoup
import re
import urllib.request
import urllib.error
import xlwt


def main():
    # 获取网页信息
    baseurl = "https://www.zj.gov.cn/col/col1554467/index.html"
    baseurl1 = "https://www.zj.gov.cn/col/col1554468/index.html"
    baseurl2 = "https://www.zj.gov.cn/col/col1554469/index.html"
    baseurl3 = "https://www.zj.gov.cn/col/col1554470/index.html"
    # baseurl4 = "https://www.zj.gov.cn/col/col1229396854/index.html"
    # 爬取网页，调用自定义的getDate函数
    datalist, title = getDate(baseurl)
    datalist1, title1 = getDate1(baseurl1, 6839553)
    datalist2, title2 = getDate1(baseurl2, 6839589)
    datalist3, title3 = getDate1(baseurl3, 6839589)
    # datalist4, title4 = getDate(baseurl4)
    datalist_all = datalist + datalist1 + datalist2 + datalist3
    title_all = title + title1 + title2 + title3
    # 创建数据保存路径
    savepath = ".\\数据存储库.xls"
    # 保存数据操作，调用saveDate函数
    saveDate(datalist_all, title_all, savepath)
    # print("爬取结束")


# 创建正则表达式对象，表示规则（字符串的模式）
findLink = re.compile(r'<a href="(.*?)" title')
findLink1 = re.compile(r'<p style="text-indent: 2em;">(.*?)</p>')
findLink2 = re.compile(r'<p style="text-align: left; text-indent: 2em;">(.*?)</p>')
findLink3 = re.compile(r'<p>(.*?)</p>')
findLink4 = re.compile(r'<p style="text-align: justify; text-indent: 2em;">(.*?)</p>')
findLink5 = re.compile(r'<p style="text-indent: 2em; text-align: justify;">(.*?)</p>')
findLink6 = re.compile(r'title=\'(.*?)\'')


# findLink7 = re.compile(r'title=\'(.*?)\'( {2})target="_blank">')


# getDate，爬取网页信息，进行数据爬取
def getDate(baseurl):
    datalist = []
    title = []
    # 逐一解析数据
    # for i in range(1, 10):
    url = baseurl
    html1 = askURL(url)  # 保存获取的网页源码

    #  逐一解析数据
    soup = BeautifulSoup(html1, "html.parser")
    for item in soup.find_all('div', id="7388415"):
        # print(item)  # 测试：查看信息
        item = str(item)
        if re.findall(findLink6, item):
            for j in range(6):
                title.append(re.findall(findLink6, item)[j])
        if re.findall(findLink, item):
            for j in range(6):
                link = "https://www.zj.gov.cn" + re.findall(findLink, item)[j]  # re库用来通过正则表达式查找指定字符串
                html1 = askURL(link)
                soup1 = BeautifulSoup(html1, "html.parser")
                data = ""
                for item1 in soup1.find_all('p', style="text-indent: 2em;"):
                    item1 = str(item1)
                    if re.findall(findLink1, item1):
                        text = re.findall(findLink1, item1)[0]
                        data += text
                datalist.append(data)
                for item2 in soup1.find_all("td", class_="wzbt"):
                    item2 = str(item2)
                    if re.findall(findLink6, item2):
                        title_content = re.findall(findLink6, item2)[0]
                        title.append(title_content)
                        print(title_content)
    return datalist, title


def getDate1(baseurl, id0):
    datalist = []
    title = []
    # 逐一解析数据
    url = baseurl
    html1 = askURL(url)  # 保存获取的网页源码

    #  逐一解析数据
    soup = BeautifulSoup(html1, "html.parser")
    for item in soup.find_all('div', id=id0):
        # print(item)  # 测试：查看信息
        item = str(item)
        if re.findall(findLink6, item):
            for j in range(6):
                title.append(re.findall(findLink6, item)[j])
        if re.findall(findLink, item):
            for j in range(6):
                if re.findall(findLink, item)[j][0:20] != "http://www.zj.gov.cn":
                    link = "https://www.zj.gov.cn" + re.findall(findLink, item)[j]  # re库用来通过正则表达式查找指定字符串
                else:
                    link = "https://www.zj.gov.cn" + re.findall(findLink, item)[j][20:]
                # print(link)
                html1 = askURL(link)
                soup1 = BeautifulSoup(html1, "html.parser")
                data = ""
                for item1 in soup1.find_all('p'):
                    item1 = str(item1)
                    if re.findall(findLink2, item1):
                        text = re.findall(findLink2, item1)[0]
                        data += text
                    if re.findall(findLink1, item1):
                        text = re.findall(findLink1, item1)[0]
                        data += text
                    if re.findall(findLink3, item1):
                        text = re.findall(findLink3, item1)[0]
                        data += text
                    if re.findall(findLink4, item1):
                        text = re.findall(findLink4, item1)[0]
                        data += text
                    elif re.findall(findLink5, item1):
                        text = re.findall(findLink5, item1)[0]
                        data += text
                datalist.append(data)
    return datalist, title


# 得到一个指定的URL的网页内容
def askURL(url):
    global html
    head = {  # 模拟浏览器头部信息，向服务器发送消息
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(HTML, likeGecko) Chrome / "
                      "92.0.4515.131Safari / 537.36SLBrowser / 8.0.03161SLBChan / 103 "
    }

    request = urllib.request.Request(url, headers=head)
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html


# 保存数据
def saveDate(datalist, titlelist, savepath):
    workbook = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    worksheet = workbook.add_sheet('爬取数据', cell_overwrite_ok=True)  # 创建工作表
    for i in range(24):
        data = datalist[i]
        worksheet.write(i, 1, data)
        title = titlelist[i]
        worksheet.write(i, 0, title)
        file = open(r'C:\Users\Lenovo\Desktop\数据\{}.txt'.format(title), mode='a', encoding='utf-8')
        # file.write(str(title) + "\n\n")
        # for j in range(len(data)):
        # file.write(str(len(data)))
        file.write(data)
        file.close()
    workbook.save(savepath)  # 用表格形式存储


if __name__ == '__main__':
    main()
