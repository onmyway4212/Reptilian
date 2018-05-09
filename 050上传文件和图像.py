import requests

files = {'uploadFile':open(r'F:\record2.txt', 'rb')}
r = requests.post('http://www.pythonscraping.com/files/processing2.php', files=files)
print(r.text)