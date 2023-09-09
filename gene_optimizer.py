def menu():
    print("Enter 1 to optimize a gene \n",
          "Enter 2 to de-optimize a gene \n",
          "Enter 3 to quit \n")

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
    for a in range(len(fasta_data)):
        fasta_data[a].lstrip('>')
        fasta_data[a].rstrip('\n')
        for b in range(b + 1, len(fasta_data)):
            fasta_data[b].rstrip("\n")
            fasta_data_dictionary[a] = b

    return fasta_data_dictionary

def load_csv_file():
    csv_data = list(open('project_data\Ecol_codon_freqs-1.csv'))
    #for line in csv_data:
        #csv_data = line.rstrip()

    return csv_data

fasta_data_file = load_fasta_file()
csv_data = load_csv_file()


print(fasta_data_file)

# print(csv_data)

