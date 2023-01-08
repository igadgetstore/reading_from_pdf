# this is the explanation of the project    
from PyPDF2 import PdfReader
# we can import the following classes from the PyPDF library
# the first is the PdfReader class
# the second is the PdfWriter class
# the third is the PdfMerger class 

# there is the method called 'the page'.extract_text() which extracts the text from the page 

# lets import naturall language detection library called langdetect
import langdetect
# we have to immport the documentation to the text file

from googletrans import Translator
translator = Translator(
)

reader = PdfReader('vocabulary.pdf')
numberOfPages = len(reader.pages)


page = reader.pages[1]
text = page.extract_text()
words = text.split()
for i in range(2):
    for word in words:
        if langdetect.detect(word) != 'ko':
            words.remove(word)

print(words, len(words), sep='\n')

translations = translator.translate(words, dest='uz')
# print(translations.text)
for translation in translations:
    print(translation.origin, '=>', translation.text)
