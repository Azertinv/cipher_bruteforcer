#!/usr/bin/python3

from common import *

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

    gap_count_per_ct = []
    gap_count = [0]*(MAX_SIZE - 1)
    distances = []
    for ct in results:
        gap_count_per_ct.append(len(ct))
        for left, right, size in ct:
            gap_count[size - 1] += 1
            distances.append(right - left)
    result = dict([(str(i)+"_gap_count", gap_count[i]) for i in range(MAX_SIZE-1)])
    result.update(data_to_info(gap_count, "gap_count"))
    result.update(data_to_info(gap_count_per_ct, "gap_count_per_ct"))
    result.update(data_to_info(distances, "distances"))
    return result

if __name__ == "__main__":
    from pprint import pprint
    pprint(measure(get_stdin_texts()))
