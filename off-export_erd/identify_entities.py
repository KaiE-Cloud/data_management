import pandas
import math
import re
from pathlib import Path
import sys
import csv
from collections import defaultdict




## iterate and list folder
def list_folder():
    directory = Path("C:\\Users\\Student\\Documents\\GFN\\LF-PV-2A Prüfungsvorbereitung FIAE - Teil 2 - schriftliche Prüfungen (Prüfungsbereich 2, 3 und 4) 31.03.2025-05.05.2025\\SQL\\")    ####
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
    filename = "C:\\Users\\Student\\Documents\\GFN\\LF-PV-2A Prüfungsvorbereitung FIAE - Teil 2 - schriftliche Prüfungen (Prüfungsbereich 2, 3 und 4) 31.03.2025-05.05.2025\\SQL\\" + file_name    ####
    fields = []
    rows = []
    with open(filename, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
    head = ''.join(field for field in fields)
    shipmentLinesTotal = 0
    for row in rows[:100]:
        shipmentLinesTotal=shipmentLinesTotal+1
    w, h = 1, shipmentLinesTotal
    orderPosition = [[0 for shipmentLinesTotal in range(w)] for y in range(h)]
    y=0
    for row in rows[:100]:
        for col in row:
            orderPosition[y][0] = ("%10s" % col)
        y=y+1
    return head, shipmentLinesTotal, orderPosition


pulls = list_folder()


for x in range(len(pulls)):
    head, shipmentLinesTotal, orderPosition = read_csv(pulls[x])
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
