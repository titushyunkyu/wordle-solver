def load_words(filepath):
    with open(filepath, 'r') as file:
        words = file.read().split()
    return words

def get_feedback(guess, answer):
    feedback = ['']*5
    answer_char = list(answer)

    # check for green
    for i in range(5):
        if guess[i] == answer[i]:
            feedback[i] = 'G'
            answer_char[i] = None
        
    # check for yellow
    for i in range(5):
        if feedback[i] != 'G' and guess[i] in answer_char:
            feedback[i] = 'Y'
            answer_char[answer_char.index(guess[i])] = None
    
    # check for gray
    for i in range(5):
        if feedback[i] == '':
            feedback[i] = 'N'

    return ''.join(feedback)

def filter_words(words, guess, feedback):
    new_words = []
    for word in words:
        if get_feedback(guess, word) == feedback:
            new_words.append(word)
    return new_words
