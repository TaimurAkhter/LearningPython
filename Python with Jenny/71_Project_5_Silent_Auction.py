# Date: 5th January 2024 Friday
# Time: 12 : 23 AM
# Start Time: 02 : 40 PM 
# End Time: 03 : 16 PM 
import os

# def find_winner(bidder_details):
#     winner_bid = 0
#     winner_name = ''
#     for bidder in bidder_details:
#         bidding_price = bidder_details[bidder]
#         if bidding_price > winner_bid:
#             winner_bid = bidding_price
#             winner_name = bidder
#     print(f"Here is the list of all the bidders:\n{bidder_details}")
#     print(f"The winner is {winner_name} with a bid of {winner_bid}.")

print("Welcome to The Silent Auction Program")
# 'Awais':102000,'Taimur':100000, 'Mamoon':101000
bidders_Info = {}
winner_bid = 0
winner_name = ''

repeat = True
while repeat:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: "))
    bidders_Info[name] = price

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no' : ").lower()
    if more_bidders == 'yes':
        repeat = True
        os.system('cls')
    else:
        for name,bid in bidders_Info.items():
            if bid > winner_bid:
                winner_bid = bid
                winner_name = name
        print(f"The winner is {winner_name} with a bid of {winner_bid}.")
        # find_winner(bidders_Info)
        repeat = False
