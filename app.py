def check_password(password):
    """Simple check for password length."""
    if len(password) >= 8:
        return "Strong"
    return "Weak"

if __name__ == "__main__":
    user_pass = input("Create a password: ")
    result = check_password(user_pass)
    print(f"Password strength: {result}")
