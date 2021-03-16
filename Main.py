#! python3
from Scrape import *

#getCharacterData - two parameters - first is the level that the loop will STOP once it hits.  Second parameter is how many characters PER CLASS it will extract.
for key, value in Scrape().getCharacterData(78,1).items(): 
    Scrape().getCharInventoryData(key, value[0], value[1]).addToCSV()