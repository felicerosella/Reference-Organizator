from ReferenceOrganizer.Funzioni.csv_massive import frist_extract
from ReferenceOrganizer.Funzioni.csv_single import csv_single
from ReferenceOrganizer.Tools.misc import sceltamsg
from ReferenceOrganizer.Tools.check_csv import CheckCsv
from ReferenceOrganizer.Tools.clear_csv import output_csv_clear

def main():
    while True:
        scelta_execute = input(sceltamsg)

        if scelta_execute == "1":
            print("Inizializzata funzione Genera CSV massivo\n\n")
            frist_extract()
        elif scelta_execute == "2":
            print("Inizializzata funzione Genera CSV Singolo \n\n")
            csv_single()
            
        elif scelta_execute == "3": 
            print("Inizializzata funzione Check CSV \n\n")
            Checker = CheckCsv()
            Checker.input_reference_finder()
            Checker.output_reference_finder()
            Checker.writer_csv()

        elif scelta_execute == "4":
            print("Inizializzata funzione Pulizia CSV \n\n ")
            output_csv_clear()  
        else:
            break # Exit

if __name__ == "__main__":
    main() # Run main function