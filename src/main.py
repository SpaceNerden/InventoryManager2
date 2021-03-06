import database

while True:
    choice = input("New or Edit?: ")
    if choice.lower() == "new":
        iN = input("itemName: ")
        iB = input("itemBrand: ")
        iC = input("itemCode: ")
        iS = input("itemStock: ")
        iD = input("itemDate(D/M/Y): ")
        database.new_item(iN, iB, iC, iS, iD)
    elif choice.lower() == "edit":
        iCe = input("itemCode: ")
        iSe = input("itemNetStock: ")
        iDe = input("itemDate(D/M/Y): ")
        database.edit_item(iCe, iSe, iDe)
    elif choice.lower() == "setup":
        pass
