import pandas as pd
import sys
sys.stdout.reconfigure(encoding='utf-8')

excel_file =  pd.read_excel('Artisan_france_page_jeune.xlsx')
json_data  = excel_file.to_json(orient='records') 
print(json_data)