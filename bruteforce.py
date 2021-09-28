import csv
import datetime
MAX_SPENT = 500

file_path = "./test_datasets/dataset1_Python+P7.csv"
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
        gain = (price * float(action["profit"])/100)
        if price <= 0: 
            # print(action)
            next
        else:
            action["gain"] = gain
            data.append(action)
            # use tuple (name, gain) ? 

### BRUTEFORCING MY WAY OUT OF THIS
# 2 ** n AKA the worst thing ever

def to_buy_or_not_to_buy(index_of_action, money_spent, total_gain):
    
    if index_of_action == len(data):
        # reached last action
        return total_gain, []
    else:
        action = data[index_of_action]
        # print(f"Questioning whether to buy {action}")
        # say i don't buy
        gain1, list1 = to_buy_or_not_to_buy(index_of_action+1, money_spent, total_gain)

        # say i buy this action
        if money_spent+float(action["price"]) < MAX_SPENT:
            gain2, list2 = to_buy_or_not_to_buy(index_of_action+1, money_spent+float(action["price"]), total_gain+float(action["gain"]))
        else:
            # allowed by the fact actions are sorted by price
            # if THIS action is too pricey, the following won't be cheaper and we'll reach end of line without buying anything
            # print("Cut short")
            return total_gain, []

        if gain2 > gain1:
            list2.append(index_of_action)
            return gain2, list2
        else:
            return gain1, list1
    
def print_results(result):
    optimized_achats = result[1]
    optimized_profit = result[0]
    total_cost = 0
    print("Bought:")
    for action_num in optimized_achats:
        action = data[action_num]
        price = float(action["price"])
        print(f"{action['name']} ({price}€)")
        total_cost += price

    print(
        f"\nTotal cost: {total_cost}\n",
        f"Profit: {optimized_profit}")

def optimize_choices(rep = 10):
    total_elapsed = datetime.timedelta(0)
    for i in range(rep):
        start = datetime.datetime.now()
        optimized_achats = to_buy_or_not_to_buy(0, 0, 0)
        end = datetime.datetime.now()
        elapsed = end - start
        total_elapsed += elapsed
        # print(f"{elapsed} seconds elapsed.") # ~ 800 000 combinaisons per second
    
    print(f"Number of runs : {rep}\tAverage of {total_elapsed / rep} seconds per run.")
    print_results(optimized_achats)

data = data[:21]
# 19 actions, max 500 ~ 0.67s avec la liste descendante et remontante (20a )
# 19 actions, max 500 ~ 0.59s avec la liste remontante seulement (20|500 = 1.19 s, 100|50 = 0.71s)
# 19 actions, max 500 ~ 0.54s avec la liste triée et le return des gens sans le sou (20|500 = 1.12s, 21|500 = 1.94s, ~3.7.10^274 années)
data = sorted(data,key= lambda x:x["price"])
optimize_choices(rep=1)

