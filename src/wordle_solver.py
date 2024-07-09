from utils import load_words, filter_words, get_feedback
from entropy import calc_word_score

class WordleSolver:
    def __init__(self, wordlist_path, answerlist_path, verbose = True):
        self.words = load_words(wordlist_path)
        self.answers = load_words(answerlist_path)
        self.current_words = self.words[:]
        self.verbose = verbose

    def make_guesses(self):
        scores = calc_word_score(self.current_words, self.answers)
        return scores[:5]
    
    def update_words(self, guess, feedback):
        self.current_words = filter_words(self.current_words, guess, feedback)
        self.answers = filter_words(self.answers, guess, feedback)

    def recommend_guesses(self):
        top_guesses = self.make_guesses()
        if self.verbose:
            print("These are the top 5 guesses:")
            for word, entropy, probability, total_score in top_guesses:
                print(f"Word: {word}, Entropy: {entropy:.2f}, Probability: {probability:.2f}, Total Score: {total_score:.2f}")
        return top_guesses
    
    # for simulator
    def reset(self):
        self.current_words = self.words[:]
        self.answers = load_words('data/answerlist.txt')

    def solve(self, solution):
        self.reset()
        attempts = 0
        while attempts < 6:
            top_guesses = self.recommend_guesses()
            guess = top_guesses[0][0]
            feedback = get_feedback(guess, solution)
            attempts+=1
            if feedback == 'GGGGG':
                return attempts
            self.update_words(guess, feedback)
            
        return attempts