# -*- coding: utf-8 -*-
"""


@author: dogus
"""

import random

class Coin:
    
    #__init__ metodu ile bozuk paranın ilk hali heads olarak başlatılır
    
    def __init__(self):
        self.sideup = 'Heads'
        
    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'
            
    def get_sideup(self):
        return self.sideup