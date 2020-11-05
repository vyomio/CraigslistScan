# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 14:38:47 2020

@author: Vyom

outputs shit to console thats all

very first program

VERSION 1.0
"""



from craigslist import CraigslistForSale as cl

a = cl(site='dallas',category = 'cta', filters={'max_year':'1972', 'model':'corvette'})

# e = []
# j = []

print("{:<20}{:<12}{:<100}".format('Name','Price','Link'))

for result in a.get_results(sort_by='price_asc'):
    # print(result, "\n")
    values = result.values()
    values_list = list(values)
    # print(values_list[3])
    
    print('{:<20}{:<12}{:<100}'.format(values_list[2],values_list[6],values_list[3]))
    
    # c=str(result)
    # d=c.split(', ')
    # print(d[6])
    
    # for i in range(len(d)):
    #     e.append(d[i].split(": "))
    
    # print(e[6], 'and', e[6][1])
    
    # for k in range(len(e)):
    #     j.append(e[k][1])
    # d=[]
    
    
    # print(j[6])
    # print(len(j))
    # print(j[10])
    