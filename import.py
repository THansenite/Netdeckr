import csv

exImport = open("Data/Inventory/InventoryImportTest.csv")
exReader = csv.reader(exImport)
for row in exReader:
    print(str(row))
