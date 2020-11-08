import tkinter as tk
from tkinter import scrolledtext, INSERT
import fastophy_GUI

def main():
    master_window = tk.Tk()
    master_window.geometry("800x400")
    master_window.title("FastoPhy")

    # Parent widget for the buttons
    buttons_frame = tk.Frame(master_window)
    buttons_frame.grid(row=0, column=0, sticky = tk.W + tk.E) # creating a grid (West, East)

    # Buttons in parent widget
    btn_fasta = tk.Button(buttons_frame, text="FASTA file to Phyllip file", command = fastophy_GUI.initializing)
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

if __name__ == '__main__':
    main()