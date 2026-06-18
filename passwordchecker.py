password=input ("Enter your password:")
if len(password) >= 8:
    has_number = any(char.isdigit() for char in password)
    has_letter = any(char.isalpha() for char in password)
    has_special = any(not char.isalnum() for char in password)

    if has_number and has_letter and has_special:
        print("Password is strong!")
    else:
        print("Password must contain letters, numbers, and a special character.")
else:
    print("Password must be at least 8 characters long.")
    
   