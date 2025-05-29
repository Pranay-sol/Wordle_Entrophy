import random
from answer_key import answers,guesses


#Generates random answer
def answer_gen():
    random.seed()
    ans = answers[random.randrange(0, len(answers))]
    return ans

#Validates if guess word fits.
def guess_word(x : str = None):
    if x is None:
        x = input().strip().lower()
    if len(x) != 5 or x not in guesses:
        print("insert Valid 5-letter Word:")
        return guess_word()
    return x

#Scores the word in accordance to answer word
def scoring(word: str, answer:str):
    score = [0,0,0,0,0]
    word = list(word.lower())
    ans = list(answer)
    for i in range(0, 5):
        if word[i] == ans[i]:
            score[i] = 2
            ans[i] = '_'
            word[i] = "@"
    for i in range(0, 5):
        if word[i] in ans:
            score[i] = 1
            ans[ans.index(word[i])] = '_'
    return score

#Replication of Game
def wordle():
    answer = answer_gen()

    solved = False
    print('Insert Word')
    #6 Attempts as per the actual game
    for i in range(0,6):
        x = guess_word()
        cur_score = scoring(x, answer)
        #Checks if word is correct
        if cur_score == [2,2,2,2,2]:
            print('Solved!')
            solved = True
            #Yield to not break loop
            yield x,tuple(cur_score)
            break
        else:
            print("Current Score:", cur_score, '\n', i+1, "th attempt,", 5 - i,"attempts remaining:")
            yield x, tuple(cur_score)
    if not solved:
        print('\n','answer is',answer)
    return

if __name__ == '__main__':
    #Usage of function (makes future procedures simplier)
    for a,b in wordle():
        print(a,b)