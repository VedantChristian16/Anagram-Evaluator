'''
Created by Vedant Christian
Created on 18 / 08 / 2020
'''

from collections import Counter
def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)
AssumedWord = input("Enter what word you think the anagram was: ")
Original = input("Enter the anagram: ")
print(is_anagram(AssumedWord, Original))
