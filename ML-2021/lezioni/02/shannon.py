import collections
import math
 
 
def estimate_shannon_entropy(sequence):
    m = len(sequence)
    bases = collections.Counter([tmp_base for tmp_base in sequence])
 
    shannon_entropy_value = 0
    for base in bases:
        # number of residues
        n_i = bases[base]
        # n_i (# residues type i) / M (# residues in column)
        p_i = n_i / float(m)
        entropy_i = p_i * (math.log(p_i, 2))
        shannon_entropy_value += entropy_i
 
    return shannon_entropy_value * -1

string = input("Enter the string to compute Shannon entropy: ")
print(estimate_shannon_entropy(string))