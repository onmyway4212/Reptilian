from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup

wordFile = urlopen('http://www.pythonscraping.com/pages/AWordDocument.docx').read()
wordFile = BytesIO(wordFile)
document = ZipFile(wordFile)
xml_content = document.read('word/document.xml')

wordobj = BeautifulSoup(xml_content.decode('utf-8'), 'html.parser')
textString =wordobj.findAll("w")
print(xml_content.decode('utf-8'))
'''
for i in textString:
    print(i)
'''
