# OCR
> built & *tested* using Python 3.11.2

Minimal version of Python script that finds PDF files in speficied directory, *converts* them into .txt files using [Python Tesseract](https://github.com/madmaze/pytesseract) & saves final files in same directory as original PDF files.

## Installation (on windows 10<!--; tested manually-->)
1. clone repo
2. enter repo directory: `cd ocr`
3. install [*Python tesseract*](https://github.com/madmaze/pytesseract#installation)
4. create virtual environment: `py -m venv venv`
5. activate virtual environment: `venv\Scripts\activate.bat`
6. update pip: `py -m pip install --upgrade pip`
7. install requirements: `pip install -r requirements.txt`
8. run program as described below (*Usage*)

## Usage (on windows 10<!--; tested manually-->)
1. run `py ocr.py`
2. follow instructions & prompts of program

## Quickstart
1. run `py ocr.py`
2. press Enter to use sample PDFs in `./samplePDFs` subdirectory by default

## What happens
`ocr.py` creates .txt files with content of all PDFs in given directory 
- for each PDF in target directory (default: `./samplePDFs`): pdf2image module used to convert PDFs in into images
  - for each image
    - pytesseract module used to convert text in image to string, then appends text to .txt file with name of original PDF & saves alongside original PDF
- process takes up to 10 minutes
- content of `./samplePDFs` expected to look like `./samplePDFsResult` eventually

## Resources
- [pytesseract installation](https://github.com/madmaze/pytesseract#installation)
- [guidance installation video](https://youtu.be/PY_N1XdFp4w?t=54)
- [sample application](https://stackoverflow.com/a/66996324)

### sample PDFs
- https://www.africau.edu/images/default/sample.pdf
- https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf
- https://www.adobe.com/support/products/enterprise/knowledgecenter/media/c4611_sample_explain.pdf
- https://unec.edu.az/application/uploads/2014/12/pdf-sample.pdf
- https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/
- https://www.orimi.com/pdf-test.pdf

## Limitations / Known Issues
- potentially inaccurate - depending on quality, structure & content of input PDFs (images, charts, ...)

## Potential Improvements
- adjust OCR settings to *real world* input PDFs (to achieve best results for expected input)
- create REST API to get share results with clients (long-term?)
  - authentication & encryption (e.g. using JSON Web Token)