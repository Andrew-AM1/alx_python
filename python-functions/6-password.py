#!/usr/bin/python3
def validate_password(password):
    # Checking for password length
    if len(password) < 8:
        return False

    # Checking for uppercase, lowercase, and digit
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True

    # Check for spaces
    if ' ' in password:
        return False

    # Check if all conditions are met
    if not (has_uppercase and has_lowercase and has_digit):
        return False
    else:
        return True