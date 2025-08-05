# parse_term_sheet.py
import os
os.environ["HOME"] = "/tmp"
os.environ["XDG_CONFIG_HOME"] = "/tmp"
os.environ["STREAMLIT_CONFIG_DIR"] = "/tmp/.streamlit"
os.makedirs("/tmp/.streamlit", exist_ok=True)
import sys
from utils_llm import extract_fields_with_llm

def extract_text_from_file(file_path):
    if file_path.lower().endswith(".pdf"):
        import pdfplumber
        with pdfplumber.open(file_path) as pdf:
            return "\n".join((page.extract_text() or "") for page in pdf.pages)
    elif file_path.lower().endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    # Add .docx support if needed
    else:
        raise NotImplementedError("Add .docx or other format support here as required.")

def extract_term_sheet_fields(file_path):
    text = extract_text_from_file(file_path)
    fields = extract_fields_with_llm(text)
    return fields

if __name__ == "__main__":
    input_fp = sys.argv[1]
    data = extract_term_sheet_fields(input_fp)
    print(data)