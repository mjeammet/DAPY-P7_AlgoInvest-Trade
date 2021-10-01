import csv
import math

# 0-1 Knapsack problem 
# https://simplecodehints.com/blog/knapsack-problem-dynamic-programming-algorithm/

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
            if float(action["price"]) <= 0 or float(action["profit"]) < 0:
                next
            else:
                action["price"] = int(float(action["price"])*100)
                action["gain"] = float(action["price"] * float(action["profit"])/100)
                # action["profitability"] = float(action["profit"])/price # ? 
                data.append(action)
                # use tuple (name, gain) ?
    return data

def make_profit_matrix(data, max_spent):
    data.insert(0, {"name":"action_0", "price":0, "gain":0})
    profit_matrix = []

    for action_index in range(len(data)):
        profit_matrix.append([0]*int(max_spent+1))
        # if data_index%100 == 0:
        #       # To track huge datasets
        #     print(f"Matrix filed for action number {data_index}")
        for remaining_money in range(max_spent+1):
            price = data[action_index]["price"]
            # print(f"Comparing {remaining_money} and {price}")
            if remaining_money < price:
                # If we don't have no money, we can't buy
                profit_matrix[action_index][remaining_money] = profit_matrix[action_index-1][remaining_money]
                # print(profit_matrix[action_index-1][remaining_money])
            else:
                # If we do have the money, we have a choice to make. What is more profitable between us buying and not buying this action ?  
                gain = data[action_index]["gain"]
                option_bought = profit_matrix[action_index-1][remaining_money-price] + gain
                option_notbought = profit_matrix[action_index-1][remaining_money]
                profit_matrix[action_index][remaining_money] = max(option_bought, option_notbought)
        
        # print(f'Line {action_index} = {profit_matrix[action_index]}')

    return profit_matrix

# /**
# * Returns the indices of the items of the optimal knapsack.
# * i: We can include items 1 through i in the knapsack
# * j: maximum weight of the knapsack
# */
def recursive_knap(action_index, remaining_money, list_of_bought_actions):
    # print(profit_matrix[action_index][remaining_money])
    # print(f"Checking {action_index},{remaining_money} (having already bought {list_of_bought_actions})")

    if action_index == 0:
        return list_of_bought_actions
    
    if action_index not in list_of_bought_actions:
        # print(profit_matrix[action_index][remaining_money])
        if profit_matrix[action_index][remaining_money] > profit_matrix[action_index-1][remaining_money]:
            price = data[action_index]['price']
            list_of_bought_actions.append(action_index)
            return recursive_knap(action_index-1, remaining_money-price, list_of_bought_actions)
        else:
            # not bought
            return recursive_knap(action_index-1, remaining_money, list_of_bought_actions)

def print_results(actions_list):
    optimized_achats = actions_list
    total_cost = 0
    optimized_profit = 0
    print("Bought:")
    for action_index in optimized_achats:
        action = data[action_index]
        price_in_eur = action["price"]/100
        print(f"{action['name']} ({price_in_eur}€)")
        total_cost += price_in_eur
        optimized_profit += float(action["gain"])

    print(
        f"\nTotal cost: {total_cost}\n",
        f"Profit: {optimized_profit/100}")

if __name__ == '__main__':
    file_path = "./test_datasets/test_dataset.csv"
    # file_path = "./test_datasets/dataset1_Python+P7.csv"
    data = load_csv(file_path)
    # data = [
    #     {"name":"action1", "price":2, "gain": 2},
    #     {"name":"action2", "price":5, "gain": 5},
    #     {"name":"action3", "price":8, "gain": 33},
    #     {"name":"action4", "price":2, "gain": 27},
    # ]
    # data = data[:10]
    # [print(action) for action in data]
    MAX_SPENT = 50000 # in cents
    data = [action for action in data if action["price"] <= MAX_SPENT]
    # sorted_data = sorted(data,key= lambda x:x["gain"], reverse=True)
    profit_matrix = make_profit_matrix(data, MAX_SPENT)
    # [print(line_num, profit_matrix[line_num]) for line_num in range(len(profit_matrix))]
    results = recursive_knap(len(data)-1, MAX_SPENT, [])
    print_results(results)

    # Tester 15 - 2300 parce que ça avait l'air de bugger pour un index out of range ?