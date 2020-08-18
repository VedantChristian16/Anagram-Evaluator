# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 22:36:00 2020

@author: 14chr
"""
from collections import Counter
def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)
AssumedWord = input("Enter what word you think the anagram was: ")
Original = input("Enter the anagram: ")
print(is_anagram(AssumedWord, Original))
