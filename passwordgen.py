import random
import string
import os

def generate_password(length):
    """
    Function that generates a secure random password based on the provided length.
    """
    uppercase_loc = random.randint(1, 4)
    symbol_loc = random.randint(5, 6)
    lowercase_loc = random.randint(7, 12)
    password = ''
    pool = string.ascii_letters + string.digits + string.punctuation

    for i in range(length):
        if i == uppercase_loc:
            password += random.choice(string.ascii_uppercase)
        elif i == lowercase_loc:
            password += random.choice(string.ascii_lowercase)
        elif i == symbol_loc:
            password += random.choice(string.punctuation)
        else:
            password += random.choice(pool)

    return password

def save_password_to_txt(name, password):
    """
    Function that saves the password to a .txt file with the provided name.
    """
    save_path = './'  # current directory
    file_name = name + ".txt"
    complete_name = os.path.join(save_path, file_name)

    with open(complete_name, "w") as file:
        file.write(password)

# User input
while True:
    try:
        password_length = int(input("Enter the desired password length: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")

user_name = input("For whom is this password? ")

# Generate the password
generated_password = generate_password(password_length)

# Display the generated password
print("Generated password:", generated_password)

# Save the password to a .txt file
save_password_to_txt(user_name, generated_password)
