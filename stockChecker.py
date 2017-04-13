from yahoo_finance import Share
from pprint import pprint
import json

stockShortCode = 'GOOG'
stock = Share(stockShortCode)
start = '2016-10-01'
end = '2017-04-10'
change = 0
history = (stock.get_historical(start, end))
stockChange = []
chngList = []
chngInRng = 0.0
numberOfEntries = 0
outputJson = 'stockTest.json'

#Finds all entries (date, open, and close prices) in the API response we care about.
#From the open and close values, it calculates the change for that day.
for day in range(0,1000):
    try:
        change = str(float(history[day]['Close']) - float(history[day]['Open']))
        chngList.append(change)
        stockChange.append({
            "Date": (str(history[day]['Date'])),
            "Start": (str(history[day]['Open'])),
            "End": (str(history[day]['Close'])),
            "Change": (change[:5]),
            })
    except IndexError:
        #prevents the code failing when there are fewer than the max range entries in the response.
        pass

#Test for the other yahoo_finance methods
print(stock.get_ebitda())

#Calculates the number of entries in the newly updated variable for use in later for loop.
numberOfEntries = (len(stockChange))

#Calculate the total change in stock across the date range set.
chngInRng = str(float(stockChange[0]['End']) - float(stockChange[numberOfEntries - 1]['Start']))

print("Change from " + start + " to " + end + " = " + str(chngInRng[:5]))

#Deletes the content of outputJson before updating the file.
with open(outputJson, 'w') as stockDel:
    stockDel.truncate()
    
#Creates a json file with all historic values as discrete dictionaries, using the length of the stockChange list
# as the upper limit to prevent overrun.
with open(outputJson, 'a') as stockfile:
    for j in range(numberOfEntries):
        try:
            json.dump(stockChange[j], stockfile)
        except IndexError:
            pass
