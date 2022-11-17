#!/usr/bin/python3

from common import *

import math
from measure import measure
from statistics import stdev
from random_ciphertext import generate_random_cts

import pickle
import os

CACHE_FILE = "measures.cache"

def get_means_and_stdevs(no_cache=False):
    if (not os.path.exists(CACHE_FILE)) or no_cache:
        means = []
        stdevs = []
        measures = []
        for i in range(10000):
            measures.append(measure(generate_random_cts(i)))
        for j in measures[0].keys():
            for k in measures[0][j].keys():
                data = [measures[i][j][k] for i in range(len(measures))]
                means.append(sum(data) / len(data))
                s = stdev(data)
                stdevs.append(s)
        with open(CACHE_FILE, 'wb') as f:
            pickle.dump((means, stdevs), f)
    else:
        with open(CACHE_FILE, 'rb') as f:
            (means, stdevs) = pickle.load(f)
    return (means, stdevs)

def get_stdev_from_anchor(stdevs, means, measures):
    i = 0
    results = {}
    for m in measures.keys():
        results[m] = {}
        for k, value in measures[m].items():
            # if the difference is too small to be measured, issue with floating points
            if math.isclose(measures[m][k], means[i]):
                results[m][k] = 0.0
            else:
                results[m][k] = (measures[m][k]/stdevs[i]) - (means[i]/stdevs[i])
            i += 1
    return results

def main():
    import sys

    (means, stdevs) = get_means_and_stdevs("--no-cache" in sys.argv)

    cts = get_stdin_texts()
    cts_measures = measure(cts)

    results = get_stdev_from_anchor(stdevs, means, cts_measures)

    for j in results.keys():
        print(j.__name__)
        for k, value in results[j].items():
            print(k+": ", end="")
            if abs(value) > 3.5:
                print("\x1b[0;37;41m", end="")
            print("{:.2f}\x1b[0;0m".format(value))
        print()

if __name__ == "__main__":
    main()
