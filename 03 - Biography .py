# Exercise 3: Biography - 25 Marks
# Maxine Briones - CS4

personal_info = {                   #Store the information (name, hometown, and age) as key-value pairs in a dictionary.
    "name": "Maxine Briones",
    "hometown": "Laon, Abucay",
    "age": 18}

print(personal_info["name"])         # Print the values on separate lines using a single print() statement.
print(personal_info["hometown"])     # Use variables with appropriate data types for each piece of information.
print(personal_info["age"])


#Advanced Requirements
print("! Advanced Requirements ! \n")
name = (input("Enter your name: "))
hometown = (input("Enter your hometown: "))
age = int(input("Enter your age: "))

personal_info = {
    "name": name,
    "hometown": hometown,
    "age": age
}

print(personal_info["name"])
print(personal_info["hometown"])
print(personal_info["age"])

'''Answer: We end up having to add the input function in order for the user to be able to enter their 
information directly on the terminal. They can put both first and second name, or any other number 
of words in the name input since Python will automatically read the information as all together on that 
specific input. If someone were to enter a string value for age, it would give a value error since the 
code only understands numeral value due to the type “int”. An easy way to fix this is to specify in the 
age input to only use numbers (e.g “Enter your age in numbers: ”) or to remove int so that both numbers 
and letters are allowed.'''
