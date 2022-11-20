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

CORPUS_THRESHOLD_SCORE = 400

def main():
    random.seed(42)

    def evaluate_cipher_stack(cipher_stack):
        cts = encrypt_with_cipher_stack(cipher_stack, pts)
        cts_measures = measure(cts)
        cts_stdevs = get_stdev_from_anchor(means, stdevs, cts_measures)
        return get_score(goal, cts_stdevs)

    goal = get_goal_stdevs()
    pts = get_plaintexts()

    queue = []
    best_queue = []
    # anything in this queue already got sheduled mutations done
    backlog = []

    best_score = CORPUS_THRESHOLD_SCORE
    best_cipher = None

    print("Generating corpus ...")
    for i in range(10000):
        cipher_stack = random_cipher_stack(random.randint(1, 6))
        score = evaluate_cipher_stack(cipher_stack)
        if i % 1000 == 0:
            print("iteration:", i, "queue:", len(queue), "best_queue:", len(best_queue))
        if score < CORPUS_THRESHOLD_SCORE:
            if score < best_score:
                best_score = score
                best_cipher = cipher_stack
                best_queue.append(cipher_stack)
                print("-------------------------------")
                print("new best score:", score)
                print_cipher_stack(cipher_stack)
            else:
                queue.append(cipher_stack)

    print("Corpus generated, starting to fuzz")
    for i in range(10000):
        if len(best_queue) > 0:
            cipher_stack = best_queue.pop()
            scheduled_mutations = True
        elif len(queue) > 0:
            cipher_stack = queue.pop(0)
            scheduled_mutations = True
        else: # if all the queues are empty exit
            break
        if i % 100 == 0:
            print("iteration:", i, \
                    "queue:", len(queue), \
                    "best_queue:", len(best_queue), \
                    "backlog:", len(backlog))
        score = evaluate_cipher_stack(cipher_stack)
        iterations = get_mutation_count(cipher_stack) if scheduled_mutations else 10
        for i in range(iterations):
            if scheduled_mutations:
                mutated_cipher_stack = mutate_cipher_stack(cipher_stack, i)
            else:
                mutated_cipher_stack = mutate_cipher_stack(cipher_stack, -1)
            mutated_score = evaluate_cipher_stack(mutated_cipher_stack)
            if mutated_score < best_score:
                best_score = mutated_score
                best_cipher = cipher_stack
                best_queue.append(mutated_cipher_stack)
                print("-------------------------------")
                print("new best score:", mutated_score)
                print_cipher_stack(mutated_cipher_stack)
                print("-------------------------------")
            elif score - mutated_score > 20.0:
                queue.append(mutated_cipher_stack)

    print(best_score)
    print_cipher_stack(best_cipher)
    from IPython import embed
    embed()

if __name__ == "__main__":
    main()
