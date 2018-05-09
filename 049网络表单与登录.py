import requests
params = {'firstname':'zhang', 'lastname':'hao'}
r = requests.post('http://www.pythonscraping.com/pages/files/processing.php', data=params)
print(type(r))
print(r.text)