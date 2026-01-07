import numpy as np
from Bio import SeqIO
import pickle as pkl
import pandas as pd


kmer_length = 3
kmer_vocab = set()
no_of_proteins = 0
proteins = []
y=[]

for record in SeqIO.parse('/home/aditya/hmmvml/vpR_vpx/protein-matching-IPR000012.fasta', "fasta"):
    if "Vpr"  in str(record.description):
        y.append(0)
    elif "Vpx" in str(record.description):
        y.append(1)
    else:
        continue

    no_of_proteins += 1
    proteins.append(record.seq)
    seq = record.seq
    for i in range(len(seq) - kmer_length + 1):
        subseq = seq[i:i + kmer_length]
        if subseq not in kmer_vocab:
            kmer_vocab.add(subseq)


num_kmers = len(kmer_vocab)

kmer_index = {kmer: j for j, kmer in enumerate(kmer_vocab)}


table = [[0] * num_kmers for _ in range(no_of_proteins)]
for i, seq in enumerate(proteins):
    for pos in range(len(seq) - kmer_length + 1):
        kmer = seq[pos:pos + kmer_length]
        j = kmer_index[kmer]
        table[i][j] = 1

table = np.array(table)
print(len(proteins))
print(len(kmer_vocab))
print((table.shape))
print(pd.Series(y).value_counts())


with open('data.pkl', 'wb',) as f:
    pkl.dump(table,f)

with open('label.pkl', 'wb') as f:
    pkl.dump(y,f)

