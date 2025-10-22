# Exercise 10: Is it even? - 35 Marks
# Maxine Briones - CS4

def even_or_odd(number):                                                    # The entered number should be passed to a function that determines if the value is even or odd.
    if number % 2 == 0:                                                     # The function should return a message indicating whether the number is even or odd.
        return f"Number {number} is even."
    else:
        return f"Number {number} is odd."
    
def main():
    user = int(input("Enter a number to check if it's odd or even: "))      # The program should ask the user for a number from within the main function.
    answer = even_or_odd(user)

    print(answer)                                                           # The message returned by the function should be printed from within the main function.

if __name__ == "__main__":
 main()