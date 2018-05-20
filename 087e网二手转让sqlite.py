from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import re
import sqlite3

def get_data(i):
    global url1
    list1 = []
    for i in range(1, i+1):
        url1 = 'http://secondhand.e0575.com/'
        url = url1 + '?page=' + str(i)
        html = urlopen(url)
        bsobj = BeautifulSoup(html, 'lxml')
        item = bsobj.find('ul', {'class': 'es_list1_l1'}).findAll('li')
        list1.append(item)
    return list1


def main():
    #连接到sqlite数据库，数据库文件是ewang.sqlite,如果不存在会自动创建
    conn = sqlite3.connect("ewang.sqlite")
    cur = conn.cursor()
    #创建user表格
    cur.execute('create table user (text varchar(20) primary key, wz varchar(20))')

    for t in get_data(3):
        for x in t:
            v = (x.text, url1+x.a['href'])
            sql = "insert into user (text, wz) values(?,?);"
            cur.execute(sql, v)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
