"""A module for translating between alignments and edits sequences."""

import re

def cigar_to_edits(cigar: str) -> str:
    """Expand the compressed CIGAR encoding into the full list of edits.

    >>> cigar_to_edits("1M1D6M1I4M")
    'MDMMMMMMIMMMM'

    """
    edits = ''
    splitted = split_pairs(cigar)
    for tup in splitted:
        edits += tup[0]*tup[1]
    return edits

def split_pairs(cigar: str) -> list[tuple[int, str]]:
    """Split a CIGAR string into a list of integer-operation pairs.

    >>> split_pairs("1M1D6M1I4M")
    [(1, 'M'), (1, 'D'), (6, 'M'), (1, 'I'), (4, 'M')]

    """
    return [(int(i), op) for i, op in re.findall(r"(\d+)([^\d]+)", cigar)]

def align(x: str, y: str, edits: str) -> tuple[str, str]:
    """Align two sequences from a sequence of edits.

    Args:
        x (str): The first sequence to align.
        y (str): The second sequence to align
        edits (str): The list of edits to apply, given as a string

    Returns:
        tuple[str, str]: The two rows in the pairwise alignment

    >>> align("ACCACAGTCATA", "ACAGAGTACAAA", "MDMMMMMMIMMMM")
    ('ACCACAGT-CATA', 'A-CAGAGTACAAA')

    """
    edits =cigar_to_edits(edits)
    row1 = ''
    row2 = ''
    i,j = 0,0
    for idx in range(len(edits)):
        if edits[idx] == 'M':
            row1 += x[i]
            row2 += y[j]
            i += 1
            j += 1
        elif edits[idx] == 'D':
            row1 += x[i]
            row2 += '-'
            i += 1
        else: # edits[i] == 'I'
            row1 += '-'
            row2 += y[j]
            j += 1
    return (row1, row2)

def edits(x: str, y: str) -> str:
    """Extract the edit operations from a pairwise alignment.

    Args:
        x (str): The first row in the pairwise alignment.
        y (str): The second row in the pairwise alignment.

    Returns:
        str: The list of edit operations as a string.

    >>> edits('ACCACAGT-CATA', 'A-CAGAGTACAAA')
    'MDMMMMMMIMMMM'

    """
    edits = ''
    for idx in range(len(x)):
        if x[idx] == '-':
            edits += 'I'
        elif y[idx] == '-':
            edits += 'D'
        else:
            edits += 'M'
    return edits

# 
print(align('accaaagta', 'acaaatgtcca', '1M1D2M1I4M2I1M')) # string idx out of range. 
print(align('acgt', 'ac', '2M2D')) # string idx out of range.
print(align('a', '', '1D')) # string idx out of range.
print(align('acgttcga', 'aaaaa', '3M3D2M'))

#Desired results:
#acca-aagt--a
#a-caaatgtcca

#acgt
#ac--

#a
#-

#acgttcga
#aaa---aa
