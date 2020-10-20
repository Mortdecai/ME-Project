import sys
import subprocess

from os import path
from docxcompose.composer import Composer
from docx import Document
from docx2pdf import convert
from pathlib import Path

try:
    from comtypes import client
except ImportError:
    # system is linux
    client = None

root = str(path.dirname(path.realpath(__file__)))

def docx_to_pdf_linux(doc):
    cmd = 'libreoffice --convert-to pdf'.split() + [doc]
    p = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    p.wait(timeout=10)
    stdout, stderr = p.communicate()
    if stderr:
        raise subprocess.SubprocessError(stderr)

def docx_to_pdf(doc):
    doc = path.abspath(doc)
    if client is None:
        return docx_to_pdf_linux(doc)

    name, ext = path.splitext(doc)
    convert(doc, name + '.pdf')
    return
    try:
        word = client.CreateObject('Word.Application')
        worddoc = word.Documents.Open(doc)
        worddoc.SaveAs(name + '.pdf', FileFormat=17)
        worddoc.Close()
        word.Quit()
    except Exception:
        raise

def enum_documents(directory):
    files = []
    for file in Path(directory).rglob('*.docx'):
        files.append(str(file))
    files.sort()
    return files

def merge_documents(files, output):
    merged_doc = Document()
    merger = Composer(merged_doc)
    for file in files:
        merger.append(Document(file))
    merger.save(output)
    docx_to_pdf(output)

def main(argv):
    n = len(argv)
    if n > 0:
        if n == 1:
            merge_documents(enum_documents(path.abspath(argv[0])), path.join(root, 'output.docx'))
        else:
            merge_documents(enum_documents(path.abspath(argv[0])), path.abspath(argv[1]))

main(sys.argv[1:])
