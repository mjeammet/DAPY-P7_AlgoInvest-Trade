import csv
import math
# from collections import OrderedDict
MAX_PER_ACTION = 500

file_path = "./test_datasets/dataset1_Python+P7.csv"
data = []
# opening the CSV file
with open(file_path, mode ='r')as file:
   
    # reading the CSV file
    csvFile = csv.DictReader(file)
    # simply csv.reader for a list of list
 
    # displaying the contents of the CSV file
    for line in csvFile:
        action = dict(line)
        price = float(action["price"])
        gain = (price * float(action["profit"])/100) - price
        if price <= 0 or gain <1 : 
            next
        else:
            action["gain"] = gain
            data.append(action)
            # use tuple (name, gain) ? 

test = sorted(data,key= lambda x:x["gain"], reverse=True)
# print(test)

money_spent = 0.0
for action in test:
    print(f"${action}")
    price = float(action["price"])
    if money_spent + price > MAX_PER_ACTION:
        # print(money_spent)
        exit
    else: 
        money_spent += price
        print(f"Buying ${action['name']} for ${price} (gain = ${action['gain']}) (total money spent: ${money_spent})")