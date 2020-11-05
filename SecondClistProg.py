# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 21:48:56 2020

@author: Vyom

outputs shit to a csv file thats all

VERSION 2.0
"""

from craigslist import CraigslistForSale as cl

# txcite  = ['dallas','austin','houston','collegestation','waco','galveston','lubbock','sanantonio']

# uscite = [] these 2 lines are useless it was just for me thinking how to get all states and and cites in it. i ended up doing somethign else in VERSION #3.0

a = cl(site='dallas' ,category = 'cta', filters={'max_year':'1972', 'model':'corvette'})

# print("{:<20}{:<12}{:<100}".format('Name','Price','Link'))

    

with open('clist1.csv','w', encoding='utf-8') as writein: #encoding utf-8 addition to allow odd charcters to be removed
    
    for result in a.get_results(sort_by='price_asc'):
        values = result.values()
        values_list = list(values)
        
        pr = values_list[6]
        # pt = values_list[2]
        
        # values_list[2] = str(pt.replace('\U0001f31f',''))
        values_list[6] = str(pr.replace(',',''))
        
        print(str(values_list[2])+','+str(values_list[6])+','+str(values_list[3])+'\n')
        
        output = str(values_list[2])+','+str(values_list[6])+','+str(values_list[3])+'\n'
        
        writein.write(output)