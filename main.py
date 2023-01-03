# this is the explanation of the project    
from PyPDF2 import PdfReader
# we can import the following classes from the PyPDF library
# the first is the PdfReader class
# the second is the PdfWriter class
# the third is the PdfMerger class 

# there is the method called 'the page'.extract_text() which extracts the text from the page 

# lets import naturall language detection library called langdetect
import langdetect
# this is the papchake that is unknowen to support uzbek language
# we have to immport the documentation to the text file

reader = PdfReader('vocabulary.pdf')
numberOfPages = len(reader.pages)
for i in range(numberOfPages):
    page = reader.pages[i]
    text = page.extract_text()
    # so this is the point where we are getting the page extracted as a text
    # i think we need another for loop to extract the information from the page we gotytujtyujopijaerfg9oi
    print(type(text))


print(numberOfPages) 
open('theTxtfile.txt', 'w')