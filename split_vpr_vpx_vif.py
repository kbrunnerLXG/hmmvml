from Bio import SeqIO

vpr = []
vpx = []


for record in SeqIO.parse("unreviewed/protein-matching-IPR000012.fasta", "fasta"):
    if "Vpr"  in str(record.description):
        vpr.append(record)
    elif "Vpx" in str(record.description):
        vpx.append(record)



with open('vpr.fasta', 'w') as f:
    SeqIO.write(vpr, f, 'fasta')
with open('vpx.fasta', 'w') as f:
    SeqIO.write(vpx, f, 'fasta')



