import csv
import pandas
import re
main_db = 'mainDatabase.csv'

col_names = ['itemName',
             'itemBrand',
             'itemCode',
             'itemStock']

def new_item(itemName, itemBrand, itemCode, itemStock, date):
    with open(main_db, mode='a') as item_stock:
        stock_writer = csv.writer(item_stock)
        stock_writer.writerow([itemName, itemBrand, itemCode, itemStock])
    with open(itemCode + ".csv", mode='w') as file:
        logger = csv.writer(file)
        logger.writerow(["Date", "Input/Output"])
        logger.writerow([date, itemStock])



def edit_item(itemCode, newNetStock, editDate):
    df = pandas.read_csv(main_db, names=col_names)
    result = df[df['itemCode']==itemCode]
    result2 = str(result['itemStock'].values)
    oldStock = int(result2.strip("[']"))
    newStock = oldStock + int(newNetStock)
    df.loc[df["itemCode"] == itemCode, "itemStock"] = newStock
    df.to_csv(main_db, index=False)
    with open(itemCode + ".csv", mode='a') as file:
        logger = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        logger.writerow([editDate, newNetStock])
