"""
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.
An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."
Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
"""



dic = {"C": 0, "T": 0, "A": 0, "G": 0}

filename = "dataset_mine1.txt"

if __name__ == '__main__':
    with open(filename, "r") as file:
        seq = file.readline()

    for i in seq:
        dic[i]=dic[i]+1
    print(f"{dic['A']} {dic['C']} {dic['G']} {dic['T']}")
