# -*- coding: utf-8 -*-
"""
Created on Sun Jun 04 22:46:25 2017

@author: mnshr
"""
#https://www.hackerrank.com/challenges/merge-the-tools
from collections import OrderedDict
def merge_the_tools(string, k):
    # your code goes here
    S = string
    step = k
    index = 0
    slen = len(S)
    vals = []
    while index <= slen:
        substr = S[index:index + step]
        key = "".join(OrderedDict.fromkeys(substr))
        vals.append(key)
        index = index + step
    for i in range(len(vals)):
        print(vals[i])
        
#https://www.hackerrank.com/challenges/the-minion-game
def minion_game(string):
    # your code goes here
    s=string.strip()
    kevin = 0
    stuart = 0

    vowels = "AEIOU"
    slen = len(s)
    for i in range(slen):
        if vowels.find(s[i]) >= 0:
            kevin += (len(s) - i)
        else:
            stuart += (len(s) - i)

    if kevin > stuart:
        print "Kevin %d" %(kevin)
    elif kevin < stuart:
        print "Stuart %d" %(stuart)
    else:
        print "Draw"

#https://www.hackerrank.com/challenges/capitalize
def capitalize(string):
    s = string.strip().split(" ")

    words = []
    for i in range(len(s)):
        words.append(s[i].capitalize())

    return (" ".join(words))

#http://www.python-course.eu
#https://www.hackerrank.com/challenges/python-string-formatting
def print_formatted(number):
    # your code goes here
    wid=len(format(number,'b')) #To create space for all the 0/1 bits
    for i in xrange(1,number+1):
        print format(i,'d').rjust(wid,' '), format(i,'o').rjust(wid,' '), format(i,'x').upper().rjust(wid,' '), format(i,'b').rjust(wid,' ')

print_formatted(320)

#https://www.hackerrank.com/challenges/text-wrap
import textwrap
def wrap(string, max_width):
    return textwrap.fill(string, max_width)

#https://www.hackerrank.com/challenges/text-alignment
#Replace all ______ with rjust, ljust or center. 
#ljust, rjust, center alignment --MH
thickness = int(raw_input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print (c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1)

#Top Pillars
for i in range(thickness+1):
    print (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)

#Middle Belt
for i in range((thickness+1)/2):
    print (c*thickness*5).center(thickness*6)    

#Bottom Pillars
for i in range(thickness+1):
    print (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)    

#Bottom Cone
for i in range(thickness):
    print ((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6)    


#https://www.hackerrank.com/challenges/string-validators
if __name__ == '__main__':
    s = raw_input()
    print any(char.isalnum() for char in s) #Generator --MH
    print any(char.isalpha() for char in s) #any returns True if any 1 is true
    print any(char.isdigit() for char in s)
    print any(char.islower() for char in s)
    print any(char.isupper() for char in s)

#https://www.hackerrank.com/challenges/find-a-string
def count_substring(string, sub_string):
    cnt=0
    for i in range(len(string)):
        #print string[i:len(sub_string)]
        if sub_string==string[i:len(sub_string)+i]: #slice the string of length of sub_string
            cnt+=1  #compare and if equal then increment
    return cnt

#https://www.hackerrank.com/challenges/python-mutations
#Converting a list to string = use join with +
def mutate_string(string, position, character):
    ret=''
    lst=list(string)
    lst[position]=character
    for i in range(len(lst)):
        ret+=''.join(lst[i])
    return ret

#https://www.hackerrank.com/challenges/whats-your-name
def print_full_name(a, b):
    print "Hello %s %s! You just delved into python." %(a,b)
    #note the C style %s, combined with %(a,b)

#https://www.hackerrank.com/challenges/python-string-split-and-join
def split_and_join(line):
    #return '-'.join(line.split(' ')) #One line solution
    line=line.split(' ')
    line2='-'.join(line)
    return line2

#https://www.hackerrank.com/challenges/swap-case
def swap_case(s):
    s2='' #create the string
    for i in range(len(s)):
        s2+=''.join(s[i].swapcase()) #join a character and add to string
    return s2