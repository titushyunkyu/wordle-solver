from wordle_solver import WordleSolver
from utils import load_words
import random

def run_simulation (wordlist_path, answerlist_path, num_simulations = 10):
    solver = WordleSolver('data/wordlist.txt', 'data/answerlist.txt', verbose=False)
    possible_answers = load_words('data/answerlist.txt')

    random_answers = random.sample(possible_answers, num_simulations)
    total_attempts = 0
    for answer in random_answers:
        attempts = solver.solve(answer)
        total_attempts += attempts
        print(f"Solves {answer} in {attempts} attempts.")

    average_attempts = total_attempts / num_simulations
    return average_attempts

if __name__ == "__main__":
    wordlist_path = 'data/wordlist.txt'
    answerlist_path = 'data/answerlist.txt'

    num_simulations = 50

    average_attempts = run_simulation(wordlist_path, answerlist_path, num_simulations)
    print(f"Average number of attempts: {average_attempts:.2f}")