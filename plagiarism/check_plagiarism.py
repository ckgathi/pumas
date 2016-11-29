import PyPDF2
from difflib import SequenceMatcher, Differ
from docx import Document
from plagiarism import NotPdfFormartError


class Plagiarism(object):

    def conver_pdf_to_txt(self, pdf_file_name):
        if not pdf_file_name[-4:] == '.pdf':
            raise NotPdfFormartError("The file that is being converted to a .txt file should be a .pdf file")
        pdf_file = open(pdf_file_name, 'rb')
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        number_of_pages = read_pdf.getNumPages()
        num = 0
        txt_file = pdf_file_name[:-3] + 'txt'
        f = open(txt_file, 'wb')
        while num < number_of_pages:
            page = read_pdf.getPage(num)
            page_content = page.extractText()
            f.write(page_content.encode('utf-8'))
            num += 1
        return txt_file

    def convert_docx_to_txt(self, docx_file_name):
        document = Document(docx_file_name)
        txt_file = docx_file_name[:-4] + 'txt'
        f = open(txt_file, 'wb')
        for p in document.paragraphs:
            f.write(p.text.encode("utf-8"))
            f.write('\n'.encode("utf-8"))

    def plagiarism_results(self, file1, file2):
        with open(file1) as file_1, open(file2) as file_2:
            file1_data = file_1.read()
            file2_data = file_2.read()
            similarity_ratio = SequenceMatcher(None, file1_data, file2_data).ratio()
            return similarity_ratio

    def doc_differences(self, file1, file2):
        diff_file1 = '/Users/ckgathi/Desktop/diff_file.txt'
        f = open(diff_file1)
        with open(file1) as file_1, open(file2) as file_2:
            file1_data = file_1.read()
            file2_data = file_2.read()
            d = Differ()
            result = list(d.compare(file1_data, file2_data))
            return result
