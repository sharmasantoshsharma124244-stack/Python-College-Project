# Python-College-Project
# Hangman Game (Python)

## 1. Project Overview
A command-line word-guessing game. The computer randomly picks a secret word and the player guesses it one letter at a time. The player loses after 6 wrong guesses.

## 2. Objectives
- Practice functions, loops, conditionals, sets and strings
- Implement input validation (single alphabetic letter only)
- Use the `random` module to select a word
- Build a replayable game loop

## 3. Features
- Random word selection from a bank of 10 words
- Progress display with underscores (e.g. `p _ t h _ n`)
- Shows wrong letters guessed and wrong-guess counter (x/6)
- Invalid inputs (numbers, symbols, empty, multiple letters) do not reduce chances
- Repeated guesses do not reduce chances
- Case-insensitive input (`P` and `p` are the same)
- "Play again?" option after every game
- `play_hangman(secret_word)` accepts an optional word, which makes testing easy

## 4. Requirements
- Python 3.8 or above
- No external libraries (uses only the built-in `random` module)

## 5. Files
| File | Purpose |
|------|---------|
| `one.py` | Complete game code |
| `README.md` | Project documentation |
| `words.txt` | Reference list of the words used in the game's word bank |
| `screenshots.pdf` | Screenshots of all test cases |

## 6. How to Run
```bash
python3 one.py
```

## 7. Game Rules
1. The computer selects a random word from `WORDS`.
2. Guess one letter at a time.
3. A maximum of **6 wrong guesses** is allowed.
4. Repeated guesses and invalid inputs are not counted as wrong.
5. Guess all letters to win; use all 6 wrong guesses and you lose.

## 8. Input / Output Details
**Input:** a single letter per turn; `y`/`n` (or `yes`/`no`) to play again.
**Output:** current word progress, wrong-guess count, incorrect letters, and win/lose messages.

Sample output:
```
Word: _ _ _ _ _ _
Wrong guesses: 0/6
Incorrect letters: None

Enter a letter: p
Correct! The letter 'p' is in the word.

Word: p _ _ _ _ _
```

## 9. Test Cases
To test with a fixed word, run in the Python shell:
```python
import one
one.play_hangman("python")
```

| # | Secret Word | Input | Expected Output |
|---|-------------|-------|-----------------|
| 1 | python | p, y, t, h, o, n | "Congratulations! You won the game!" |
| 2 | python | z, x, q, w, v, u | Chances drop 5,4,3,2,1,0 then "GAME OVER!" and correct word shown |
| 3 | python | `1` | "Invalid input. Please enter a single letter." (no chance lost) |
| 4 | python | `ab` | "Invalid input..." (no chance lost) |
| 5 | python | empty input (press Enter) | "Invalid input..." (no chance lost) |
| 6 | python | p, then p again | "You already guessed 'p'. Try another letter." |
| 7 | python | z, then z again | Wrong guess once; repeat shows "already guessed", no extra penalty |
| 8 | python | `P` (uppercase) | Treated as `p`: "Correct!" |
| 9 | any | After game, enter `y` | "Starting a new game..." |
| 10 | any | After game, enter `n` | "Thank you for playing Hangman. Goodbye!" |
| 11 | any | After game, enter `maybe` | "Please enter 'y' for yes or 'n' for no." |

## 10. Author
Name: santosh sharma  |  Roll No: ___33___  |  Section: B2
@SATYAPRAKASHSETHY
