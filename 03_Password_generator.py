import random
import string

def generate_password(length):
    # Defining the characters that will be used in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Generating a random password of the specified length
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def main():
    # Prompting the user to specify the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired length for the password: "))
            if length <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print(f"Generated Password: {password}")

# Run the main function
if __name__ == "__main__":
    main()
