# source: https://stackoverflow.com/a/66996324

import pytesseract
from pdf2image import convert_from_path
# pdf2image requires poppler on windows: https://github.com/Belval/pdf2image#windows
import glob

pdfs = glob.glob(r".\samplePDFs\*.pdf")

for pdf_path in pdfs:
    pages = convert_from_path(pdf_path, 500, poppler_path = r".\poppler-23.01.0\Library\bin")

    for pageNum,imgBlob in enumerate(pages):
        text = pytesseract.image_to_string(imgBlob,lang='eng')

        with open(f'{pdf_path}.txt', 'a') as the_file:
            the_file.write(text)