import csv
import math
# from collections import OrderedDict
MAX_PER_ACTION = 500

file_path = "./test_datasets/dataset2_Python+P7.csv"
data = []
# opening the CSV file
with open(file_path, mode ='r') as file:
   
    # reading the CSV file
    csvFile = csv.DictReader(file)
    # simply csv.reader for a list of list
 
    # displaying the contents of the CSV file
    for line in csvFile:
        # print(line)
        action = dict(line)
        price = float(action["price"])
        gain = (price * float(action["profit"])/100)
        if price <= 0 or gain <1 : 
            next
        else:
            action["gain"] = gain
            action["profitability"] = float(action["profit"])/price
            data.append(action)
            # use tuple (name, gain) ? 

def print_results(optimized_achats):
    total_profit = 0
    total_cost = 0
    print("Bought:")
    for action in optimized_achats:
        # action = data[action_num]
        price = float(action["price"])
        print(f"{action['name']} ({price}€)")
        total_cost += price
        total_profit += float(action["gain"])

    print(
        f"\nTotal cost: {total_cost}\n",
        f"Profit: {total_profit}")

test = sorted(data,key= lambda x:x["profitability"], reverse=True)
# print(test)

money_spent = 0.0
actions_bought = []
for action in test:
    print(f"${action}")
    price = float(action["price"])
    if money_spent + price > MAX_PER_ACTION:
        # print(money_spent)
        next
    else: 
        money_spent += price
        actions_bought.append(action)
        # print(f"Buying ${action['name']} for ${price} (gain = ${action['gain']}) (total money spent: ${money_spent})")

print_results(actions_bought)
    