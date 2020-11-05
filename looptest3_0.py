# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 18:25:34 2020

@author: Vyom

just some basic loop testing that will be used in VERSION 4.0
"""

cites = []

yn = 1

while yn == 1:

    add_state = input('Enter states: ')
    
    if add_state != 'done':
        def state():
            with open(add_state+'.txt') as readfile:
                statestring = readfile.read()
                
                statelist = statestring.split('\n')
                return statelist
        cites += state()
        
    else:
        break

print(cites)