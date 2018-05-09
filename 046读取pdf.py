from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from io import open

def readPDF(pdfFile):
    rscmgr = PDFResourceManager()
    retsrt = StringIO()
    laparams = LAParams()
    device = TextConverter(rscmgr, retsrt, laparams=laparams)

    PDFPage.get_pages(rscmgr, device, pdfFile)
    device.close()

    content = retsrt.getvalue()
    retsrt.close()
    return content

pdfFile = urlopen('http://www.pythonscraping.com/pages/warandpeace/chapter1.pdf')
outputString = readPDF(pdfFile)
print(outputString)
pdfFile.close()
