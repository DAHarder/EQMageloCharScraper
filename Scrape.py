import webbrowser
import requests
import bs4
import csv
from CharacterInventory import *
from CharacterInventoryDict import *

tableUrl = 'http://magelo.ezserver.online/index.php?page=search&name=a&guild=&orderby=level&direction=DESC&start=' #Used with getCharacterData
inventoryUrl = 'http://magelo.ezserver.online/index.php?page=character&char=' #Used with getCharInventoryData

class Scrape:

    def __init__(self):
        pass
    
    def getCharacterData(self, stopLevel, classCount):
        # classCount is the max count of each class per level that is wanted.
        # stopLevel is the min level to go to, such as 55, 65, etc.
        # add level and class together
        # if level+class item count greater than 10, skip

        # Writes data to a file in case of wanting to stop the script - you delete entries and start again using the file data
        with open('character_level_csv.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Name', 'Level', 'Class'])

            charDict = {} # Character name as key and array with class and level as data - Use with getCharInventoryData
            charClassLevelCountDict = {} #Character class and level concatenated together as key with count as data 
            tableNavCount = 0 #Counts each 'next' button of the table - in 25 count increments
            loopCount = 0 #TEMP PLACEHOLDER FOR levelMax

            # characterURL = 'http://magelo.ezserver.online/index.php?page=character&char='
            # while level != '78':
            print('Scraping Data...')
            # Go through each table item, then go to the next 25 items in the table
            level = 80
            while stopLevel < int(level):
                res = requests.get(tableUrl+str(tableNavCount))
                res.raise_for_status()
                soup = bs4.BeautifulSoup(res.text, 'html.parser')
                #Go through each item in the table and add it to the CharDict Map
                for i in range(2,27):
                    try:
                        name = soup.select('tr:nth-child(' + str(i) + ') > td:nth-child(1)')[0].text.strip()
                        level = soup.select('tr:nth-child(' + str(i) + ') > td:nth-child(3)')[0].text.strip()
                        charClass = soup.select('tr:nth-child(' + str(i) + ') > td:nth-child(4)')[0].text.strip()
                        classLevelCombo = level + charClass
                        if classLevelCombo in charClassLevelCountDict.keys():
                            if charClassLevelCountDict[classLevelCombo] < classCount:            
                                charDict[name] = [level, charClass]
                                charClassLevelCountDict[classLevelCombo] = charClassLevelCountDict[classLevelCombo] + 1
                                writer.writerow([name, level, charClass])
                        else:
                            charClassLevelCountDict.update({classLevelCombo : 1})
                            charDict[name] = [level, charClass]
                            writer.writerow([name, level, charClass])
                    except:
                        print('failed to get data')
                        # pass

                tableNavCount += 25
                loopCount += 1
                print('Getting Character names from page ' +  str(loopCount) + '...')
        print('Starting data scrape for inventory')
        return charDict
        
        
    def getCharInventoryData(self, name, level, charClass): #add name, level, class - import from getCharacterList
        url = inventoryUrl + name

        res = requests.get(url)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        characterInv = CharacterInventory()

        characterInv.name = name
        characterInv.level = level
        characterInv.charClass = charClass

        for slot, item in characterInvDict.items():
            try:
                vars(characterInv)[slot] = soup.select(item)[0].text.strip()
            except:
                continue
        
        for x in range(251, 350):
            slot = '#slot' + str(x)
            elems = soup.select(slot + '> div.ItemTitle')

            try:
                if elems[0].text.strip().find('Mold') != -1 or elems[0].text.strip().find('Mold') != -1:
                    characterInv.patterns.append(elems[0].text.strip())
            except:
                continue
        print('Getting inventory for ' + name)
        return characterInv


#-----MISC------
    def getSlotData(self, URL):
        res = requests.get(URL)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        for x in range(251, 350):
            slot = '#slot' + str(x)
            elems = soup.select(slot + '> div.ItemTitle')
            slotName = soup.select(slot + '> div.ItemInner')
            try:
                if elems[0].text.strip().find('Mold') != -1:
                    print(x, end=' ')
                    print(slotName[0].text[slotName[0].text.find('Slot:'):slotName[0].text.find('Slot:') + 15] + "| " + elems[0].text.strip())
            except:
                continue
                # print('emtpy')

# for key, value in Scrape().getCharacterData(78,1).items():
#     # print(key, value[0], value[1])
#     Scrape().getCharInventoryData(key, value[0], value[1])
# Scrape().getCharacterData(1,1)

# Scrape().getSlotData('http://magelo.ezserver.online/index.php?page=character&char=Himurra')