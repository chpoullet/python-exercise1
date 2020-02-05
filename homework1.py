# Define the following variables
# name, last_name, species, eye_color, hair_color
# name = 'Lana'
# Prompt user for input and Re-assign these
# name = input('what new name would you like?')
# Print them back to the user as conversation
# Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair color is black.

#Section 2 - Calculate in what year was the person born? and responde back.
# print something like: 'You said you we're 28 hence you were born in 1991!'

name = 'Charlie'
last_name = 'Poullet'
species = 'Human'
eye_colour = 'Blue'
hair_colour = 'Blonde'

print('Hello there! Please input your first name:')
name = input().strip().capitalize()

print('Last name:')
last_name = input().strip().capitalize()

print('Your eye colour:')
eye_colour = input().strip().lower()

print('Hair colour:')
hair_colour = input().strip().lower()

print('Age:')
age = int(input().strip())

year_born = 2020 - age

print(f"Your name is {name} {last_name}, your eye colour is {eye_colour}, your hair is {hair_colour}, you are {age} years old and was born in {year_born}.")

print(f"Your name is {name} {last_name}, your eye colour is {eye_colour}, your hair is {hair_colour}, you are {age} years old and were born in {year_born}.")

