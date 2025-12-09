# Home Work from GPt
# challenge_3
# Username + Password creation system



username = input("Create a username: ")
password = input("Create a password: ")

special = "!@#$%^&*()-+?_=,<>/"

# Validate username
valid_username = len(username) >= 4 and " " not in username

# Validate password
valid_password = (
    len(password) >= 8 and
    any(ch.islower() for ch in password) and
    any(ch.isupper() for ch in password) and
    any(ch.isdigit() for ch in password) and
    any(ch in special for ch in password)
)
if valid_username and valid_password:
    print("Account created successfully!")
else:
    print("invalid username or weak password")    