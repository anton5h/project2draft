#from bio.seq import Seq, MutableSeq
from pandas import DataFrame, read_csv



def enumerate_codons(bases):
	"""Return a list of possible codons given a list of bases
	
	bases -- a list of possible bases as strings e.g. ['A','C','T','G']
	"""
	bases = [b.upper() for b in bases]
	codons = [a+b+c for a in bases for b in bases for c in bases]
	return codons

def translater(seq,codon_table):						 #translation of sequences to amino acids 
    seq = seq.lower().replace('\n', '').replace(' ', '')
    peptide = ''
    ###         genetic code = {


      #  "UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
      #  "UCU":"S", "UCC":"s", "UCA":"S", "UCG":"S",
      #  "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
      #  "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
      #  "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
      #  "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
      #  "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
      #  "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
      #  "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
      #  "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
      #  "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
      #  "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
      #  "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
      #  "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
      #  "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
      #  "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}
		
		
    for i in xrange(0, len(seq), 3):
        codon = seq[i: i+3]
        amino_acid = codon_table.get(codon, '*')
        if amino_acid != '*':
            peptide += amino_acid
        else:
            break
                
    return peptide
	

#def FASTA(filename): ###Fasta file reader
#	pass
	
bases = ['t', 'c', 'a', 'g']
codons = enumerate_codons(bases)	
amino_acids = 'CCCCCCCAAAAAAA**CC*WWWWWWGGGGGGCCCCCCCCCAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))
print(codon_table)

