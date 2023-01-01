# this is the explanation of the project    
from PyPDF2 import PdfReader
import time
# there is the method called 'the page'.extract_text() which extracts the text from the page 


reader = PdfReader('vocabulary.pdf')
numberOfPages = len(reader.pages)
for i in range(numberOfPages):
    page = reader.pages[i]
    text = page.extract_text()
    print(text)
    time.sleep(2)
    

print(numberOfPages)