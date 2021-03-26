from pdf2docx import Converter

pdf_file = 'C:/Users/EDZ/Desktop/ruan/3.pdf'
docx_file = 'C:/Users/EDZ/Desktop/ruan/1.docx'

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file, start=0, end=None)
cv.close()

