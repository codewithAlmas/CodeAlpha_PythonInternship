# Import the random module to select a random word
import random

# List of words for the Hangman game
words = ["python", "apple", "table", "chair", "ocean"]

# Randomly choose one word from the list
word = random.choice(words)

# List to store correctly guessed letters
guessed = []

# Number of chances the player gets
tries = 6

# Welcome message
print("Welcome to Hangman!")

# Main game loop runs until tries become 0
while tries > 0:

    # Empty string to display guessed letters and blanks
    display = ""

    # Check each letter in the selected word
    for letter in word:

        # If letter is guessed, show the letter
        if letter in guessed:
            display += letter + " "

        # Otherwise show underscore
        else:
            display += "_ "

    # Print the current progress of the word
    print(display)

    # Check if all letters are guessed
    if "_" not in display:
        print("You won!")
        break

    # Take input from the user
    guess = input("Guess a letter: ").lower()

    # Check if guessed letter exists in the word
    if guess in word:

        # Add correct letter to guessed list
        guessed.append(guess)

        print("Correct!")

    else:
        # Reduce tries for wrong guess
        tries -= 1

        print("Wrong! Tries left:", tries)

# If tries become 0, player loses
if tries == 0:
    print("You lost! The word was:", word)






    