import tkinter as tk
from tkinter import scrolledtext, INSERT
import re
from tkinter import filedialog, messagebox

taxa = []
sequences = []

def main():
    master_window = tk.Tk()
    master_window.geometry("800x400")
    master_window.title("FastoPhy")

    # Parent widget for the buttons
    buttons_frame = tk.Frame(master_window)
    buttons_frame.grid(row=0, column=0, sticky = tk.W + tk.E) # creating a grid (West, East)

    # Buttons in parent widget
    btn_fasta = tk.Button(buttons_frame, text="FASTA file to Phyllip file", command = initializing)
    btn_fasta.grid(row=0, column=0, padx=10, pady=10)

    # Parent widget for console log
    console_frame = tk.LabelFrame(master_window, text="Console log", padx =10, pady =10)
    console_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=tk.W + tk.E + tk.N + tk.S)

    master_window.columnconfigure(0, weight=1)
    master_window.rowconfigure(1, weight=1)

    console_frame.rowconfigure(0, weight=1)
    console_frame.columnconfigure(0, weight=1)

    # Console log without text
    console_log = scrolledtext.ScrolledText(console_frame, width=40, height=10)
    console_log.grid(row=0, column=0, sticky=tk.W + tk.E + tk.N + tk.S)
    console_log.tag_configure("centered", justify="left")
    console_log.insert(INSERT, "------------ FastoPhy v0.3.1, a software to convert FASTA file in Phyllip file ------------\n")
    console_log.insert(INSERT, "Please, click on top button to input FASTA file and iniate the conversion.\n")

    master_window.mainloop()

def ask_for_continue():
    check = messagebox.askyesno(title= 'Fas to Phy',
                                message= 'Do you want input another FASTA file to convert to Phyllip file?')
    return check

def choosing_fasta_file():
    local = filedialog.askopenfilename(title = "Choose a FASTA file ('.fas', '.fasta', '.fna', 'ffn', 'faa', '.frn')",
                                       filetypes = [('FASTA file', ('.fas', '.fasta', '.fna', 'ffn', 'faa', '.frn')),
                                                    ('all files', '.*')])
    return local

def initializing():
    check = True
    while check:
        fasta_file = choosing_fasta_file()
        extracting_data_from_fasta_file(fasta_file)
        phy_file = choosing_local_and_name_to_phy_file()
        writing_data_from_fasta_to_phy_file(phy_file)
        check = ask_for_continue()

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
    print(f'{len(taxa)} taxa found, {len(sequences)} sequences found(number of sites: {len(sequences[0])})')

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

def choosing_local_and_name_to_phy_file():
    local = filedialog.asksaveasfilename(title="Choose a local to save your converted Phyllip file ('.phy'):",
                                         filetypes=[('Phyllip file (.phy)', '.phy'), ('all files', '.*')],
                                         defaultextension='.phy',
                                         initialfile='converted')
    return local

def writing_data_from_fasta_to_phy_file(phy_file):
    with open(phy_file, mode = 'w') as output_file:
        output_file.write(f'{len(taxa)} {len(sequences[0])}\n')
        for taxon in taxa:
            output_file.write(f'{taxon} {sequences[taxa.index(taxon)]}\n')
    taxa.clear()
    sequences.clear()
    print('FASTA file converted sucessfully to Phyllip file!')

if __name__ == '__main__':
    main()