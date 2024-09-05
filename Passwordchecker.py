def password_checker():
    common_passwords = ["123456", "password", "123456789", "qwerty", "abc123", "password1"]
    user_password = input("Enter a password: ")

    if user_password in common_passwords:
        print(f"Use a safer password, {user_password} is compromised.")
    else:
        print("Password is safe.")

password_checker()