import csv
import hashlib
from getpass import getpass

def hash_password(password):
    # Hashing the password using SHA-256
    return hashlib.sha256(password.encode()).hexdigest()

def save_password(username, password):
    with open('passwords.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([username, hash_password(password)])

def get_password(username):
    with open('passwords.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == username:
                return row[1]
    return None

def main():
    print("Welcome to Password Manager!")
    while True:
        print("\nMenu:")
        print("1. Save password")
        print("2. Retrieve password")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = getpass("Enter password: ")
            save_password(username, password)
            print("Password saved successfully!")
            break

        elif choice == '2':
            username = input("Enter username: ")
            password = get_password(username)
            if password:
                print("Retrieved password:", password)
            else:
                print("Password not found!")
                break

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
