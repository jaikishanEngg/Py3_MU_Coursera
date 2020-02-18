# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:10:49 2020

@author: Jmore
"""
import random

VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Write the WOFPlayer class definition (part A) here
class WOFPlayer:
    def __init__(self,name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []
    
    def addMoney(self,amt):
        self.prizeMoney += amt
    
    def goBankrupt(self):
        self.prizeMoney = 0
    
    def addPrize(self, prize):
        self.prizes.append(prize)
    
    def __str__(self):
        return "{} (${})".format(self.name, self.prizeMoney)
        #Steve ($1800)

        
        
# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
    def getMove(self, category, obscuredPhrase, guessed):
        template = """{name} has ${prizeMoney}

Category: {category}
Phrase:  {obscured_phrase}
Guessed: {guessed}

Guess a letter, phrase, or type 'exit' or 'pass':
        """.format(name = self.name, prizeMoney = self.prizeMoney, category = category, obscured_phrase = obscuredPhrase, guessed = ", ".join(guessed))
        return input(template)
        
# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = "ZQXJKVBPYGFWMUCLDRHSNIOATE"
    
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self.prizeMoney = 0
        self.prizes = []
    
    def smartCoinFlip(self):
        return True if random.randint(1,10) > self.difficulty else False
    
    def getPossibleLetters(self, guessed):
        diff = list(set(LETTERS) - set(guessed))
        if(self.prizeMoney < VOWEL_COST):
            #He cannot guess the vowels 
            return list(set(diff) - set(VOWELS))
        else:
            return list(diff)
    
    def getMove(self, category, obscuredPhrase, guessed):
        possible_guess = self.getPossibleLetters(guessed)
        if len(possible_guess) == 0:
            return 'pass' 
        else:            
            if(self.smartCoinFlip()):
                for l in self.SORTED_FREQUENCIES:
                    if l in possible_guess:
                        return l
            else:
                return random.choice(possible_guess)
 