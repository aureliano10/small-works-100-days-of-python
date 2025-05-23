from art import logo
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
print(logo)
dict_bids = {}
bid_boolean = False

def ganador(bidd_dict):
    winner = ""
    big_amount = 0
    for keys in bidd_dict:
        bidder = dict_bids[keys]
        if bidder > big_amount:
            big_amount = bidder
            winner = keys
    print(f"the winner is: {winner} with ${big_amount}")
while not bid_boolean:
    name = input("whats your name?\n")
    bid = int(input("what is your bid?\n$"))
    dict_bids[name] = bid
    more_people = input("are there more people?, type yes or no\n").lower()
    print("\n" * 40)
    if more_people == "no":
        ganador(dict_bids)
        bid_boolean = True




