import hashlib
import os

def password_hash(password, salt, iterations):
    hashed_password = password

    for _ in range(iterations):
        salted_password = hashed_password + salt

        hashed_password = hashlib.sha256(salted_password.encode('utf-8')).hexdigest()

    return hashed_password

if __name__ == "__main__":
    password = "qwerty"
    size_of_salt = 10
    salt = str(os.urandom(size_of_salt))

    iterations = 400000
    print("This is salt:",salt)

    hashed_password = password_hash(password, salt, iterations)
    print("Generated Password Hash:", hashed_password)