"""
Questa funzione permette di generare un file csv con tutte le anagrafiche presenti nei file in Root/AnagDirectory.
E' una funzione che viene utilizzata in automatico in main.py per generare il file csv

"""
from ReferenceOrganizer.Tools.misc import root_directory,output_folder,input_reference
import csv
import os
import glob


ListCsv = glob.glob(os.path.join(root_directory, "*.csv"))
ref_locate = []


def frist_extract():
    with open(input_reference, mode="r", encoding='utf-8', errors='ignore') as reference_list:
        reference = reference_list.readlines()
    reference = [Referenza.replace("\n", "") for Referenza in reference]
    reference = set(reference)
    for file_csv_singolo in ListCsv:
        for Referenza in reference:
            check_extract(file_csv_singolo, Referenza)


# Funzione che permette di trovare solo re referenze ricercate
def check_extract(file_csv, referenza):
    file_open = open(os.path.join(file_csv))
    file_open = csv.reader(file_open, delimiter=""",""")

    for extract in file_open:
        additional_attribute = extract[21].split(",")
        sys_modello = additional_attribute[4:5]
        if len(sys_modello) > 0:
            if referenza in sys_modello[0]:
                ref_locate.append(extract)
                csv_builder(ref_locate)
                ref_locate.pop()
    

# Funzione  usata in main.py per generare il file csv
def csv_builder(row):
    with open(output_folder, mode="a") as OutputFile:
        output_write = csv.writer(OutputFile)
        output_write.writerows(row)


