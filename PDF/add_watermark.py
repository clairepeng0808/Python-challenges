import PyPDF2
import sys
import os

filename = sys.argv[1]

template = PyPDF2.PdfFileReader(open(filename, 'rb'))
watermark = PyPDF2.PdfFileReader(open('watermarker.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)
    clean_name = os.path.splitext(filename)[0]

    with open(f'./watermarked/{clean_name}_watermark.pdf', 'wb') as new_file:
        output.write(new_file)

print('All done!')
