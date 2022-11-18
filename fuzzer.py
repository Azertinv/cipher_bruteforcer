#!/usr/bin/python3

from common import *

from standard_deviations import get_means_and_stdevs, get_stdev_from_anchor
from random_cipher import random_cipher_stack, mutate_cipher_stack, encrypt_with_cipher_stack
from measure import measure
from messages import messages_bytes

import sys
import random

from pprint import pprint

(means, stdevs) = get_means_and_stdevs()

def get_goal_stdevs():
    return get_stdev_from_anchor(means, stdevs, measure(messages_bytes))

def get_plaintexts():
    # lorem ipsum plaintext has almost same size as eye glyphs
    with open("sample_plaintexts/lorem_ipsum.txt", 'rb') as f:
        return normalize_pts(f.read().splitlines())

def get_score(goal, cts_measures):
    score = 0
    for m in goal:
        for k in goal[m]:
            score += (abs(goal[m][k] - cts_measures[m][k]) / 3)**2
    return score

def print_cipher_stack(cipher_stack):
    for cipher, params in cipher_stack:
        print(cipher.__name__ + ":")
        print("\t", params)

CORPUS_THRESHOLD_SCORE = 25.0
CORPUS_DIR = "./corpus"

def main():
    goal = get_goal_stdevs()
    pts = get_plaintexts()
    random.seed(1337)
    best_score = 1000
    best_scorer = []
    for i in range(100000):
        #if i > 10000 and i % 10 == 1:
        #    cipher_stack = mutate_cipher_stack(random.choice(best_scorer[-3:]))
        #else:
        cipher_stack = random_cipher_stack(random.randint(1, 5))
        cts = encrypt_with_cipher_stack(cipher_stack, pts)
        cts_measures = measure(cts)
        cts_stdevs = get_stdev_from_anchor(means, stdevs, cts_measures)
        score = get_score(goal, cts_stdevs)
        if score < CORPUS_THRESHOLD_SCORE:
            if score < best_score:
                best_score = score
                best_cipher = cipher_stack
            print("iteration:", i)
            print("score:", score)
            print_cipher_stack(cipher_stack)
            print("-------------------------------")
            best_scorer.append(cipher_stack)

    print(best_score)
    print_cipher_stack(best_cipher)
    from IPython import embed
    embed()

if __name__ == "__main__":
    main()
