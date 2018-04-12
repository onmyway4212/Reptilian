import urllib.request
import re

def url_open():
    url = 'http://www.e0575.com/'
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')
    return html

def get_title():
    html = url_open()
    p = r'<a href="articleshow.php\?.*?">'
    title = re.findall(p, html)
    for each in title:
        name = each.split('=')[-1]
    print(name)


if __name__ == '__main__':
    get_title()

