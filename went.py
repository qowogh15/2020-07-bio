from bio import seqIO

record = seqIO.read("059.fasta","fasta")

A = record.seq.count("A")
C = record.seq.count("C")
G = record.seq.count("G")
T = record.seq.count("T")

print(f"A:{A}")
print(f"C:{C}")
print(f"G:{G}")
print(f"T:{T}")

