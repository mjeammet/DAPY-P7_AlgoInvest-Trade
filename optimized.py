import csv
import math
# from collections import OrderedDict
MAX_SPENT = 50000 # in cents

file_path = "./test_datasets/dataset1_Python+P7.csv"

def load_csv(file_path):
    """Opens a csv file"""
    data = []
    with open(file_path, mode ='r') as file:
    
        # reading the CSV file
        csvFile = csv.DictReader(file)
        # simply csv.reader for a list of list
    
        # displaying the contents of the CSV file
        for line in csvFile:
            # print(line)
            action = dict(line)
            price = float(action["price"])
            if price <= 0:
                next
            else:
                action["price"] = int(float(action["price"])*100)
                action["gain"] = (price * float(action["profit"])/100)
                action["profitability"] = float(action["profit"])/price # ? 
                data.append(action)
                # use tuple (name, gain) ?
    return data

def print_results(optimized_achats):
    total_profit = 0
    total_cost = 0
    print("Bought:")
    for action in optimized_achats:
        # action = data[action_num]
        price = action["price"]/100
        print(f"{action['name']} ({price}€)")
        total_cost += price
        total_profit += float(action["gain"])

    print(
        f"\nTotal cost: {total_cost}\n",
        f"Profit: {total_profit}")

def maximize_profit_hs(data):
    remaining_money = MAX_SPENT
    actions_bought = []
    for action in data:
        # print(f"${action}")
        price = float(action["price"])
        if remaining_money > price:
            remaining_money -= price
            actions_bought.append(action)
        else:
            # print(f"Buying ${action['name']} for ${price} (gain = ${action['gain']}) (total money spent: ${money_spent})")
            # print(money_spent)
            next
    return actions_bought

def maximize_profit(data):
    crazy_table = [[0]*len(data)]*len(data)
    crazy_table = []
    remaining_money = 20
    
    # for action_index in data:
        # crazy_table.append([1,0])
    return crazy_table

# def maximize_profit(data):
#     table_res = {}

#     while table_res[0] == None:
#         pass

#     for action_index in len(data):
#         if table_res[action_index] == None:

if __name__ == '__main__':
    data = load_csv(file_path)
    data = data[:3]
    sorted_data = sorted(data,key= lambda x:x["gain"], reverse=True)
    results = maximize_profit(sorted_data)
    print(results)
    # print_results(results)
    