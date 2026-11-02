"""
Project: Hangman Game
Language: Python 3

How to run:
    python3 one.py

Rules:
- The computer selects a word randomly from WORDS.
- Guess the word one letter at a time.
- You can make a maximum of 6 wrong guesses.
- Repeated guesses and invalid inputs do not reduce your chances.
"""

import random


# Word bank: the secret word is selected randomly from this list.
WORDS = [
    "python",
    "computer",
    "programming",
    "keyboard",
    "algorithm",
    "science",
    "college",
    "developer",
    "internet",
    "function",
]


def display_progress(secret_word, correct_guesses):
    """Return the word with unguessed letters shown as underscores."""
    return " ".join(
        letter if letter in correct_guesses else "_"
        for letter in secret_word
    )


def play_hangman(secret_word=None):
    """
    Run one game of Hangman.

    secret_word is optional. It can be supplied for testing;
    otherwise, a random word is selected from WORDS.
    """
    if secret_word is None:
        secret_word = random.choice(WORDS)

    secret_word = secret_word.lower()

    if not secret_word.isalpha():
        raise ValueError("The secret word must contain letters only.")

    correct_guesses = set()
    wrong_guesses = set()
    max_wrong_guesses = 6

    print("\n" + "=" * 38)
    print("          WELCOME TO HANGMAN")
    print("=" * 38)
    print(f"Guess the secret word. It has {len(secret_word)} letters.")
    print(f"You have {max_wrong_guesses} wrong guesses available.")
    print("Enter one letter at a time. Good luck!\n")

    while len(wrong_guesses) < max_wrong_guesses:
        progress = display_progress(secret_word, correct_guesses)
        print(f"Word: {progress}")
        print(
            f"Wrong guesses: {len(wrong_guesses)}/"
            f"{max_wrong_guesses}"
        )

        if wrong_guesses:
            print("Incorrect letters:", ", ".join(sorted(wrong_guesses)))
        else:
            print("Incorrect letters: None")

        guess = input("\nEnter a letter: ").strip().lower()

        # Validate input: exactly one alphabetic character is required.
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.\n")
            continue

        # Do not penalize the player for entering the same letter again.
        if guess in correct_guesses or guess in wrong_guesses:
            print(f"You already guessed '{guess}'. Try another letter.\n")
            continue

        if guess in secret_word:
            correct_guesses.add(guess)
            print(f"Correct! The letter '{guess}' is in the word.\n")

            # Check whether every letter in the secret word was guessed.
            if all(letter in correct_guesses for letter in secret_word):
                print(f"Word: {display_progress(secret_word, correct_guesses)}")
                print("\nCongratulations! You won the game!")
                print(f"The word was: {secret_word}")
                return True
        else:
            wrong_guesses.add(guess)
            remaining = max_wrong_guesses - len(wrong_guesses)
            print(f"Wrong guess! You have {remaining} chance(s) left.\n")

    print("\nGAME OVER!")
    print(f"You used all {max_wrong_guesses} wrong guesses.")
    print(f"The correct word was: {secret_word}")
    return False


def main():
    """Start the game and ask whether the player wants another round."""
    print("This is a word-guessing game. Find the hidden word!")

    while True:
        play_hangman()

        while True:
            play_again = input("\nWould you like to play again? (y/n): ")
            play_again = play_again.strip().lower()

            if play_again in ("y", "yes"):
                print("\nStarting a new game...")
                break
            elif play_again in ("n", "no"):
                print("\nThank you for playing Hangman. Goodbye!")
                return
            else:
                print("Please enter 'y' for yes or 'n' for no.")


if __name__ == "__main__":
    main()
