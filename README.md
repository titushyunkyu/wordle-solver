# Wordle Solver

## Wordle solver in Python utilizing information theory

A Python-based Wordle solver that uses information theory concepts such as entropy and probability to recommend the best possible guesses. This solver aims to efficiently solve Wordle puzzles by calculating the information 
gain of each guess and selecting the optimal word based on combined entropy and probability scores. The list of valid words contain the 12,792 accepted words from the Wordle dictionary and the list of valid answers contain 2,309 possible solutions published by Wordle.

## Features
  * Calculates entropy and probability for each guess
  * Recommends the top 5 guesses based on combined scores
  * Parallel processing for improved performance
  * Simulator to measure performance and average number of guesses required to solve the Wordle.
     - Average performance after 100 simulations: 3.42 guesses per word

## Installation
1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/wordle-solver.git
    cd wordle-solver
    ```
2. Set up a virtual environment and install dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```
## Usage
1. Place your word list and answer list in the `data` directory:

    ```
    wordle_solver/
    ├── data/
    │   └── wordlist.txt
    │   └── answerlist.txt
    ```

2. Run the solver interactively:

    ```bash
    python src/main.py
    ```

    The solver will recommend the top 5 guesses based on the entropy and probability scores. You can input your guesses and feedback to interactively solve the Wordle puzzle. For feedback, type G for green, Y for yellow, and N for gray (e.g. GNNYN)

### Running the Simulator

To measure the average number of guesses required to solve puzzles, use the simulator:

    ```bash
    python simulator/simulator.py
    ```

    The simulator will run a specified number of simulations and print the average number of attempts needed to solve the puzzles.

## Project Structure

    ```
    wordle_solver/
    ├── data/
    │   └── wordlist.txt        # List of valid words for guesses
    │   └── answerlist.txt      # List of possible answers
    ├── src/
    │   ├── __init__.py
    │   ├── main.py             # Entry point for the interactive solver
    │   ├── wordle_solver.py    # Core logic for solving Wordle
    │   ├── entropy.py          # Functions for entropy calculation
    │   └── utils.py            # Utility functions
    │   └── simulator.py        # Script for running simulations
    └──  README.md

## Contact
For any questions or suggestions, please open an issue or contact me at hvm4sg@virginia.edu
