import csv
import datetime

file_path = "./test_datasets/test_dataset.csv"

def load_file(path):
    data = []

    ### READING CSV FILE
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
                # print(action)
                next
            else:
                action["gain"] = (price * float(action["profit"])/100)
                action["price"] = float(action['price'])
                data.append(action)
                # use tuple (name, gain) ? 
    return data

### BRUTEFORCING MY WAY OUT OF THIS
# 2 ** n AKA the worst thing ever

def maximize_profit(index_of_action, remaining_money, total_gain):
    """Maximize profit recursively"""
    if index_of_action == len(data):
        # reached last action
        return total_gain, []
    else:
        action = data[index_of_action]
        # print(f"Questioning whether to buy {action}")
        # say i don't buy
        notbought_profit, notbought_list = maximize_profit(index_of_action+1, remaining_money, total_gain)

        # say i buy this action
        if remaining_money > action["price"]:
            bought_profit, bought_list = maximize_profit(index_of_action+1, remaining_money-action["price"], total_gain+float(action["gain"]))
        else:
            # allowed by the fact actions are sorted by price
            # if THIS action is too pricey, the following won't be cheaper and we'll reach end of line without buying anything
            # print("Cut short")
            return total_gain, []

        if bought_profit > notbought_profit:
            bought_list.append(index_of_action)
            return bought_profit, bought_list
        else:
            return notbought_profit, notbought_list

def print_results(result):
    optimized_achats = result[1]
    optimized_profit = result[0]
    total_cost = 0
    print("Bought:")
    for action_num in optimized_achats:
        action = data[action_num]
        price_in_eur = float(action["price"])
        print(f"{action['name']} ({price_in_eur}€)")
        total_cost += price_in_eur

    print(
        f"\nTotal cost: {total_cost}\n",
        f"Profit: {optimized_profit}")
def maximize_profit_timed(max_spent, rep = 1):
    total_elapsed = datetime.timedelta(0)
    for i in range(rep):
        start = datetime.datetime.now()
        optimized_achats = maximize_profit(0, max_spent, 0)
        end = datetime.datetime.now()
        elapsed = end - start
        total_elapsed += elapsed
        # print(f"{elapsed} seconds elapsed.") # ~ 800 000 combinaisons per second
    
    print(f"Number of runs : {rep}\tAverage of {total_elapsed / rep} seconds per run.")
    print_results(optimized_achats)

data = load_file(file_path)
data = data[:19]
# print(len(data))
# 19|500 ~ 0.67s avec la liste descendante et remontante (20a )
# 19|500 ~ 0.59s avec la liste remontante seulement (20|500 = 1.19 s, 100|50 = 0.71s)
# 19|500 ~ 0.54s avec la liste triée et le return des gens sans le sou (20|500 = 1.12s, 21|500 = 1.94s, ~3.7.10^274 années)
# 19|500 ~ 0.41s si on fait money restante - price (au lieu de money depensée + price < 500) et convertir les prix en float direct
data = sorted(data,key= lambda x:x["price"])
maximize_profit_timed(500)