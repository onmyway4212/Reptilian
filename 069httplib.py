import requests
#https://www.baidu.com/s?tn=baiduhome_pg&rsv_idx=2&wd=github%E4%B8%AD%E6%96%87%E7%89%88&rsv_crq=6&bs=github
payload = {'tn': 'baiduhome_pg',
           'rsv_idx': 2,
           'wd': 'github%E4%B8%AD%E6%96%87%E7%89%88',
           'rsv_crq': 6,
           'bs': 'github'}
r = requests.get('https://www.baidu.com/s', params=payload)
print(r.url)
