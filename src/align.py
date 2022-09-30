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
    seq1=[]
    seq2=[]
    s1=0
    s2=0
    for i in edits:
        if i == "M":
            seq1.append(x[s1])
            seq2.append(y[s2])
            s1+=1
            s2+=1
        elif i == "D":
            seq1.append(x[s1])
            seq2.append("-")
            s1+=1
        elif i == "I":
            seq1.append("-")
            seq2.append(y[s2])
            s2+=1

    seq1="".join(seq1)
    seq2="".join(seq2)


    return (seq1, seq2)
    


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
    ed=[]
    for i in range(len(x)):
        if x[i]!="-" and y[i]!="-":
            ed.append("M")
        elif x[i]=="-":
            ed.append("I")
        elif y[i]=="-":
            ed.append("D")
    
    ed="".join(ed)

    return ed
