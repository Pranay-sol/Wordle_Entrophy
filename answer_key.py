answers = open('Data/wordle-answers-alphabetical.txt')
answers = list(map(lambda s: s.rstrip('\n'), answers.readlines()))

guesses = open('Data/wordle-allowed-guesses.txt')
guesses = list(map(lambda s: s.rstrip('\n'), guesses.readlines())) + answers
