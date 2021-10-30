# blindAuction.py
#
# Python Bootcamp Day 9 - Blind Auction
# Usage:
#      Create a blind auction program
#
# Marceia Egler October 1, 2021

#Create a blind auction program which takes an
#infinite amount of bidders and returns the
#highest bidder when completed

from replit import clear
from art import logo

print(logo)


auction = {}
are_bids = True

def highest_bid(bidders: dict):
  high_bid = 0

  #remember this will iterate through keys, not values  
  for bidder in bidders:
    if high_bid < bidders[bidder]:
      high_bid = bidders[bidder]
      winner = bidder
  print(f'The winner is {winner} with a bid of ${high_bid}.')


while are_bids:   
  user = input("What is your name?\n")
  bid = int(input("What is your bid in whole dollars?\n$"))

  #Add input to dictionary. No need to make a list
  auction[user] = bid
  more_bids = input("Are there any other bidders? Y/N\n").lower()
  clear()

  if more_bids == "n":
    highest_bid(auction)      
    are_bids = False