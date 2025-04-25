import pytesseract
import re

def extract_text_from_image(image):
    return pytesseract.image_to_string(image)

def extract_fields(text):
    fields = {}
    fields['Name'] = re.search(r"Name[:\-]?\s*(.+)", text)
    fields['Address'] = re.search(r"Address[:\-]?\s*(.+)", text)
    fields['Income'] = re.search(r"Income[:\-]?\s*₹?\s*([\d,]+)", text)
    fields['Loan Amount'] = re.search(r"Loan Amount[:\-]?\s*₹?\s*([\d,]+)", text)
    return {k: v.group(1).strip() if v else "" for k, v in fields.items()}
