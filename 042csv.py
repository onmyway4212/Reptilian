import csv

csvFile = open('d://1.csv', 'w+')     #w以写入的方式打开文件。+可读写模式
try:
    writer = csv.writer(csvFile)
    writer.writerow(('number', 'number plus 2', 'number times 2'))
    for i in range(10):
        writer.writerow((i, i+2, i*2))
finally:
    csvFile.close()
