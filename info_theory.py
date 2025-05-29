import numpy as np
import itertools
from collections import OrderedDict
import time
from answer_key import guesses, answers

#Calculates entropy for a given word at a certain score
def entropy(x: str, score: tuple, answer_list: list):
    correct = []
    in_ans = []
    not_in_ans = set()
    ind_check = []
    #baskets to help in filtering
    for i in range(0,5):
        let = x[i]
        if score[i] == 2:
            correct.append((let,i))
            ind_check.append(i)
        if score[i] == 1:
            in_ans.append((let,i))
        else:
            not_in_ans.add(let)

    temp1 = []
    #Filters for possible matches
    for i in answer_list:
        #1st pass for green letter
        if all(i[pos] == ch for ch,pos in correct):
            #replacing green letters to avoid double counting
            masked_i = ''.join('_' if idx in [pos for _, pos in correct] else ch for idx, ch in enumerate(i))
            #2nd pass for yellow letter
            if all((ch in masked_i and masked_i[pos] != ch) for ch,pos in in_ans):
                # replacing yellow letters to avoid double counting
                filtered_i = ''.join(c for idx, c in enumerate(i) if idx not in ind_check)
                #3rd pass for grey letters
                if any(j in filtered_i for j in not_in_ans):
                    pass
                else:
                    temp1.append(i)

    #Calculation of entropy
    #P(x)
    p = len(temp1)/len(answer_list)
    #log(1/P(x))
    h = -np.log2(p) if p != 0 else 0
    return p*h, temp1

# Calculates Expected Information Gain for a word over all possible scores
def guess_score(guess: str,nCr : list, guess_left:list):
    H_x = 0
    for i in nCr:
        temp, temp1 = entropy(guess,i,guess_left)
        H_x += temp
    return H_x

#Ranks all possible guesses against themselves based on E[Information Gain].
def ranking(guess_left:list):
    #time taken for function
    start = time.time()
    all_combos = list(itertools.product([0, 1, 2], repeat=5))
    #Dictionary to record all guesses with their corresponding E[info Gain].
    d = {}
    for i in guess_left:
        d.update({i : round(float(guess_score(i, all_combos, guess_left)), 4)})
    #Ordered Dictionary to get a sorted dictionary.
    d = OrderedDict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    end = time.time()
    print(len(guess_left),'guesses left and processed','\t',f'took {end - start:.4f} secs.')
    return d

#Calculates next best guess, given a word, score and the remaining guesses left.
def next_best_guess(x: str, score: tuple, names: list):
    h_x, temp1 = entropy(x, score, names)
    return ranking(temp1),temp1
