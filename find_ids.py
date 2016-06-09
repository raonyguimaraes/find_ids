from Bio import SeqIO

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-ids', '--ids', help='ids')
parser.add_argument('-i', '--input', help='fasta input')
parser.add_argument('-o', '--output', help='fasta output')
args = parser.parse_args()

id_list_file = open(args.ids)
input_fasta = open(args.input)
output_fasta = open(args.output, "w")

id_list = []
for id in id_list_file:
    id_list.append(id.strip())  

sequences = []
for record in SeqIO.parse(input_fasta, "fasta"):
    if record.id in id_list:
        sequences.append(record)
        # print(record.id, record.seq) 


SeqIO.write(sequences, output_fasta, "fasta")

output_fasta.close()
input_fasta.close()