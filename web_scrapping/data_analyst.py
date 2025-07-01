import re

def extract_contacts(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read()

        # Regular expression patterns
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        phone_pattern = r'\+234 \d{3} \d{3} \d{4}'

        # Extract email addresses and phone numbers
        emails = re.findall(email_pattern, text)
        phone_numbers = re.findall(phone_pattern, text)

        return emails, phone_numbers

    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
        return None, None

def save_contacts(emails, phone_numbers):
    try:
        with open('emails.txt', 'w') as file:
            for email in emails:
                file.write(email + '\n')

        with open('phone_numbers.txt', 'w') as file:
            for phone_number in phone_numbers:
                file.write(phone_number + '\n')

        print("Email addresses and phone numbers have been saved to emails.txt and phone_numbers.txt respectively.")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    file_name = 'reviews.txt'
    emails, phone_numbers = extract_contacts(file_name)

    if emails is not None and phone_numbers is not None:
        save_contacts(emails, phone_numbers)

