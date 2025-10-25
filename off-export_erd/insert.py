import pandas as pd
import math
from pathlib import Path
import sys
import numpy as np

import mysql.connector




def convert_to_null(data):
    converted_to_null = [None if isinstance(x, float) and math.isnan(x) else x for x in data]
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
    directory = Path("C:\\Users\\eton_\\OneDrive\\Dokumente\\GFN\\data_management\\off-export_erd\\")
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
    filename = "C:\\Users\\eton_\\OneDrive\\Dokumente\\GFN\\data_management\\off-export_erd\\" + file_name
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

    #code, lc, quantity, serving_size, obsolete, obsolete_since_date, link, off:nova_groups, off:nova_groups_tags

    print()
    if 'code' in df.columns:
        codes = df['code'].tolist()
        codes = [to_int_or_nan(v) for v in codes]
        codes = convert_to_null(codes)
        print(len(codes))
        print("codes:", codes[1:1000])
    print()
    if 'lc' in df.columns:
        lcs = df['lc'].tolist()
        lcs = convert_to_null(lcs)
        print(len(lcs))
        print("lcs:", lcs[1:1000])
    print()
    if 'quantity' in df.columns:
        quantities = df['quantity'].tolist()
        quantities = convert_to_null(quantities)
        print(len(quantities))
        print("quantities:", quantities[1:1000])
    print()
    if 'serving_size' in df.columns:
        serving_sizes = df['serving_size'].tolist()
        serving_sizes = convert_to_null(serving_sizes)
        print(len(serving_sizes))
        print("serving_sizes:", serving_sizes[1:1000])
    print()
    if 'obsolete' in df.columns:
        obsolete = df['obsolete'].tolist()
        obsolete = convert_to_null(obsolete)
        print(len(obsolete))
        print("obsolete:", obsolete[1:1000])
    print()
    if 'obsolete_since_date' in df.columns:
        obsolete_since_dates = df['obsolete_since_date'].tolist()
        obsolete_since_dates = convert_to_null(obsolete_since_dates)
        print(len(obsolete_since_dates))
        print("obsolete_since_dates:", obsolete_since_dates[1:1000])
    print()
    if 'link' in df.columns:
        links = df['link'].tolist()
        links = convert_to_null(links)
        print(len(links))
        print("links:", links[1:1000])
    print()
    if 'off:nova_groups' in df.columns:
        off_nova_groups = df['off:nova_groups'].tolist()
        off_nova_groups = convert_to_null(off_nova_groups)
        print(len(off_nova_groups))
        print("off_nova_groups:", off_nova_groups[1:1000])
    print()
    if 'off:nova_groups_tags' in df.columns:
        off_nova_groups_tags = df['off:nova_groups_tags'].tolist()
        off_nova_groups_tags = convert_to_null(off_nova_groups_tags)
        print(len(off_nova_groups_tags))
        print("off_nova_groups_tags:", off_nova_groups_tags[1:1000])
    input()



'''
# Connect to database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="100%Safe",
    database="open_food_facts"
)
'''
table_name = "Product"
attributes = "code, lc, quantity, serving_size, obsolete, obsolete_since_date, link, nova_group, nova_group_tag"

#cursor = conn.cursor()




for x in range(1, len(codes)):
    #values = ""

    #codes[x] + ", " + lcs[x] + ", " + quantities[x] + ", " + serving_sizes[x] + ", " + obsolete[x] + ", " + obsolete_since_dates[x] + ", " + links[x] + ", " + off_nova_groups[x] + ", " + off_nova_groups_tags[x]
    print()
    print("insert into " + table_name + "(" + attributes + ") values(" + str(codes[x]) + ", " + str(lcs[x]) + ", " + str(quantities[x]) + ", " + str(serving_sizes[x]) + ", " + str(obsolete[x]) + ", " + str(obsolete_since_dates[x]) + ", " + str(links[x]) + ", " + str(off_nova_groups[x]) + ", " + str(off_nova_groups_tags[x]) + ");")
    #cursor.execute("insert into " + table_name + "(" + attributes + ") values(" + values + ");")
input()



'''
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
'''