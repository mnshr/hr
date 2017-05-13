# -*- coding: utf-8 -*-
"""
Created on Fri May 12 23:08:06 2017

@author: mnshr
"""

from collections import Counter

def ransom_note(magazine, ransom):
    magazine_counter = Counter(magazine)
    ransom_counter = Counter(ransom)

    if magazine_counter & ransom_counter == ransom_counter:
        return True

    return False    

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
    

