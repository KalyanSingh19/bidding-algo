bidding = True
details = {}
highest_val = 0
winner = ""

def record (ledger):
    global highest_val,winner
    for val in ledger:
        bid_amt = ledger[val]
        if bid_amt > highest_val:
            highest_val = bid_amt
            winner = val

while bidding:
    name = input("Enter your name: \n")
    bidding_value = int(input("Enter the value: \n"))
    
    details[name] = bidding_value 
    bid = input("Do you want to continue bidding? (Yes or No): ").lower()
    values = details.values()
    if bid == "no":
        record(details)
        bidding = False

print(f"The winner is {winner} with bid value of ${highest_val}")




    



