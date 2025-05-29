from wordle_ig import wordle
from info_theory import next_best_guess
from answer_key import answers

#setting up worldle helper bot in conjunction with a game of wordle
def wordle_helper():
    #intial possible guesses (to be noted that guesses from answer key should be more optimum but requires
    #more computating power, as this is a theoretical project rather than an absolute, a less optimal path
    # is choosen.)
    guess = answers
    #intiating wordle game
    for word,score in wordle():
        #if game isn't completed
        if sum(score) != 10:
            print('calculating next best guess')
            rank,guess = next_best_guess(word, score,guess)
            #headers
            print(f"{'rank':<5} {'word':<10} {'E[Info]':>8}")
            for i, (word, info) in enumerate(list(rank.items())[0:10], start=1):
                #Top 10 guesses ranked
                print(f"#{i:<4} {word:<10} {info:>8.4f}")

if __name__ == '__main__':
    wordle_helper()



 