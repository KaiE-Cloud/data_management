import pandas as pd
import math
from pathlib import Path
import sys
import numpy as np

import mysql.connector




def convert_to_null(data):
    converted_to_null = [None if isinstance(x, float) and math.isnan(x) else x for x in data]
    #converted_to_null = [
    #    "NULL" if (x is None or (isinstance(x, float) and math.isnan(x))) else x
    #    for x in data
    #]
    return converted_to_null




def to_int_or_nan(value):
    if value is None:
        return np.nan  # preserve as NaN
    try:
        # Normalize decimal comma ? dot
        normalized = value.replace(',', '.')
        # Convert to float (handles scientific notation)
        fval = float(normalized)
        # Convert to int
        return int(fval)
    except (ValueError, AttributeError):
        return np.nan




## iterate and list folder
def list_folder():
    directory = Path("C:\\Users\\Student\\Documents\\GFN\\LF-PV-2A Prüfungsvorbereitung FIAE - Teil 2 - schriftliche Prüfungen (Prüfungsbereich 2, 3 und 4) 31.03.2025-05.05.2025\\data_management\\off-export_erd\\")
    pulls = []
    for csv_file in directory.iterdir():
        if csv_file.is_file() and csv_file.suffix.lower() == '.csv':
            pulls.append(csv_file.name)
    ## check for data
    if pulls == []:
        print("Keine Datens?tze vorhanden")
        print("\n\n\n\n")
        sys.exit()
    return pulls




## read csv
def read_csv(file_name):
    filename = "C:\\Users\\Student\\Documents\\GFN\\LF-PV-2A Prüfungsvorbereitung FIAE - Teil 2 - schriftliche Prüfungen (Prüfungsbereich 2, 3 und 4) 31.03.2025-05.05.2025\\data_management\\off-export_erd\\" + file_name
    df = pd.read_csv(
        filename,
        encoding="latin1",         # safer encoding
        sep=None,                  # let pandas sniff the delimiter
        engine="python",           # python engine handles irregular CSVs better
        on_bad_lines="skip"        # skip malformed rows instead of failing
    )
    return df




pulls = list_folder()




for x in range(len(pulls)):

    df = read_csv(pulls[x])

    if 'stores' in df.columns:
        store_name = df['stores'].tolist()
        store_name = convert_to_null(store_name)
    if 'stores_tags' in df.columns:
        store_tag = df['stores_tags'].tolist()
        store_tag = convert_to_null(store_tag)




# Connect to database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="100%Safe",
    database="open_food_facts"
)

cursor = conn.cursor()

query = """
insert into store
(store_id, store_name, store_tag)
values
(%s, %s, %s)
"""

for x in range(0, len(store_name)):
    
    print('test ' + str(x))

    store_id = x+1

    if store_name[x] != None:
        store_name[x] = str(store_name[x])
    if store_tag[x] != None:
        store_tag[x] = str(store_tag[x])

    values = (
        store_id,
        store_name[x],
        store_tag[x]
    )

    cursor.execute(query, values)




conn.commit()

cursor.close()
conn.close()
