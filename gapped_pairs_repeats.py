#!/usr/bin/python3

from common import *
from statistics import stdev

MAX_SIZE = 15

def measure(cts):
    results = []
    for ct in cts:
        # [left_index, right_index, gap_size]
        ct_len = len(ct)
        gapped_pairs = set()
        for i, l in enumerate(ct):
            offset = ct.find(l, i + 1)
            while offset != -1:
                for j in range(1, MAX_SIZE):
                    if offset + j >= ct_len:
                        break
                    if ct[i + j] == ct[offset + j]:
                        gapped_pairs.add((i, offset, j))
                offset = ct.find(l, offset + 1)
        results.append(gapped_pairs)

    gap_amounts_per_ct = []
    gap_amounts = [0]*(MAX_SIZE - 1)
    distances = []
    for ct in results:
        gap_amounts_per_ct.append(len(ct))
        for left, right, size in ct:
            gap_amounts[size - 1] += 1
            distances.append(right - left)
    #print(distances)
    #pprint(results)
    distances_info = [sum(distances) / len(distances), stdev(distances)]
    gap_amounts_per_ct_info = [sum(gap_amounts_per_ct) / len(gap_amounts_per_ct), stdev(gap_amounts_per_ct)]
    return gap_amounts + gap_amounts_per_ct_info + distances_info

if __name__ == "__main__":
    from pprint import pprint
    pprint(measure(get_stdin_texts()))
