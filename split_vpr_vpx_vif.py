from Bio import SeqIO

vpr = []
vpx = []
vif = []

for record in SeqIO.parse("vpR_vpx/protein-matching-IPR000012.fasta", "fasta"):
    if (str(record.description).split(" ")[1][:3]) == 'Vpr':
        vpr.append(record)

    elif (str(record.description).split(" ")[1][:3]) == 'Vpx':
        vpx.append(record)


with open('vpr.fasta', 'w') as f:
    SeqIO.write(vpr, f, 'fasta')
with open('vpx.fasta', 'w') as f:
    SeqIO.write(vpx, f, 'fasta')



