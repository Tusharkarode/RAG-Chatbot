import pdfplumber

def load_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


def load_txt(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()
