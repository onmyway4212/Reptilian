import csv
headers = ['ID','UserName','PassWord','age','Country']
rows = [(1001, 'qiye', 'qiye_pass',24, 'china'),
        (1002, 'mary','mary_pass', 20, 'usa'),
        (1003, 'jack', 'jack_pass', 60, 'gbt')]

with open('111.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)