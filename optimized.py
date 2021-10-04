import csv
import datetime

# 0-1 Knapsack problem 
# https://simplecodehints.com/blog/knapsack-problem-dynamic-programming-algorithm/

def load_csv(file_path, max_invested=500):
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
            if float(action["price"]) > 0 and float(action["profit"]) > 0:
                action["price"] = int(float(action["price"])*100)
                action["gain"] = action["price"] * float(action["profit"])/100
                action["ror"] = action["gain"]/action["price"]
                data.append(action)
    return data

def make_profit_matrix(data, money_thresholds):
    min_price = money_thresholds[0]
    max_spent = money_thresholds[1]
    data.insert(0, {"name":"action_0", "price":0, "gain":0})
    profit_matrix = []

    for action_index in range(len(data)):
        profit_matrix.append([0]*int(max_spent+1))
        # if data_index%100 == 0:
        #       # To track huge datasets
        #     print(f"Matrix filed for action number {data_index}")
        for remaining_money in range(min_price-1,max_spent+1):
            price = data[action_index]["price"]
            # print(f"Comparing {remaining_money} and {price}")
            if remaining_money < price:
                # If we don't have no money, we can't buy
                profit_matrix[action_index][remaining_money] = profit_matrix[action_index-1][remaining_money]
                # print(profit_matrix[action_index-1][remaining_money])

                # if we can't buy this one, we won't be able to buy the following
                # so we can copy the whole remaining line
            else:
                # If we do have the money, we have a choice to make. What is more profitable between us buying and not buying this action ?  
                option_bought = profit_matrix[action_index-1][remaining_money-price] + data[action_index]["gain"]
                option_notbought = profit_matrix[action_index-1][remaining_money]
                profit_matrix[action_index][remaining_money] = max(option_bought, option_notbought)
        
        # print(f'Line {action_index} = {profit_matrix[action_index]}')

    return profit_matrix

# /**
# * Returns the indices of the items of the optimal knapsack.
# * i: We can include items 1 through i in the knapsack
# * j: maximum weight of the knapsack
# */
def recursive_knap(profit_matrix, data, action_index, remaining_money, list_of_bought_actions = []):
    """Browse profit matrix from maximum gain to first action and/or 0 remaining money."""
    # print(profit_matrix[action_index][remaining_money])
    # print(f"Checking {action_index},{remaining_money} (having already bought {list_of_bought_actions})")

    if action_index == 0:
        return list_of_bought_actions
    
    if action_index not in list_of_bought_actions:
        # print(profit_matrix[action_index][remaining_money])
        if profit_matrix[action_index][remaining_money] > profit_matrix[action_index-1][remaining_money]:
            price = data[action_index]['price']
            list_of_bought_actions.append(action_index)
            return recursive_knap(profit_matrix, data, action_index-1, remaining_money-price, list_of_bought_actions)
        else:
            # not bought
            return recursive_knap(profit_matrix, data, action_index-1, remaining_money, list_of_bought_actions)

def print_results(data, actions_list, sep="\t"):
    """Show results Sienna's style"""
    optimized_achats = actions_list
    total_cost = 0
    optimized_profit = 0
    print("Bought:")
    for action_index in optimized_achats:
        action = data[action_index]
        price_in_eur = action["price"]/100
        gain = action["gain"]/100
        ror = action["ror"]
        print(f"{action['name']}{sep}{price_in_eur}{sep}{action['profit']}{sep}{gain}{sep}{ror}")
        total_cost += price_in_eur
        optimized_profit += gain

    print(
        f"\nTotal cost: {round(total_cost,2)}\n",
        f"Profit: {round(optimized_profit,2)}")

def main():
    MAX_SPENT = 50000 # in cents

    fake_data = [
    {"name":"action1", "price":3, "profit": 0.1, "gain": 2},
    {"name":"action2", "price":5, "profit": 0.1, "gain": 5},
    {"name":"action3", "price":8, "profit": 0.1, "gain": 33},
    {"name":"action4", "price":2, "profit": 0.1, "gain": 27},
    {"name":"action4", "price":1, "profit": 0.1, "gain": 1},
    ]

    # data = fake_data
    file_path = "./test_datasets/test_dataset.csv"
    # file_path = "./test_datasets/dataset1_Python+P7.csv"
    data = load_csv(file_path, MAX_SPENT)
    data = [action for action in data if action["price"] > 0 and action["price"] <= MAX_SPENT]
    if data != []:
        start = datetime.datetime.now()
        min_price = min(data, key= lambda x:x["price"])["price"]

        # data = data[:10]
        # [print(action) for action in data]


        data = sorted(data, key= lambda x:x["ror"], reverse=True)
        # [print(action) for action in data[:10]]
        # money_post_greed = MAX_SPENT - greedily_bought["price"]

        # Generate the matrix M(0...n, 0...W)
        profit_matrix = make_profit_matrix(data, [min_price, MAX_SPENT])
        print(f"{datetime.datetime.now() - start}")
        # [print(line_num, profit_matrix[line_num]) for line_num in range(len(profit_matrix))]

        # From maximum gain, recursively browse the matrix towards 0,0
        results = recursive_knap(profit_matrix, data, len(data)-1, MAX_SPENT)
        print(f"{datetime.datetime.now() - start}")
        print_results(data, results)        
    else:
        print(f"Input is empty.")

if __name__ == '__main__':
    main()