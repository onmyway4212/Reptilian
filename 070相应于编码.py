import requests
r = requests.get('https://www.baidu.com/')
#print('content-->'+ r.content.encode('utf-8'))
print('text-->'+ r.text)
print('enconding-->'+ r.encoding)
r.encoding = 'utf-8'
#print('new text-->' + r.text)