sequence=input("Give me mRNA sequence, thanks :) ").upper()
sequence_list=list(sequence)

def find_sequence():
    coding_region=[]
    start_code=False
    start_position=-1
    for i in range(0,len(sequence_list)-2):
        code=sequence[i:i+3]
        if code=="AUG":
            start_position=i
            start_code=True
            break
    if start_code:
        remaining_sequence=sequence[start_position:]
        j=0
        while j < len(remaining_sequence) - 2:
            if j + 3 > len(remaining_sequence):
                break
            end_code = remaining_sequence[j:j+3]
            if end_code in ["UAA", "UAG", "UGA"]:
                for v in remaining_sequence[:j]:
                    coding_region.append(v)
                break
            j += 3
    if len(remaining_sequence) - j == 1 or len(remaining_sequence) - j == 2:
        remaining_sequence = remaining_sequence[:j]
    for v in remaining_sequence:
        coding_region.append(v)
    return coding_region


codon_table = {
    'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu',
    'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
    'UAU': 'Tyr', 'UAC': 'Tyr', 'UAA': 'Stop', 'UAG': 'Stop',
    'UGU': 'Cys', 'UGC': 'Cys', 'UGA': 'Stop', 'UGG': 'Trp',
    'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
    'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
    'CAU': 'His', 'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln',
    'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
    'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile', 'AUG': 'Met',
    'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
    'AAU': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
    'AGU': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',
    'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
    'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
    'GAU': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu',
    'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly'
}
def counter(m):
        acid_dict={}
        for i in m:
            acid_dict[i]=acid_dict.get(i,0)+1
        return acid_dict

def max_amino_acid(coding_region):
    all_acids=[]
    if not coding_region:
        return ({},[])
    for i in range(0,len(coding_region)-2,3):
        mRNA1=coding_region[i:i+3]
        mRNA2="".join(mRNA1)
        acids=codon_table[mRNA2]
        all_acids.append(acids)
    acid=counter(all_acids)
    max_count=max(acid.values())
    max_acid=[acid_name for acid_name,count in acid.items() if count==max_count]
    return acid,max_acid

x=find_sequence()
y=max_amino_acid(x)
acid=y[0]
max=y[1]
result="".join(x)
print(f"The mRNA sequence is {result}")
print(f"Most frequency amino acid is {max}")


import matplotlib.pyplot as plt
x=list(acid.keys())
y=[int(value) for value in acid.values()]
plt.bar(x,y)
plt.xlabel("Amino acid name")
plt.ylabel("Times")
for i,value in enumerate(y):
    plt.text(i, value, f"{value}",ha="center", va="bottom")
plt.title("Amino acid frequencies")
plt.show()

"""
import matplotlib.pyplot as plt
u=list(acid.keys())
v=list(acid.values())
plt.pie(v,labels=u,autopct="%1.2f%%")
plt.title("Amino acid frequencies")
plt.show()
"""