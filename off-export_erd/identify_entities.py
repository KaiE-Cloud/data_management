import pandas as pd
import math
import re
from pathlib import Path
import sys
import csv
from collections import defaultdict
from decimal import Decimal
import numpy as np




## iterate and list folder
def list_folder():
    directory = Path("C:\\Users\\Student\\Documents\\GFN\\LF-PV-2A Prüfungsvorbereitung FIAE - Teil 2 - schriftliche Prüfungen (Prüfungsbereich 2, 3 und 4) 31.03.2025-05.05.2025\\data_management\\off-export_erd\\")    ####
    pulls = []
    for csv_file in directory.iterdir():
        if csv_file.is_file() and csv_file.suffix.lower() == '.csv':
            pulls.append(csv_file.name)
    ## check for data
    if pulls == []:
        print("Keine Datensätze vorhanden")    ####
        print("\n\n\n\n")
        sys.exit()
    return pulls




## read csv
def read_csv(file_name):
    filename = "C:\\Users\\Student\\Documents\\GFN\\LF-PV-2A Prüfungsvorbereitung FIAE - Teil 2 - schriftliche Prüfungen (Prüfungsbereich 2, 3 und 4) 31.03.2025-05.05.2025\\data_management\\off-export_erd\\" + file_name    ####
    fields = []
    rows = []
    with open(filename, 'r', encoding='ISO-8859-1', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='\t')
        fields = next(csvreader)
        for row in csvreader:
            if any(field.strip() for field in row):
                rows.append(row)




    df = pd.read_csv(
        filename,
        encoding="latin1",         # safer encoding
        sep=None,                  # let pandas sniff the delimiter
        engine="python",           # python engine handles irregular CSVs better
        on_bad_lines="skip"        # skip malformed rows instead of failing
    )
    #print("Total rows (excluding header):", len(df))
    #print("Detected delimiter:", df.columns.name or "unknown")
    #input()
    # List all column names
    #print("Columns:", df.columns.tolist())
    # Preview the first 5 rows
    #print(df.head())
    #input()




    head = ''.join(field for field in fields)
    shipmentLinesTotal = 0
    for row in rows[:1000]:
        shipmentLinesTotal=shipmentLinesTotal+1
    w, h = 1, shipmentLinesTotal
    orderPosition = [[0 for shipmentLinesTotal in range(w)] for y in range(h)]
    y=0
    for row in rows[:1000]:
        for col in row:
            orderPosition[y][0] = ("%10s" % col)
        y=y+1
    return head, shipmentLinesTotal, orderPosition, df




def convert_to_int_keep_nan(value):
    """
    Convert scientific notation strings or integer strings to int.
    Keep nan values as float('nan').
    """
    # Handle NaN (either float nan or string 'nan')
    if value is None or (isinstance(value, float) and math.isnan(value)) or str(value).strip().lower() == 'nan':
        return np.nan
    try:
        # Convert to string and replace comma with dot
        value_str = str(value).strip().replace(',', '.')
        # Convert using Decimal for precision
        return int(Decimal(value_str))
    except Exception:
        # If conversion fails, return nan
        return np.nan




pulls = list_folder()




for x in range(len(pulls)):
    head, shipmentLinesTotal, orderPosition, df = read_csv(pulls[x])




    #code, lc, quantity, serving_size, obsolete, obsolete_since_date, link, off:nova_groups, off:nova_groups_tags
    if 'code' in df.columns:
        codes = df['code'].tolist()
        print(len(codes))
        print("codes:", codes[:1000])
    print()

    input()

    if 'lc' in df.columns:
        lcs = df['lc'].tolist()
        print(len(lcs))
        print("lcs:", lcs[:1000])
    print()
    if 'quantity' in df.columns:
        quantities = df['quantity'].tolist()
        print(len(quantities))
        print("quantities:", quantities[:1000])
    print()
    if 'serving_size' in df.columns:
        serving_sizes = df['serving_size'].tolist()
        print(len(serving_sizes))
        print("serving_sizes:", serving_sizes[:1000])
    print()
    if 'obsolete' in df.columns:
        obsolete = df['obsolete'].tolist()
        print(len(obsolete))
        print("obsolete:", obsolete[:1000])
    print()
    if 'obsolete_since_date' in df.columns:
        obsolete_since_dates = df['obsolete_since_date'].tolist()
        print(len(obsolete_since_dates))
        print("obsolete_since_dates:", obsolete_since_dates[:1000])
    print()
    if 'link' in df.columns:
        links = df['link'].tolist()
        print(len(links))
        print("links:", links[:1000])
    print()
    if 'off:nova_groups' in df.columns:
        off_nova_groups = df['off:nova_groups'].tolist()
        print(len(off_nova_groups))
        print("off_nova_groups:", off_nova_groups[:1000])
    print()
    if 'off:nova_groups_tags' in df.columns:
        off_nova_groups_tags = df['off:nova_groups_tags'].tolist()
        print(len(off_nova_groups_tags))
        print("off_nova_groups_tags:", off_nova_groups_tags[:1000])
    input()




    properties = head.split()

    # Group by the first tag
    groups = defaultdict(list)
    for item in properties:
        key = item.split('_')[0]  # first tag
        groups[key].append(item)

    # Convert defaultdict to regular dict
    groups = dict(groups)

    '''
    # Flatten the grouped items
    sorted_data = []
    for key in groups.keys():
        sorted_data.extend(groups[key])
    '''

    print("\n")
    print("File      – " + pulls[x])
    print("\n")
    for tag, items in groups.items():
        print(f"{tag}: {items}")
    print("\n")
    input()
    '''
    try:
        print("Kopf      – " + "MSN: " + head.split(';')[1] + "; MON: " + head.split(';')[2] + "; additionalProp3: " + head.split(';')[5] + "; TTN: " + head.split(';')[6] + "; Method: " + head.split(';')[9] + "; CountryCode: " + head.split(';')[10] + "; ShipmentDate: " + str(datetime.strptime(head.split(';')[11], '%Y-%m-%d').date()))
    except:
        print("Kopf      – " + "MSN: " + head.split(';')[1] + "; MON: " + head.split(';')[2] + "; additionalProp3: " + head.split(';')[5] + "; TTN: " + head.split(';')[6] + "; Method: " + head.split(';')[9] + "; CountryCode: " + head.split(';')[10] + "; ShipmentDate: " + str(datetime.strptime(head.split(';')[11], '%d.%m.%Y').date()))
    for y in range(shipmentLinesTotal):
        print("Position" + str(y+1) + " – MPN: " + orderPosition[y][0].split(';')[1] + "; Quantity: " + orderPosition[y][0].split(';')[2])
    print()
    '''
print("\n\n")
