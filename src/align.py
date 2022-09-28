"""A module for translating between alignments and edits sequences."""


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
