def to_rna(dna_strand):
LOOKUP = str.maketrans("GCTA", "CGAU")
def to_rna(dna_strand):
    return dna_strand.translate(LOOKUP)
