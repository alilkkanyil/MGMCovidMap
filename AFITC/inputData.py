# inputData.py
# Last modified: 08/23/2020
# By Ali Yildirim
# Data to create/update input json file for database
# Work in progress.
# No dependencies other than json for this file.
import json

market = {}
newMarkets = {}
preLoaded = False
startKey = 1

try:
    f = open("./StoreMap/data/outfile.json")
    loadedFile = json.load(f)
    market.update(loadedFile)
    for key in market.keys():
        startKey = int(key) + 1

except:
    print("No pre-existing data found")

menuChoice = 0

while(menuChoice != 4):
    print("Options")
    print("1) Add new market")
    print("2) Print current market list")
    print("3) Edit existing market")
    print("4) Exit")
    menuChoice = int(input("Enter input: "))

    if(menuChoice == 1):
        storeName = input("Enter the store name: ")
        storeAddress = input("Enter the store address: ")
        storeLat = input("Enter store lat.: ")
        storeLong = input("Enter store long. : ")
        sanitizerAvailable = input("Is sanitizer available? (Available/Unavailable): ")
        tpAvailable = input("Is toilet paper available? (Available/Unavailable): ")   
        ptAvailable = input("Is paper towels available? (Available/Unavailable): ")
        foodAvailable = input("Is food available? (Available/Unavailable): ")
        market[startKey] = {
            "brand": storeName,
            "Address": storeAddress,
            "lat": storeLat,
            "lng": storeLong,
            "cannedFood": foodAvailable,
            "toiletPaper": tpAvailable,
            "paperTowels": ptAvailable,
            "sanitizer": sanitizerAvailable
        }
    
    elif (menuChoice == 2):
        for store in market:
            print(market[store])
    
    elif (menuChoice == 3):
        print("Select store ID to be edited:")
        for store in market:
            print(str(store) + ")")
            print(market[store])
            print("\n")
        choice = input()
        if(choice < startKey):
            storeName = input("Enter the store name: ")
            storeAddress = input("Enter the store address: ")
            storeLat = input("Enter store lat.: ")
            storeLong = input("Enter store long. : ")
            sanitizerAvailable = input("Is sanitizer available? (Available/Unavailable): ")
            tpAvailable = input("Is toilet paper available? (Available/Unavailable): ")   
            ptAvailable = input("Is paper towels available? (Available/Unavailable): ")
            foodAvailable = input("Is food available? (Available/Unavailable): ")
            market[choice] = {
                "brand": storeName,
                "Address": storeAddress,
                "lat": storeLat,
                "lng": storeLong,
                "cannedFood": foodAvailable,
                "toiletPaper": tpAvailable,
                "paperTowels": ptAvailable,
                "sanitizer": sanitizerAvailable
            }

output = json.dumps(market)
with open("./Map/src/data/outfile.json","w+") as outfile:
    outfile.write(output)
    outfile.close()