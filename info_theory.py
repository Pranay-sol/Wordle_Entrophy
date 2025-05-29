import numpy as np
import itertools
from collections import OrderedDict
import time
from answer_key import guesses, answers
#from wordle_ig import wordle,scoring,guess_word,answer_gen

def entrophy(x: str, score: tuple, answer_list: list):
    correct = []
    in_ans = []
    not_in_ans = set()
    ind_check = []
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
    for i in answer_list:
        if all(i[pos] == ch for ch,pos in correct):
            masked_i = ''.join('_' if idx in [pos for _, pos in correct] else ch for idx, ch in enumerate(i))
            if all((ch in masked_i and masked_i[pos] != ch) for ch,pos in in_ans):
                filtered_i = ''.join(c for idx, c in enumerate(i) if idx not in ind_check)
                if any(j in filtered_i for j in not_in_ans):
                    pass
                else:
                    temp1.append(i)

    p = len(temp1)/len(answer_list)
    h = -np.log2(p) if p != 0 else 0
    return p*h, temp1

def guess_score(guess: str,nCr : list, guess_left:list):
    H_x = 0

    for i in nCr:
        temp, temp1 = entrophy(guess,i,guess_left)
        H_x += temp
    return H_x

def ranking(guess_left:list):
    start = time.time()
    all_combos = list(itertools.product([0, 1, 2], repeat=5))
    d = {}
    for i in guess_left:
        d.update({i : round(float(guess_score(i, all_combos, guess_left)), 4)})
    d = OrderedDict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    end = time.time()
    print(len(guess_left),'guesses left and processed','\t',f'took {end - start:.4f} secs.')
    return d

def next_best_guess(x: str, score: tuple, names: list):
    h_x, temp1 = entrophy(x, score, names)
    return ranking(temp1),temp1
