#Exercise 5: Days of the Month - 30 Marks
# Maxine Briones - CS4

months = {                                                                 #Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
    }

user_input = int(input("Enter the corresponding number of a month: "))
if user_input in months:                                                   #Input Handling: Ask the user to input the month number.
    print(f"Month {user_input} has {months[user_input]} days!")            #Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.
else:
    print("No month corresponding to the number has been found. Enter a number from 1-12.")

# Advanced Requirement
print("! Advanced Requirements !")

months = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
    }

user_input = int(input("Enter the corresponding number of a month: "))
if user_input in months:
   if user_input == 2:
      year = int(input("Enter the year: "))
      if (year % 400 == 0):
         print(f"Month {user_input} has 29 days during {year}! (Leap Year)")
      else:
         print(f"Month {user_input} has 28 days during {year}!")
   else:
        print(f"Month {user_input} has {months[user_input]} days!")
else:
    print("No month corresponding to the number has been found. Enter a number from 1-12.")