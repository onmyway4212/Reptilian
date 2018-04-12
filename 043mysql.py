import pymysql
conn = pymysql.connect(host = '127.0.0.1', user = 'root',password = 'zh12345',db = 'mysql')   #conn链接对象
cur = conn.cursor()                                                                           #光标对象
cur.execute("use scraping")
cur.execute('select * from pages where id = 3')
print(cur.fetchone())
cur.close()
conn.close()
