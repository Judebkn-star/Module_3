# # TODO: Create a string variable with a sentence

# sentence = "Je suis Jude"
# print(sentence)

# # TODO: Convert the string to uppercase

# sentence_upper = sentence.upper()
# print(sentence_upper)

# # TODO: Convert the string to lowercase

# sentence_lower = sentence.lower()
# print(sentence_lower)

# # TODO: Capitalize the first letter of each word
# sentence_title = sentence.title()
# print(sentence_title)

# # TODO: Replace a word in the string

# sentence_replaced = sentence.replace("Je", "Tu").replace("Jude","Moi")
# print(sentence_replaced)



# # TODO: Split the string into a list of words

# sentence_split = sentence.split() 
# print(f' La sentence split est {sentence_split}')


# #  TODO: Check if the string starts with a specific word

# Word_to_check = 'Je'

# if sentence.startswith(Word_to_check):
#     print(f"La phrase commence par {Word_to_check} ")
# else:
#     print(f'La phrase ne commence pas par {Word_to_check}')

# # TODO: Remove leading and trailing whitespace from a string

# sentence_with_spaces = "   Bonjour   "
# print(sentence_with_spaces.strip())   # "Bonjour"
# print(sentence_with_spaces.lstrip())  # "Bonjour   "
# print(sentence_with_spaces.rstrip())  # "   Bonjour"


#Exercice 2 

# name = 'Jude'
# height = '190'
# age = 22

# # TODO: Use the .format() method to create a sentence with these variables
# sentence = "Je m'appelle {n}, je mesure {h}cm et j'ai {a} ans".format(n=name,a=age,h=height)
# print(sentence)

# # TODO: Use f-strings to create the same sentence

# sentence = f"Je m'appelle {name}, je mesure {height}cm et j'ai {age} ans."
# print(sentence)

# sentence = "Je m'appelle %s, je mesure %d, et j'ai %d "


# # TODO: Format a float number to display only two decimal places 

# pi = 3.142546271
# formatted_pi = f"{pi:.2f}"
# print(formatted_pi)  

# #EXERCICE 3 

# # TODO: Create a list of numbers
# numbers = [1,2,4,8,9,22]

# # TODO: Use a for loop to print each number in the list
# for tamerecon in numbers:
#     print(tamerecon)

# # TODO: Create a dictionary and use a for loop to print all keys and values
 
# New_dictionary = {
#     "Numéro": 21,
#     "Chiffre": 2,
#     "Encore": 13
# }

# print(New_dictionary)
 
# for i in New_dictionary:
#     print(i)

# # TODO: Create a dictionary
# dictionary = {
#     "Nom": "Jude",
#     "Âge": 22,
#     "Taille": 190
# }
# print(dictionary)

# # TODO: Use a for loop to print all keys and values

# for i, tamerecon in dictionary.items():
#     print(f'{i}: {tamerecon}')


# # TODO: Use a for loop with range() to print numbers from 1 to 10

# range_example = range(1, 101)

# for i in range_example :
#     print (i)


# City = ["Tamerconcity", "Sonmereconcity", "Tonbabiécity"]

# for i in City:
#     print (i)


#     # Liste de nombres
# numbers = [1, 2, 4, 8, 9, 22]
# squares = [n**2 for n in numbers]

# print(squares)


# TODO: Use a while loop to print numbers from 1 to 10

range_example = range(1,11)
i = 1 

while i < 6:
    print(i)
    i+=1

# TODO: Create a guessing game using a while loop
# (generate a random number and leti the user guess until correct)

import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Initialize guess to something that isn't the secret number yet
guess = None

while guess != secret_number:
    # Ask the user for a guess
    guess = int(input("Guess a number between 1 and 10: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("🎉 Correct! You guessed it!")

# TODO: Use a while loop to calculate the factorial of a number



# TODO: Implement a simple calculator using a while loop
# (continue calculating until the user chooses to exit)



