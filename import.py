import csv

exImport = open("Data/Inventory/InventoryImportTest.csv")
exReader = csv.reader(exImport)

# prints the header line of the file
header = exReader.__next__()

imCount = header.index('Count')
imName = header.index('Name')
imEdition = header.index('Edition')
imFoil = header.index('Foil')


# iterates through subsequent rows of data
def checkfoil(param):
    if param == "Yes":
        result = "Foil"
    else:
        result = "Normal"
    return result


class Card:
    def __init__(self, count, name, edition, foil):
        self.count = count
        self.name = name
        self.edition = edition
        self.foil = foil


for row in exReader:
    # print(", ".join([row[imCount], row[imName], row[imEdition], checkfoil(row[imFoil])]))
    inventory = Card(row[imCount], row[imName], row[imEdition], checkfoil(row[imFoil]))
    print(", ".join([inventory.count, inventory.name, inventory.edition, inventory.foil]))




