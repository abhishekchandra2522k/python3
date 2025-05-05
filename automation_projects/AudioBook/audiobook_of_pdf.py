import pyttsx3
import PyPDF2

book = open('Five_Shakespeare_Sonnets.pdf', 'rb')

pdf_reader = PyPDF2.PdfFileReader(book)

num_pages = pdf_reader.numPages

play = pyttsx3.init()

print('Playing Audio Book')

for num in range(0, num_pages):
    page = pdf_reader.getPage(num) # get each page

    data = page.extractText() # extract text from page

    play.say(data) # say text

    play.runAndWait() # run the text through the engine