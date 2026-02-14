import random

with open("random_user.txt", "w") as file:                       # Create the file if it doesn't exist and write the header
    file.write("ID          USERNAME           PASSWORD\n")

with open("random_user.txt", "r") as file:
    existing_accounts = [account.strip() for account in file.readlines()[1:]]  # Skip the header line

name = input("Enter your First name: ")  # Get the user's name (not used in username generation, but can be stored if needed)

n = 10 - len(name)  # Calculate the number of random characters needed to make the total length 10

username = name.upper() +'-' + "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=n))  # Generate a random username with a prefix "ABHAY-" followed by 4 random characters

password = "".join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*", k=10))  # Generate a random password of length 12

def auto_increment():                
    with open ("random_user.txt", "r") as f:
        num = f.readlines()
        X = len(num)
    return str(X)
    


with open("random_user.txt", "a") as file:
    file.write(f"{auto_increment()}{' '*11}{username}{' '*9}{password}\n")
    
print("Account created successfully!!!")
print("Your account details are:")
print(f"ID: {len(existing_accounts)+1}")
print(f"Username: {username}")
print(f"Password: {password}")


# This code creates a simple account manager that generates a random username based on the user's first name and a random password for a new account. 
# The account details are stored in a text file called "random_user.txt". 
# Each account is assigned a unique ID that auto-increments based on the number of existing accounts.