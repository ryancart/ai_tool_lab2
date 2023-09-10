def menu():
    print("Please select an option: \n: ",
          "1) Optimize a gene \n",
          "2) De-optimize a gene \n",
          "3) Exit the program \n",
          "Enter the integer for your choice: ")

    choice = int(input('Enter your choice: '))

    if choice == 1:
        True
        #recombobulate(True)
    elif choice == 2:
        False
        #recombobulate(False)
    elif choice == 3:
        exit()
    else:
        print("Please enter a number between 1 and 3.")
""" A main menu """


def load_fasta_file():
    fasta_data = list(open('project_data\Scer-1.fasta'))
    fasta_data_dictionary = dict()
    gene_counter = 0

    for a in range(0, len(fasta_data), 2):
        fasta_data_dictionary[fasta_data[a].lstrip('>').rstrip('\n')] = fasta_data[a + 1].rstrip("\n")
        gene_counter += 1

    print("The total number of sequences imported was ", gene_counter)

    return fasta_data_dictionary


def load_csv_file():
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
            acid_max_frequency_dictionary[acid] = freq
        elif freq < acid_max_frequency_dictionary[acid]:
            acid_max_frequency_dictionary[acid] = freq

        if acid not in acid_min_frequency_dictionary:
            acid_min_frequency_dictionary[acid] = freq
        elif freq > acid_min_frequency_dictionary[acid]:
            acid_min_frequency_dictionary[acid] = freq

    return codon_acid_dictionary, acid_max_frequency_dictionary, acid_min_frequency_dictionary


fasta_data_file = load_fasta_file()

codon_acid_data, acid_max_frequency_data, acid_min_frequency_data = load_csv_file()


print(codon_acid_data)
print(acid_max_frequency_data)
print(acid_min_frequency_data)

# print(csv_data)

