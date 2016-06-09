from Bio import SeqIO

id_list_file = open('no_uniq_hits_S288c_no_mito_x_probiotics')
input_fasta = open('orf_trans_all_R64-1-1_20110203.fasta')
output_fasta = open("output.fasta", "w")

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