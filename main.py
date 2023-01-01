# this is the explanation of the project    
from PyPDF2 import PdfReader
# we can import the following classes from the PyPDF library
# the first is the PdfReader class
# the second is the PdfWriter class
# the third is the PdfMerger class 

# there is the method called 'the page'.extract_text() which extracts the text from the page 


reader = PdfReader('vocabulary.pdf')
numberOfPages = len(reader.pages)
for i in range(numberOfPages):
    text = page.extract_text()
    page = reader.pages[i]
    # so this is the point where we are getting the page extracted as a text
    # i think we need another for loop to extract the information from the page we gotytujtyujopijaerfg9oi
    

print(numberOfPages)