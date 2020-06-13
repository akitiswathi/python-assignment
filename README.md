# python-assignment
1.ebook.py---Problem Statement Design a ‘book’ class with title, author, publisher, price and author’s royalty as instance variables. Provide getter and setter properties for all variables. Also define a method royalty() to calculate royalty amount author can expect to receive the following royalties:10% of the retail price on the first 500 copies; 12.5% for the next 1,000 copies sold, then 15% for all further copies sold. 
 
Then design a new ‘ebook’ class inherited from ‘book’ class. Add ebook format (EPUB, PDF, MOBI etc) as additional instance variable in inherited class. Override royalty() method to deduct GST @12% on ebooks.

2.man of the match(fun[1].py,cricket.py)--- 
SCENARIO: 
The 'Man of the Match' award of a 50-over cricket match is decided by computing points  earned by players. The points are calculated on the basis of the following rules:  


BATTING:
● 1 point for 2 runs scored 
● Additional 5 points for a half-century  
● Additional 10 points for a century
● 2 points for strike rate (runs/balls faced) of 80-100 
● Additional 4 points for strike rate>100  
● 1 point for hitting a boundary (four) and 2 points for over boundary (six) 



BOWLING:
● 10 points for each wicket 
● Additional 5 points for three wickets in innings 
● Additional 10 points for 5 wickets or more in innings 
● 4 points for economy rate (runs given per over) between 3.5 and 4.5 
● 7  points for an economy rate between 2 and 3.5  
● 10 points for an economy rate less than 2



FIELDING:
● 10 points each for catch/stumping/run out



PROBLEM STATEMENT:
Assuming the 5 performers, write a Python program to decide the player  with the highest points. Develop separate functions to compute batting and bowling points  and save them in a module. These functions should be imported into the main code.  
