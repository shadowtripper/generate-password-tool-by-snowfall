import secrets
import string

def generate_random_password(length):
    
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


print(generate_random_password(12))