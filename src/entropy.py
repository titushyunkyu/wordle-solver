import math
from collections import defaultdict
from utils import get_feedback_cached
from concurrent.futures import ProcessPoolExecutor

def calculate_entropy(word, possible_answers):
    feedback_counter = defaultdict(list)
    total = len(possible_answers)
    entropy = 0

    for answer in possible_answers:
        feedback = get_feedback_cached(word, answer)
        feedback_counter[feedback].append(answer)

    for feedback, words in feedback_counter.items():
        remaining = len(words)
        probability = remaining / total
        entropy += probability * math.log2(1/probability)

    return entropy

def calc_word_scores_single(word, possible_answers, total_answers):
    entropy = calculate_entropy(word, possible_answers)
    probability = len([ans for ans in possible_answers if get_feedback_cached(word, ans) == 'GGGGG']) / total_answers
    total_score = entropy + probability
    return (word, entropy, probability, total_score)

def calc_word_score(possible_guesses, possible_answers):
    scores = []
    total_answers = len(possible_answers)

    with ProcessPoolExecutor() as executor:
        results = executor.map(calc_word_scores_single, possible_guesses, [possible_answers] * len(possible_guesses), [total_answers] * len(possible_guesses))
        scores = list(results)

    scores.sort(key=lambda x:x[3], reverse=True)
    return scores
