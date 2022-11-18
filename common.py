#!/usr/bin/python3

from statistics import stdev

import sys

CT_ALPHABET_SIZE = 83
CT_ALPHABET = bytes(range(CT_ALPHABET_SIZE))

READABLE_OFFSET = 32

def data_to_info(data, prefix=""):
    if prefix != "":
        prefix = prefix + "_"
    data = sorted(data)
    result = {
        prefix+"mean": sum(data) / len(data),
        prefix+"median": data[len(data) // 2],
        prefix+"minimum": min(data),
        prefix+"maximum": max(data),
        prefix+"stdev": stdev(data),
    }
    return result

def print_cipher_stack(cipher_stack):
    for cipher, params in cipher_stack:
        print(cipher.__name__ + ":")
        print("\t", params)

def get_stdin_texts():
    pts = sys.stdin.buffer.read().splitlines()
    if "--normalize-input" in sys.argv:
        return normalize_pts(pts)
    else:
        return [bytes([y - READABLE_OFFSET for y in x]) for x in pts]

def print_cts(cts):
    for ct in cts:
        print(bytes([l + READABLE_OFFSET for l in ct]).decode())

def get_alphabet(pts):
    return bytes(set(b"".join(pts)))

def normalize_pt(pt, alphabet):
    return bytes([alphabet.index(l) for l in pt])

def normalize_pts(pts):
    alphabet = get_alphabet(pts)
    return [normalize_pt(pt, alphabet) for pt in pts]

def get_isomorphs(ct, max_size):
    isomorphs = set()
    for i, l in enumerate(ct):
        offset = ct.find(l, i + 1, i + max_size + 1)
        while offset != -1:
            isomorphs.add((i, offset - i - 1))
            offset = ct.find(l, offset + 1, i + max_size + 1)
    return isomorphs

def autokeyer(pts, autokeyer_alphabet_fn, iv):
    autokey_alphabets = {}
    for l in CT_ALPHABET:
        autokey_alphabets[l] = autokeyer_alphabet_fn(l)
    cts = []
    for pt in pts:
        ct = []
        for i, l in enumerate(pt):
            ct.append(autokey_alphabets[iv if i == 0 else ct[-1]][l])
        cts.append(bytes(ct))
    return cts

def poly_substitute(pts, ct_alphabet_fn):
    max_len = max([len(pt) for pt in pts])
    ct_alphabets = [ct_alphabet_fn(i) for i in range(max_len)]
    results = []
    for pt in pts:
        results.append(bytes([ct_alphabets[i][l] for i, l in enumerate(pt)]))
    return results

def substitute(pts, ct_alphabet):
    results = []
    for pt in pts:
        results.append(bytes([ct_alphabet[l] for l in pt]))
    return results

# takes a ciphertext
# returns a dictionnary, key is letter, value is count
def get_letters_count(ct):
    counts = dict.fromkeys(range(CT_ALPHABET_SIZE), 0)
    for l in ct:
        counts[l] += 1
    return counts
