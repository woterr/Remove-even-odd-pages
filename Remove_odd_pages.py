from pypdf import PdfReader, PdfWriter
import os
from os import listdir
from os.path import isfile, join

cwd = os.getcwd()
onlyfiles = [os.path.join(cwd, f) for f in os.listdir(cwd) if 
os.path.isfile(os.path.join(cwd, f))]
paths = []

for i in onlyfiles:
     x = i.split("/")
     if i.endswith(".pdf"):
          paths.append(x[-1])


for j in paths:
    input_pdf = PdfReader(j)
    name = j.split(".")[0]

    output_pdf = PdfWriter()
    for i in range(len(input_pdf.pages)):
        if i%2 != 0:
            output_pdf.add_page(input_pdf.pages[i])

    output_pdf.write(name + "english.pdf")
    os.remove(j)
