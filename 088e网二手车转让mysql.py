from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import re
import mysql.connector

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
    #连接到mysql数据库，数据库文件是scraping,如果不存在会自动创建
    conn = mysql.connector.connect(
    user='root',
    password='zh12345',
    host='127.0.0.1',
    port='3306',
    database='scraping'
    )

    cur = conn.cursor()
    #创建user表格
    cur.execute('create table user (text varchar(100) primary key, wz varchar(100))')

    for t in get_data(3):
        for x in t:
            v = (x.text, url1+x.a['href'])
            sql = "insert into user (text, wz) values(%s,%s);"
            cur.execute(sql, v)
    conn.commit()
    conn.close()

if __name__=='__main__':
    main()
