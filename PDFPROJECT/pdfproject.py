import PyPDF2
import sys

inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')


pdf_combiner(inputs)

# aqui o que foi feito foi apenas printar os PDFs selecionados quando abrimos o terminal
# os argv possibilitando e o inputs sendo printados
