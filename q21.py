gene_code={'A':"Adenine", 'C':"Cytosine", 'G':"Guanine ", 'T':"Thymine"}
reverse_gene_code = {gene_code[k]:k for k in gene_code.keys()}
print('Opp dictionary:', reverse_gene_code)
code = input('Enter gene code of your choice: ').upper()

def gene_decoder(genes : str) -> None:
    if any(char not in 'ACGT' for char in genes):
        print('Enter valid gene code: ')
        exit(0)
    else:
        print('Chemical names of given code sequence: ')
        for item in genes:
            print(gene_code[item])

gene_decoder(code)