# CraigslistScan
python program that pulls things from craigslist and outputs it in different formats



The motive behind this project was to find the cheapest car of some sort of kind Im looking at. I am a car enthusiast and wanted to create some program that would scrape all the craigslist sites and output those listings somwhere.

Now from VERSION 1.0 - VERSION 5.0 it is only about searching cars.

I am using @juliomalegria's module "craigslist":
https://github.com/juliomalegria/python-craigslist#classes
^If you want to know how the actual code works and how to manipulate things

The only thing I'm really doing is using his tool to seach for cars all across the USA. Along with that it outputs it into a .csv file 

VERSION 1.0-VERSION 4.0---> for sale. Cars/trucks specific

VERSION 1.0 : FirstClistProg.py ---> This verison was my first trial at this program. All it does is print the search results into the console. You have do adjust website and all that. It just pulls NAME, PRICE and URL from the output of @juliomalgeria's module. Look at the github of julio (linked line 12) to see all of the filters you can add and how to add.

VERSION 2.0: SecondClistProg.py ---> Same as VERSION 1.0 but all it does is output to a csv file for better looks

VERSION 3.0: ThirdClistProg.py ----> Rather than manually typing all websites, you adujust all other parts of the program (model, year, etc...) but it searches all of USA and outputs to a CSV file

VERSION 4.0: Haven't completed it yet. But probably only going to ask for what states you want to add to the search. Other input requests may come later. As of right now the only user input the program will request is states to include. You still have to add/change all other filters in the code. like change model, year etc... 
