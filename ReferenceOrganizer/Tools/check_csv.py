'''
Questa funzione permette di esaminare il file Extract.csv e verificare se sono state esportate tutte le anagrafiche presenti nel file Anagrafiche.csv
in modo da avere un controllo sulla presenza di anagrafiche mancanti e gestione di errori

La funzione crea un file Root/Output/Check.csv che contiene i prodotti che sono prensenti nel file Anagrafiche.csv ma non nel file Extract.csv
'''
import os
import pandas
import json

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
        self.models = {}
        self.extract_file_row = self.output_reference_finder()


    def input_reference_finder(self) -> str:
        print("Interagisco con il file Anagrafiche.csv")
        with open(self.input_reference, mode="r") as file:
            self.reference_input_line = file.readlines()   
        # self.reference_input_line.append(reference_input_line)

    def output_reference_finder(self) -> str:
        print("Interagisco con il file Extract.csv")
        with open(self.extract_folder, mode="r") as file: 
            extract_file_rows= file.readlines() 
        self.reference_output_line=extract_file_rows
    
    def writer_csv(self):
        print("Inizio scrittura file Check.csv")
        for _,reference_input in enumerate(self.reference_input_line):
            reference = reference_input.replace("\n","").split(",")
            if reference not in self.reference_output_line:
                # with open("Root/Output/Check.csv", mode="w") as file:  
                #     print("Scrittura file in corso")
                #     file.write(reference_input)
                self.error_list.append(reference_input)
                    # print("Scrittura file c   ompletata ;)")
            else:
                print("Tutte le anagrafiche sono presenti nel file Extract.csv :)")
        # return self.error_list

    def normalize_models(self):
        with open(self.extract_folder, mode="r") as file:
            df = pandas.read_csv(file)

        for _, row in df.iterrows():
            attr = '{"'+row["additional_attributes"]+'"}'
            attr = attr.replace("=", '":"').replace(",", '","')
            # Qui ho fatto una cosa molto poco ortodossa, ma funziona
            # Esempio di attr
            # '{"sys_category":"118","sys_color":"C1675","sys_color_description":"BORDEAUX","sys_color_hex":"752534","sys_modello":"IR 12030SI 321","sys_size":"PZ","composizione":"100% POLIESTERE","gruppo_articoli":"AC-ACCESSORI","variante":"SI","campagna_acquisti":"AI21","cod":"IR 12030SI 321-C1675","sys_barcode":"2100037465013"}'
            attr = json.loads(attr)
            modello = attr.get("sys_modello")
            is_present = self.models.get(modello)
            if not is_present:
                self.models.update(
                    {
                        modello:[attr.get("sys_color")]
                    }
                )
            else:
                self.models.get(modello).append(attr.get("sys_color"))



        for modello, lista_colori in self.models.items():
            self.models.update({modello:list(set(lista_colori))})


    def check_color(self):
        self.normalize_models()
        to_dump = {"modelli":[],"colori":[]}
        for model, attr in self.models.items():
            to_dump.get("modelli").append(model)
            to_dump.get("colori").append(attr)

        new_df = pandas.DataFrame.from_dict(to_dump)
        new_df.to_csv("Root/Output/Check.csv")

    def check_not_in_extract(self):
        self.writer_csv()
        
        with open("Root/Output/Error.csv", mode="w") as errfile:
            for modello in self.error_list:
                errfile.write(f"{modello}")

                
        


    
if __name__ == "__main__":
    CheckCsv = CheckCsv()
    CheckCsv.input_reference_finder()
    CheckCsv.output_reference_finder()
    CheckCsv.writer_csv()

