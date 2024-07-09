import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from wordle_solver import WordleSolver

def main():
    wordlist_path = 'data/wordlist.txt'
    answerlist_path = 'data/answerlist.txt'
    print
    solver = WordleSolver(wordlist_path, answerlist_path)

    while True:
        solver.recommend_guesses()

        guess = input("Enter your guess: ").strip().lower()
        # G for green, Y for yellow, and N for gray
        feedback= input("Enter the feedback (e.g. GNNYN): ").strip().upper()

        if feedback == 'GGGGG':
            print("Congratulations! You solved it!")
            break

        solver.update_words(guess, feedback)

if __name__ == "__main__":
    main()
