import PyPDF2
import sys

inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('super.pdf')
    print('All done!')


def tilt_pdf(fname):

    with open(fname, 'rb') as original:

        original = PyPDF2.PdfFileReader(original)
        output = PyPDF2.PdfFileWriter()

        page = original.getPage(0)
        page.rotateCounterClockwise(90)
        output.addPage(page)

        with open('tilted.pdf', 'wb') as new_file:
            output.write(new_file)
            print('New file saved.')


if __name__ == '__main__':

    pdf_combiner(inputs)
