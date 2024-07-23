import PyPDF2
import itertools

def brute_force_pdf_password(file_path, max_length):
    charset = '0123456789'  # Only numeric characters
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        for length in range(1, max_length + 1):
            for attempt in itertools.product(charset, repeat=length):
                password = ''.join(attempt)
                print(password)
                try:
                    if reader.decrypt(password):
                        print(f"Success! The password is: {password}")
                        return password
                except Exception as e:
                    print(f"An error occurred: {e}")
                    continue

    print("Password not found.")
    return None

# Example usage
file_path = "C:/Users/HP/OneDrive/College/SEM-5/PYTHON/a_protected.pdf"
max_length = 7  # Adjust the maximum length as needed
brute_force_pdf_password(file_path, max_length)
