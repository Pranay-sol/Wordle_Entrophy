from wordle_ig import wordle
from info_theory import next_best_guess, entrophy
from answer_key import guesses, answers

def wordle_helper():
    guess = answers
    for word,score in wordle():
        if sum(score) != 10:
            print('calculating next best guess')
            rank,guess = next_best_guess(word, score,guess)
            print(f"{'rank':<5} {'word':<10} {'E[Info]':>8}")
            for i, (word, info) in enumerate(list(rank.items())[0:10], start=1):
                print(f"#{i:<4} {word:<10} {info:>8.4f}")

wordle_helper()



