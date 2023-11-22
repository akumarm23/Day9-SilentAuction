# Silent Auction Version 1

# Import the logo from a separate file
from logo import logo

# Print the logo at the beginning
print(logo)

# Import the os module for clearing the terminal screen
import os

# Function to determine the highest bidder and bid amount
def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bidding_amount = bidding_record[bidder]
        if bidding_amount > highest_bid:
            highest_bid = bidding_amount
            winner = bidder  # Update the winner only if a higher bid is found
    print(f"Winner is {winner}\nBid amount is ${highest_bid}\n")

# Initialize an empty dictionary to store bids
bids = {}

# Flag to indicate if the bidding is finished
bidding_finished = False

# Continue bidding until the user decides to stop
while not bidding_finished:
    # Get bidder's name and bid amount
    name = input("What is your Name? : ")
    price = int(input("What is your Bid? : $ "))
    
    # Store the bid in the dictionary
    bids[name] = price
    
    # Check if there are more bidders
    should_continue = input("Any other Bidders? Type 'yes' or 'no': ").lower()
    
    if should_continue == 'no':
        bidding_finished = True
        # Call the function to determine the highest bidder and bid amount
        highest_bidder(bids)
    elif should_continue == 'yes':
        # Clear the terminal screen for the next bidder
        os.system('cls' if os.name == 'nt' else 'clear')

# END OF CODE v0.1
