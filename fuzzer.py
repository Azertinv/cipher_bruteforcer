#!/usr/bin/python3

from common import *

from standard_deviations import get_means_and_stdevs, get_stdev_from_anchor
from random_cipher import *
from measure import measure
from messages import messages_bytes

import sys
import random

from pprint import pprint

(means, stdevs) = get_means_and_stdevs()

def get_goal_stdevs():
    return get_stdev_from_anchor(means, stdevs, measure(messages_bytes))

def get_plaintexts():
    with open("sample_plaintexts/best.txt", 'rb') as f:
        return normalize_pts(f.read().splitlines())

def get_score(goal, cts_measures):
    score = 0
    for m in goal:
        for k in goal[m]:
            score += (abs(goal[m][k] - cts_measures[m][k]))**2
    return score

CORPUS_THRESHOLD_SCORE = 200
CORPUS_DIR = "./corpus"

def main():
    def evaluate_cipher_stack(cipher_stack):
        cts = encrypt_with_cipher_stack(cipher_stack, pts)
        cts_measures = measure(cts)
        cts_stdevs = get_stdev_from_anchor(means, stdevs, cts_measures)
        return get_score(goal, cts_stdevs)
    goal = get_goal_stdevs()
    pts = get_plaintexts()
    queue = []
    random.seed(42)
    best_score = CORPUS_THRESHOLD_SCORE
    best_scorer = []
    best_cipher = None
    for i in range(10000):
        cipher_stack = random_cipher_stack(random.randint(1, 6))
        score = evaluate_cipher_stack(cipher_stack)
        if score < CORPUS_THRESHOLD_SCORE:
            if score < best_score:
                best_score = score
                best_cipher = cipher_stack
                queue.append(cipher_stack)
            print("iteration:", i)
            print("score:", score)
            print_cipher_stack(cipher_stack)
            print("-------------------------------")
            best_scorer.append(cipher_stack)

    while len(queue) > 0:
        cipher_stack = queue.pop(0)
        score = evaluate_cipher_stack(cipher_stack)
        for i in range(get_mutation_count(cipher_stack)):
            mutated_cipher_stack = mutate_cipher_stack(cipher_stack, i)
            mutated_score = evaluate_cipher_stack(mutated_cipher_stack)
            if mutated_score < score:
                if mutated_score < best_score:
                    best_score = mutated_score
                    best_cipher = cipher_stack
                    queue.insert(0, mutated_cipher_stack)
                    print("mutated_score:", mutated_score)
                    print_cipher_stack(mutated_cipher_stack)
                    print("-------------------------------")
                else:
                    queue.append(mutated_cipher_stack)

    print(best_score)
    print_cipher_stack(best_cipher)
    from IPython import embed
    embed()

if __name__ == "__main__":
    main()
