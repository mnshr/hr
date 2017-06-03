# -*- coding: utf-8 -*-
"""
Created on Sat Jun 03 11:21:33 2017

@author: mnshr
"""

import multiprocessing

def spawn(num, num2):
    print('Spawned! {} -- {}'.format(num, num2)) #Need {} for format

def job(num):
    return num * 2

#__name__ Necessary in multiprocessing, will run only if the 
#script is being run, if the script is called it won't run
if __name__=='__main1__': 
    for i in range (55):                        
        p=multiprocessing.Process(target=spawn, args=(i,i+1)) #, need though 1 arg
        p.start()
        p.join() #waits for the process to be complete, helps thread coordination

#getting information back from a process
from multiprocessing import Pool
if __name__=='__main__':
    p=Pool(processes=20) #number of max processes
    data=p.map(job, range(200)) #map job to an iterable e.g. a generator here/list
    data2=p.map(job, [1, 3, 5])
    p.close()
    print(data) #a list of values from job process
    print (data2)