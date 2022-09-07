'''
Questa funzione permette di esaminare il file Extract.csv e verificare se sono state esportate tutte le anagrafiche presenti nel file Anagrafiche.csv
in modo da avere un controllo sulla presenza di anagrafiche mancanti e gestione di errori

La funzione crea un file Root/Output/Check.csv che contiene i prodotti che sono prensenti nel file Anagrafiche.csv ma non nel file Extract.csv
'''
import os

class CheckCsv:


    def __init__(self):
        self.root_directory = "./Root/"
        self.output_folder = os.path.join(self.root_directory, "Output")
        self.extract_folder = os.path.join(self.output_folder, "Extract.csv")
        self.input_reference = os.path.join(self.root_directory, "Anagrafiche.csv")
        self.error_folder = os.path.join(self.output_folder, "Extract_error.csv")
        self.error_list = []
        self.reference_input_line = []
        self.reference_output_line = []
        self.extract_file_row = self.output_reference_finder()


    def input_reference_finder(self) -> str:
        print("Interagisco con il file Anagrafiche.csv")
        with open(self.input_reference, mode="r") as file:
            reference_input_line = file.readlines()   
        self.reference_input_line.append(reference_input_line)

    def output_reference_finder(self) -> str:
        print("Interagisco con il file Extract.csv")
        with open(self.extract_folder, mode="r") as file: 
            extract_file_row = file.read() 
            return self.reference_output_line.append(extract_file_row)
    
    def writer_csv(self):
        print("Inizio scrittura file Check.csv")
        for _,reference_input in enumerate(self.reference_input_line):
            reference = reference_input.replace("\n","").split(",")
            if reference not in self.reference_output_line:
                print(reference)
                with open("Root/Output/Check.csv", mode="w") as file:  
                    print("Scrittura file in corso")
                    file.write(reference_input)
                    self.error_list.append(reference_input)
                    print("Scrittura file completata ;)")
            else:
                print("Tutte le anagrafiche sono presenti nel file Extract.csv :)")
        return self.error_list

    
if __name__ == "__main__":
    CheckCsv = CheckCsv()
    CheckCsv.input_reference_finder()
    CheckCsv.output_reference_finder()
    CheckCsv.writer_csv()

