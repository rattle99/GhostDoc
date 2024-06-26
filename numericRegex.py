import re

def validate_credit_card(text):
    patterns = [
        r'\b(?:3[47]\d{2})([-\s]?)\d{6}\1\d{5}\b',  # American Express
        r'\b(?:3\d{3})([-\s]?)\d{6}\1\d{4}\b',      # Diners Club
        r'\b(?:6011)([-\s]?)\d{4}\1\d{4}\1\d{4}\b', # Discover
        r'\b(?:2131|1800|35\d{2})([-\s]?)\d{4}\1\d{4}\1\d{4}\b', # JCB
        r'\b(?:5[1-5]\d{2}|2221|222[2-9]|22[3-9]\d{1}|2[3-6]\d{2}|27[01]\d{1}|2720)([-\s]?)\d{4}\1\d{4}\1\d{4}\b', # MasterCard
        r'\b(?:4\d{3})([-\s]?)\d{4}\1\d{4}\1\d{4}\b' # Visa
    ]
    return any(re.search(pattern, text) for pattern in patterns)

def validate_social_security_number(text):
    pattern = r'(^|(?<=\D\W))(?!(000|666|9))[0-9]{3}[ \t\-]{0,3}(?!00)[0-9]{2}[ \t\-]{0,3}(?!0000)[0-9]{4}(?=(\W\D|$))'
    return bool(re.search(pattern, text))

def validate_phone_number(text):
    pattern = r"\(?\b(\d{3})\)?[-.●]?(\d{3})[-.●]?(\d{4})\b"
    return bool(re.search(pattern, text.replace(" ", "")))

def validate_account_number(text):
    pattern = r'\b[0-9]{10,12}\b'
    return bool(re.search(pattern, text))


def regexCheck(text):
    if(validate_credit_card(text) or  validate_social_security_number(text) or validate_phone_number(text) or validate_account_number(text)):
        return True
    else:
        return False




# Example usage:
#text = "Your Visa card number is 4111-1111-1111-1111 and your SSN is 123-45-6789. You can reach me at (123) 456-7890."

# print(validate_credit_card("4123-4567-8910-1119"))            # Should return True
# print(validate_social_security_number("123-45-6789")) # Should return True
# print(validate_phone_number("(123) 456-7890"))           # Should return True
# print(validate_account_number("12"))         # Should return False (no account number in text)


# one function which does not match any name in faker
# if multiple entity_group ->
# original->fake
# original->if no fake function, generate with new custom faker function

