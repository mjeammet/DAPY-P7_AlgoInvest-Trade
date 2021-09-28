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
results = []

def to_buy_or_not_to_buy(index_of_action, list_of_bought_actions, money_spent, total_gain, max_profit = 0):
    # reached last action
    if index_of_action == len(data):
        return total_gain, list_of_bought_actions
    else:
        action = data[index_of_action]
        # print(f"Questioning whether to buy {action}")
        # say i don't buy
        gain1 = to_buy_or_not_to_buy(index_of_action+1, list_of_bought_actions, money_spent, total_gain)

        # say i buy this action
        if money_spent+float(action["price"]) < MAX_SPENT:
            new_list = list_of_bought_actions + [action]
            gain2 = to_buy_or_not_to_buy(index_of_action+1, new_list, money_spent+float(action["price"]), total_gain+float(action["gain"]))
        else:
            gain2 = 0.0, []

        return max(gain1, gain2)
    
def print_results(result):
    optimized_achats = result[1]
    optimized_profit = result[0]
    total_cost = 0
    print("Bought:")
    for action in optimized_achats:
        price = float(action["price"])
        print(f"{action['name']} ({price}€)")
        total_cost += price

    print(
        f"\nTotal cost: {total_cost}\n",
        f"Profit: {optimized_profit}")

    # print(f"Best course of actions (lol) is {} with {max_profit} pesos.")

data = data[:19]
start = datetime.datetime.now()
optimized_achats = to_buy_or_not_to_buy(0, [], 0, 0)
end = datetime.datetime.now()

print(f"{end - start} seconds elapsed.") # ~ 800 000 combinaisons per second
print_results(optimized_achats)

