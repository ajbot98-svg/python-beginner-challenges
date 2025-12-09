# Home Work from GPT
# challenge_2
# password strength_checker

password = input("Enter your password: ")
len(password) >= 8
has_number = False
for ch in password:
    if ch.isdigit():
        has_number = True
any (ch.isdigit() for ch in password)
any (ch.islower() for ch in password)
any (ch.isupper() for ch in password)
special = "!@#$%^&*()-+"
any (ch in special for ch in password)
if (len(password) >= 8 and
    any(ch.isdigit() for ch in password) and
    any(ch.islower() for ch in password) and
    any(ch.isupper() for ch in password) and
    any(ch in special for ch in password)):
    print("Strong password")
else:
    print("Weak password")