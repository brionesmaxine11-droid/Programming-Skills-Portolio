# Exercise 8: Simple Search - 30 Marks
# Maxine Briones - CS4

names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
user = input("Who are you searching for in the list? ")   # Allow the user to input the search term instead of using a predefined value.
                                                          # Implement the search functionality based on user input.
if user in names:
    print(f"{user}'s name is in the list.")
else:
    print(f"{user}'s name is not in the list.")