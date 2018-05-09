from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import OrderedDict


def cleanInput(input):
    input = re.sub('\n+', ' ', input)            # 把\n换行符替换为空格
    input = re.sub('\[[0-9]*\]', ' ', input)     #剔除[1]引用字符
    input = re.sub(' +', ' ', input)             # 把连续的多个空格替换成一个空格
    input = input.upper()                        #不区分大小写
    input = bytes(input, 'utf-8')                # 把内容转化成utf-8格式
    input = input.decode('ascii', 'ignore')
    cleanInput = []                               # 创建一个空列表output
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)      #string.punctuation 返回所有的标点符号
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):            #剔除单字的单词，除非这个字符是i或者a
            cleanInput.append(item)            # 把切片i到i+n加入列表output
    return cleanInput

def getngrams(input, n):
    input = cleanInput(input)
    output = dict()
    for i in range(len(input)-n+1):
        newNGram = " ".join(input[i:i + n])
        if newNGram in output:
            output[newNGram] += 1
        else:
            output[newNGram] = 1
    return output


html = urlopen('https://en.wikipedia.org/wiki/Python_(programming_language)')
bsobj = BeautifulSoup(html, 'lxml')
content = bsobj.find('div',{'id':'mw-content-text'}).get_text()
ngrams= getngrams(content, 2)
ngrams= OrderedDict(sorted(ngrams.items(), key=lambda t: t[1], reverse=True))
print(ngrams)
print('2-grams count is:'+str(len(ngrams)))
