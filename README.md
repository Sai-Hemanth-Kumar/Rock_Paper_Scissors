# Rock, Paper, Scissors Game

This is a simple command-line implementation of the classic Rock, Paper, Scissors game in Python. The game allows you to play against the computer, which makes its choices randomly using Python's built-in `random` module.

## How to Play

1. **Run the Game**
   - Make sure you have Python installed on your system.
   - Open a terminal or command prompt in the project directory.
   - Run the following command:
     ```bash
     python RPS.py
     ```

2. **Gameplay**
   - You will be prompted to enter your choice: `rock`, `paper`, or `scissors`.
   - The computer will randomly select its choice.
   - The result of the round will be displayed:
     - If both choices are the same, it's a tie.
     - Rock beats scissors, scissors beats paper, and paper beats rock.
     - The winner is announced, or you are told if you lose.
   - After each round, you can choose to play again or exit the game.

## Example Game Session
```
Choose rock, paper, or scissors: rock
You chose rock and the computer chose scissors.
You win!
Do you want to play again? (yes/no) : yes
Choose rock, paper, or scissors: paper
You chose paper and the computer chose rock.
You win!
Do you want to play again? (yes/no) : no
```

## How It Works
- The game uses the `random` module to let the computer make a random choice between `rock`, `paper`, and `scissors` each round:
  ```python
  computer_choice = random.choice(options)
  ```
- User input is validated to ensure only valid options are accepted.
- The game continues in a loop until you choose to stop playing.

## Requirements
- Python 3.x

No external libraries are required.