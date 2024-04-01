from PyPDF2 import PdfReader
import itertools

def crack_pdf_password(pdf_file, max_length=8, charset='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
    pdf = PdfReader(pdf_file)
    for password_length in range(1, max_length + 1):
        for password_attempt in itertools.product(charset, repeat=password_length):
            password = ''.join(password_attempt)
            if pdf.decrypt(password) == 1:
                return password
    return None

# Example usage
pdf_file = "CS_00134_XXXXXXXX26_050324204056_YP_monthly.pdf"
password = crack_pdf_password(pdf_file)
if password:
    print(f"Password found: {password}")
else:
    print("Password not found.")
