#Name: Jacinda Waters
#Date: 21/05/2025
#Purpose:Assessment GLOBAL EXPLORER QUIZ

# Random Coding
import random
import time

# countries = ["Australia", "France", "Japan", "Ecuador", "New_Zealand", "Sealand", "South_Korea", "Sweden", "United_States", "Wales" ]
countries = ["New_Zealand"]
file.closed()
selected_country = random.choice(countries)


file.closed()
filename = selected_country + ".txt"

with open (filename, 'r') as file:
    lines = file.read().splitlines()



#*****************************************************************************************************************
#Message Stating Rules and Purpose of Game

print("Welcome to the Global Explorer Quiz!")

print("This game was made to celebrate Harmony day at the company!")

print("How to play: The game randomly selects a country and you must guess the country with the full name within 3 attempts\n")

#*****************************************************************************************************************
# Into Section
first_name = input("What is your first name? ").upper()

last_initial = input("What is your last name initial? ").upper()

while True:
    ready = input (f"Hello, {first_name} {last_initial}! Are you ready to start? (yes/no) ").lower()

    if ready == "yes":
        break
    elif ready == "no":
        print("Take a few seconds and let me know when.")
        time.sleep(3)
    else:
        print("Invalid answer. Please enter 'yes' or 'no'.")
        time.sleep(1)


print("Alright! Lets begin!")
time.sleep(3)

# ******************************************************************************************************************
# Game Code Start

attempts = 0
max_attempts = 3
won = False


while attempts < max_attempts:
    print("Here is your hint!: \n")

    random_lines=random.sample(lines, 1)
    # print("Inside of while loop")
    hint = random.choice(lines)
    print(hint)
    


    lines.remove(hint)

    guess = str(input("Your guess: ")).strip().upper()
    attempts += 1


    if guess == selected_country.upper().replace("_", " "):
        print("Well done you guessed right! You must know your countries!")
        won = True
      

        break

    elif attempts<max_attempts:
        print("Not correct, But don't give up hope!")

    else: print(f"Sorry, you ran out of attempts. The country was {selected_country.replace("_", " ")}.")
  



with open("results.txt", "a") as file:
    file.write(f"\n{first_name} {last_initial} - {'WIN' if won else 'LOST'} in {attempts} attempts. Country: {selected_country.replace("_", " ")}\n")

# ****************************************************************************************************************************************************
#Score Board

while True:
    score_board = input("Would you like to view the score board? (yes/no) ").lower()
    if score_board == "yes":
        try:
            with open("results.txt", "r") as file:
                print("\n--- Score Board ---")
                print(file.read())
                print("Thank You for playing!")
        except FileNotFoundError:
            print("No results yet!")
        break
    elif score_board == "no":
        print("Thank you for playing!")
        break
    else:
        print("Invalid answer. Please enter 'yes' or 'no'.")














