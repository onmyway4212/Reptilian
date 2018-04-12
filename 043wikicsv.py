import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://en.wikipedia.org/wiki/Comparison_of_text_editors')
bsobj = BeautifulSoup(html, 'lxml')
table = bsobj.findAll('table', {'class': 'wikitable'})[0]    #bsobj看成一个列表，[0]返回第一张表格
rows = table.findAll('tr')                                   #tr是一行的数据，返回到rows列表

csvFile = open('d://2.csv', 'wt', newline='', encoding='utf-8')   #打开文件csvFile t以文本模式打开
writer =csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):                    #单元格数据都在td里面
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()
