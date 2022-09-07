'''
File misc.py contiene frasi e processi secondari che non sono necessari per l'esecuzione del programma
per un ordine di lettura vengono definiti in questo file
'''

output_folder = "./Root/Output/Extract.csv"
input_reference = "./Root/Anagrafiche.csv"
root_directory = "./Root/Input/"

header = "status,visibility,sku,store_view_code,attribute_set_code,product_type,product_websites,url_key,name,description,short_description,product_online,price,special_price,special_price_from_date,special_price_to_date,qty,is_in_stock,tax_class_id,categories,configurable_variation_labels,additional_attributes,configurable_variations"

sceltamsg ="""

1 - Genera Csv Massivo
2 - Genera Csv Singolo
3 - Check Csv
4 - Pulizia Csv

Scelta>> """