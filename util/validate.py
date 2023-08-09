import re


def is_email(email: str):
    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(email_pattern, email):
        return True
    else:
        return False

