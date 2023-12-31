def menu():
    """ A main menu. Its glory-full"""
    print("Please select an option: \n",
          "1) Optimize a gene \n",
          "2) De-optimize a gene \n",
          "3) Exit the program \n",
          "Enter the integer for your choice: ")

    nonsense = input('Enter your choice: ')
    if nonsense.isdigit():
        choice = int(nonsense)
    else:
        choice = 0

    if choice == 1:
        gene_id, new_sequence = recombobulate(True)
        print("The optimized gene sequence for ", gene_id, " is:", "\n", new_sequence)
        save_gene(gene_id, new_sequence, "optimized")
    elif choice == 2:
        gene_id, new_sequence = recombobulate(False)
        print("The de-optimized gene sequence for ", gene_id, " is:", "\n", new_sequence)
        save_gene(gene_id, new_sequence, "deoptimized")
    elif choice == 3:
        exit()
    else:
        print("Please follow directions and enter a number between 1 and 3.")

    
def save_gene(gene_id, new_sequence, change_type):
    """Function to create the file name and open a new file and write the data"""
    save_choice = input("Would you like to save Y/N: ").upper()
    if save_choice == "Y":
        filename = gene_id + "_" + change_type + ".fasta"
        file = open(filename, "w")
        line = [">" + gene_id + "\n", new_sequence + "\n"]
        file.writelines(line)
        file.close()
    else:
        menu()


def load_fasta_file():
    """Loads the fasta data"""
    fasta_data = list(open('project_data\Scer-1.fasta'))
    fasta_data_dictionary = dict()
    gene_counter = 0

    for a in range(0, len(fasta_data), 2):
        fasta_data_dictionary[fasta_data[a].lstrip('>').rstrip('\n')] = fasta_data[a + 1].rstrip("\n")
        gene_counter += 1

    print("The total number of sequences imported was ", gene_counter)

    return fasta_data_dictionary


def load_csv_file():
    """Loads the csv data into 3 dictionary"""
    csv_data = list(open('project_data\Ecol_codon_freqs-1.csv'))
    codon_acid_dictionary = dict()
    acid_max_frequency_dictionary = dict()
    acid_min_frequency_dictionary = dict()

    for b in range(1, len(csv_data), 1):
        chop_stringy = csv_data[b].split(',')
        code = chop_stringy[0]
        acid = chop_stringy[1]
        freq = float(chop_stringy[2].rstrip('\n'))

        codon_acid_dictionary[code] = acid

        if acid not in acid_max_frequency_dictionary:
            acid_max_frequency_dictionary[acid] = (freq, code)
        elif freq > acid_max_frequency_dictionary[acid][0]:
            acid_max_frequency_dictionary[acid] = (freq, code)

        if acid not in acid_min_frequency_dictionary:
            acid_min_frequency_dictionary[acid] = (freq, code)
        elif freq < acid_min_frequency_dictionary[acid][0]:
            acid_min_frequency_dictionary[acid] = (freq, code)

    return codon_acid_dictionary, acid_max_frequency_dictionary, acid_min_frequency_dictionary


def recombobulate(bool):
    """Does the reconfiguring of the gene sequence"""
    gene_id_input = input("Enter the gene to edit: ").upper()
    edited_gene = ""

    if gene_id_input not in fasta_data_file:
        print("gene ID not in database to edit")
        menu()

    if bool:
        data_base = acid_max_frequency_data
    else:
        data_base = acid_min_frequency_data

    gene_to_edit = fasta_data_file[gene_id_input]

    for c in range(0, len(gene_to_edit), 3):
        next_codon = gene_to_edit[c:c + 3]
        replacement = data_base[codon_acid_data[next_codon]][1]
        edited_gene += replacement

    return gene_id_input, edited_gene


fasta_data_file = load_fasta_file()
codon_acid_data, acid_max_frequency_data, acid_min_frequency_data = load_csv_file()
while(True):
    menu()



