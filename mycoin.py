# -*- coding: utf-8 -*-
"""


@author: dogus
"""

import coin
def main():
    
    coin1 = coin.Coin()
    coin2 = coin.Coin()
    coin3 = coin.Coin()
    
    print("I have 3 coins with these side up:  ")
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    print()
    
    #Toss the coin
    coin1.toss()
    coin2.toss()
    coin3.toss()
    
    print("Now here are the sideup that are up: ")
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    print()
    
main()

import deneme


