import requests
import time
import hashlib
import os
from bs4 import BeautifulSoup


class EggsClimber:
    TheFinish = '''
###################################################################
#       Done,All the article you ask is climbed!                  #
#       Is good website:https://77nali.com/                       #
#       and I have some very similar website you may want to view:#
#       http://htwgif.com/                                        #
#       http://tu.duowan.com/m/bxgif                              #
#       http://www.fulibae.com/                                   #
#       have good day ^_^                                         #
###################################################################
                                '''
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'cookie': 'UM_distinctid=15eb26f5e506e-0384dcf277e50f-5d153b16-1fa400-15eb26f5e51560; Hm_lvt_11df17f23583077b56f6b7e91766cfd6=1507345564,1507437987,1507781100,1507795104; Hm_lpvt_11df17f23583077b56f6b7e91766cfd6=1507796147; CNZZDATA1260180129=722484165-1506260005-https%253A%252F%252F77nali.com%252F%7C1507793571SZS',
        'host': '77nali.com', 'referer': 'https://77nali.com/dongtaitu/page/3', 'connection': 'keep-alive'}
    timeout = 10
    base_url = "https://77nali.com/dongtaitu/"
    base_path = r"E:\test"  # the path where you want save

    def try_untill_get(self, url, what):
        while 1:
            try:
                if what == 'html':
                    the_get = requests.get(url, headers=self.headers, timeout=self.timeout).text
                else:
                    the_get = requests.get(url, headers=self.headers, timeout=self.timeout).content
                break
            except:
                print("maybe be catched,just let me sleep!")
                time.sleep(3)
        return the_get

    def create_new_name(self, content, end):
        mini = str(content[1000:1111]).encode('utf-8') + str(content[4000:4111]).encode('utf-8')
        new_name = hashlib.md5(mini).hexdigest() + end
        return new_name

    def get_num(self, list):
        num = 0
        for item in list:
            num = num + 1
        return num

    def get_img(self, soup):
        img_list = soup.find('article').find_all('img')
        for img in img_list:
            content = self.try_untill_get(img['src'], 'gif')
            name = self.create_new_name(content, '.gif')
            path = self.base_path + "\\" + name
            with open(path, 'wb+') as f:
                f.write(content)
            print('gif:%s done' % name)

    def get_reset_all(self, link, all_num):
        num = 2
        while num < all_num:
            html = self.try_untill_get(link + '/' + str(num), 'html')
            num = num + 1
            soup = BeautifulSoup(html, "html.parser")
            self.get_img(soup)
            time.sleep(1)

    def GoGet(self):
        choose = input(
            "Witch url you want me to climb?[1:https://77nali.com/dongtaitu/ ; 2:https://77nali.com/gifchuchu]")
        if choose == '2':
            print('Climb on https://77nali.com/gifchuchu')
            self.base_url = 'https://77nali.com/gifchuchu'
        else:
            print("Climb on https://77nali.com/dongtaitu/")
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)
        article = 1
        article = input("How many article you want?:")
        current_article = int(article)
        if current_article <= 0:
            print("Seriously???-_-???")
        current_page = int(current_article / 20) + 1
        else_path = ''
        while current_page > 0:
            url = self.base_url + else_path
            html = self.try_untill_get(url, 'html')
            print('page:%d get' % current_page)
            soup = BeautifulSoup(html, "html.parser")
            article_list = soup.find_all('article', class_='excerpt')
            for article in article_list:
                link = article.find('a')['href']
                html = self.try_untill_get(link, 'html')
                print('article:%s done' % link)
                soup = BeautifulSoup(html, "html.parser")
                try:
                    a_list = soup.find('div', class_='article-paging').find_all('a')
                    all_num = self.get_num(a_list)
                    self.get_img(soup)
                    time.sleep(1)
                    self.get_reset_all(link, all_num)
                except:
                    continue
                current_article = current_article - 1
                if current_article == 0:
                    print(self.TheFinish)
                    return 0
            current_page = current_page - 1


if __name__ == '__main__':
    EggsClimber().GoGet()
