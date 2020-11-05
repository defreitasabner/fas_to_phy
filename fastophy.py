import re

# set-up
taxa = []
sequences = []

def initializing():
    fasta_file = input("Input the path to '.fasta' or '.fas' file as you which to convert to .phy: ")
    extracting_data_from_fasta_file(fasta_file)
    phy_file = input("Choose a name to '.phy' output file (without the extension .phy): ")
    phy_output_file_name = f'{phy_file}.phy'
    writing_data_from_fasta_to_phy_file(phy_output_file_name)


def extracting_data_from_fasta_file(fasta_file):
    with open(fasta_file, mode = 'r') as fasta_data:
        content = fasta_data.readlines()
        for item in content:
            if content.index(item) == 0 or content.index(item) % 2 == 0:
                item = cleaning_taxon_name_from_fasta_to_phy(item)
                taxa.append(item.strip())
            else:
                sequences.append(item.strip())
        testing_number_of_taxa_and_sequence()
    return print(f'{len(taxa)} taxa found, {len(sequences)} sequences found(number of sites: {len(sequences[0])})')

def cleaning_taxon_name_from_fasta_to_phy(taxon_name):
    pattern = ">"
    taxon_name = re.sub(pattern, '', taxon_name)
    return taxon_name

def testing_number_of_taxa_and_sequence():
    number_of_taxa = len(taxa)
    number_of_sequences = len(sequences)
    if (number_of_taxa == number_of_sequences):
        print('OK!')
    else:
        ValueError('Number of taxa and sequence do not match. Check the pattern of your .fasta or .fas file.')

# def extracting_input_file_name_to_output(input_file_name): # CORRIGIR
#     pattern = "([a-z]*)?(/)?([a-z]*)(.)([a-z]{2,4})"
#     search = re.search(pattern, input_file_name)
#     file_name = search.group(3)
#     output_file_name = f'{file_name}_converted.phy'
#     return output_file_name

def writing_data_from_fasta_to_phy_file(phy_output_file_name):
    with open(phy_output_file_name, mode = 'w') as output_file:
        output_file.write(f'{len(taxa)} {len(sequences[0])}\n')
        for taxon in taxa:
            output_file.write(f'{taxon} {sequences[taxa.index(taxon)]}\n')
    print('.fasta or .fas file converted sucessfully to .phy file!')

initializing()