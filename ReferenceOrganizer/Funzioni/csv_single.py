"""
La funzione Csv Single permette di recuperare una sola anagrafica con il corrispettivo colore ed importarla nel file Extract.csv
Questa funzione va utilizzata per avere un maggior controllo su ogni export
"""
from ReferenceOrganizer.Tools.misc import root_directory,output_folder
import csv
import os
import glob

ListCsv = glob.glob(os.path.join(root_directory, "*.csv"))

def csv_single():
    frist_step_extract()


def frist_step_extract():
    sys_modello_find = input("Inserisci la referenza da cercare: ")
    sys_color_find = input("Inserisci la variante colore da cercare: ")
    for file_csv_singolo in ListCsv:
        second_step_compile(file_csv_singolo,sys_modello_find,sys_color_find)


def second_step_compile(csv_file,sys_modello_find,sys_color_find):
    open_file = open(os.path.join(csv_file))
    open_file = csv.reader(open_file, delimiter=""",""")

    for index,extract in enumerate(open_file): #extract è una lista di stringhe
            if index == 0:
                continue
            else:
                additional_attribute = extract[21].split(",") # 21 è l'indice dell'attributo addizionale
                sys_modello = additional_attribute[4:5] #sys_modello 
                sys_color = additional_attribute[1:2] #variante colore

                sys_modello = sys_modello[0].split("=")[1]
                sys_color = sys_color[0].split("=")[1]
                if sys_modello_find == sys_modello and sys_color_find == sys_color:
                    third_step_export(extract)

def third_step_export(row):
    with open(output_folder, mode="a") as OutputFile:
        writer = csv.writer(OutputFile)
        writer.writerow(row)
    return print("Riga compilata con successo")


if __name__ == "__main__":
    csv_single()



