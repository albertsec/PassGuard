import string
from getpass import getpass

print("================================")
print("       PASSGUARD v1.0")
print("================================")
print("Password Security Checker")
print("Welcome!")


def check_length(pw):
    if len(pw) < 8:
        return 0
    elif len(pw) < 12:
        return 1
    else:
        return 2


def check_lowercase(pw):
    for char in pw:
        if char.islower():
            return True

    return False


def check_uppercase(pw):
    for char in pw:
        if char.isupper():
            return True

    return False


def check_digit(pw):
    for char in pw:
        if char.isdigit():
            return True

    return False


def check_symbol(pw):
    for char in pw:
        if char in string.punctuation:
            return True

    return False


def calculate_score(pw):
    score = check_length(pw)

    if check_lowercase(pw):
        score += 1

    if check_uppercase(pw):
        score += 1

    if check_digit(pw):
        score += 1

    if check_symbol(pw):
        score += 1

    return score


def get_strength(score):
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


def load_common_passwords():
    with open("common_passwords.txt", "r", encoding="utf-8") as file:
        passwords = set()

        for line in file:
            password = line.strip().lower()

            if password:
                passwords.add(password)

    return passwords


def is_common_password(pw, common_passwords):
    return pw.lower() in common_passwords


def get_tips(pw):
    tips = []

    if len(pw) < 12:
        tips.append("Use at least 12 characters")

    if not check_lowercase(pw):
        tips.append("Add lowercase letters")

    if not check_uppercase(pw):
        tips.append("Add uppercase letters")

    if not check_digit(pw):
        tips.append("Add at least one digit")

    if not check_symbol(pw):
        tips.append("Add at least one special symbol")

    return tips


common_passwords = load_common_passwords()

password = getpass("\nEnter your password: ")

score = calculate_score(password)

is_common = is_common_password(password, common_passwords)

if is_common:
    strength = "Weak"
else:
    strength = get_strength(score)

print("\n================================")
print("       PASSWORD REPORT")
print("================================")

print("Score:", score, "/ 6")
print("Strength:", strength)

if is_common:
    print("WARNING: This is a common password!")

print("\nTips:")

tips = get_tips(password)

if tips:
    for tip in tips:
        print("-", tip)
else:
    print("No improvements needed!")

