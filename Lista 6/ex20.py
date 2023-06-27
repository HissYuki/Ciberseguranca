vet = [64,65,12,13,14,15,21,33,34,35,36,37,100,91,9,93,94]
seq = [vet[0]]
max_seq = seq

for i in range(1, len(vet)):
    if seq[len(seq)-1] + 1 == vet[i]:
        seq.append(vet[i])
    else:
        seq = [vet[i]]
    if len(seq) > len(max_seq):
        max_seq = seq

print(max_seq)