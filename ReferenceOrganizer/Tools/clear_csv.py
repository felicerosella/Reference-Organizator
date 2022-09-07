'''
Questa funzione permette di eliminare i campi dal file Extract.csv
Applicare questa funzione solo se si vuole generare un nuovo file Extract.csv
In automatico importa anche la header
'''
from ReferenceOrganizer.Tools.misc import output_folder,header

def output_csv_clear():
    with open(output_folder, "w") as clear_file:
        clear_file.write(header)
    print("Pulizia file effettuata con successo")