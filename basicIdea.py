import csv
import inventory

exImport = open("Data/Inventory/InventoryImportTest.csv")
exReader = csv.reader(exImport)
myInventory = []

# prints the header line of the file
header = exReader.__next__()

imCount = header.index('Count')
imName = header.index('Name')
imEdition = header.index('Edition')
imFoil = header.index('Foil')


def checkFoil(param):
    if param == "Yes":
        result = "Foil"
    else:
        result = "Normal"
    return result


# iterates through subsequent rows of data
for row in exReader:
    currentCard = inventory.Card(row[imCount], row[imName], row[imEdition], checkFoil(row[imFoil]))
    myInventory.append(currentCard)
    # print(currentCard.showInfo())

print(myInventory.showInfo())
