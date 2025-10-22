# Exercise 6: Brute Force Attack - 30 Marks
# Maxine Briones - CS4

correct_password = "11111"                                # Define the correct password.

while True:                                               # Use a while loop to repeatedly ask the user for the password until the correct one is entered.
    user = input("Enter the password: ")

    if user == correct_password:
        print("The password is correct. Access granted.") # Output an appropriate message when the correct password is entered.
        break  # stops the loop
    else:
        print("The password is incorrect. Please try again.")


# Advanced Requirements
print("\n ! Advanced Requirements ! \n")

acorrect_password = "55555"

max_attempts = 5
attempt = 0

while attempt < max_attempts:
    auser = input("Enter the password: ")
    attempt += 1

    if auser == acorrect_password:
        print("The password is correct. Access granted.") 
        break
    else:
        remaining = max_attempts - attempt
        if remaining > 0:
            print(f"The password is incorrect. You have {remaining} attempt(s) left. \n")
        else:
            print("You have run out of attempts. The authorities have been alerted.")