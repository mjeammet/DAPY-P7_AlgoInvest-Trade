import csv
import math

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
                action["gain"] = (price * float(action["profit"]))
                action["profitability"] = float(action["profit"])/price # ? 
                data.append(action)
                # use tuple (name, gain) ?
    return data

def maximize_profit(data, max_spent):
    # crazy_table = [[0]*len(data)]*len(data) # nested lists so not working, OMG 

    profit_matrix = []
    for data_index in range(len(data)):
        profit_matrix.append([])
        # if data_index%100 == 0:
        #       # To track huge datasets
        #     print(f"Matrix filed for action number {data_index}")
        for remaining_money in range(max_spent+1):
            profit_matrix[data_index].append(0)
            price = data[data_index]["price"]
            gain = float(data[data_index]["profit"])
            # print(f"Comparing {price} and {remaining_money*100}")
            if price > remaining_money:
                # If we don't have no money, we can't buy so remaining_money remains the same as for previous action
                profit_matrix[data_index][remaining_money] = profit_matrix[data_index-1][remaining_money]
            else:
                # If we do have the money, we also have a choice to make. What is more profitable between us buying and not buying this action ? 
                option_bought = profit_matrix[data_index-1][remaining_money-price]+gain
                option_notbought = profit_matrix[data_index-1][remaining_money]
                profit_matrix[data_index][remaining_money] = max(option_bought, option_notbought)

    return profit_matrix

# /**
# * Returns the indices of the items of the optimal knapsack.
# * i: We can include items 1 through i in the knapsack
# * j: maximum weight of the knapsack
# */
def recursive_knap(action_index, remaining_money, list_of_bought_actions):

    if action_index == 0:
        return list_of_bought_actions
    
    # print(profit_matrix[action_index][remaining_money])
    if profit_matrix[action_index][remaining_money] > profit_matrix[action_index-1][remaining_money]:
        price = data[action_index]['price']
        # print(action_index)
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
        optimized_profit += float(action["profit"])

    print(
        f"\nTotal cost: {total_cost}\n",
        f"Profit: {optimized_profit}")

if __name__ == '__main__':
    file_path = "./test_datasets/test_dataset.csv.txt"
    data = load_csv(file_path)
    # data = data[:101]
    MAX_SPENT = 50000 # in cents
    sorted_data = sorted(data,key= lambda x:x["gain"], reverse=True)
    profit_matrix = maximize_profit(sorted_data, MAX_SPENT)
    results = recursive_knap(len(data)-1, MAX_SPENT, [])
    print(results)
    print_results(results)
    