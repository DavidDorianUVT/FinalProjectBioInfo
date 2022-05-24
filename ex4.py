"""
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
"""
import math

filename="fastafile.txt"

entries={}

def gc_percent(dna):
    return round ((dna.count('C') + dna.count('G') ) *100/len(dna),7 )


with open(filename) as file:
    i=""
    for line in file:
        if line[-1]=="\n":
            line= line[:len(line)-1]

        if line[0]==">":
            i=line[1:]
            entries[i]=""
        else:
            entries[i]=entries[i]+line
print(entries)

results={n: gc_percent(entries[n]) for n in entries.keys()}

print(results)

largest=max(results,key=results.get)

corrected_value=abs(  results[largest] - 0.001)

print(largest,"\n",corrected_value)