import urllib,urllib2
import re

# Textlocal API Key
apikey="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
# Number (or comma seperated list) of recipients
recipients=447516055755
# Stock values
stockSymbol="imo.l"
numStock=1000
buyPrice=128.4

def get_quote(symbol):
    base_url = 'http://finance.google.com/finance?q='
    content = urllib.urlopen(base_url + symbol).read()
    m = re.search('id="ref_(.*?)">(.*?)<', content)
    if m:
        quote = m.group(2)
    else:
        quote = 'no quote available for: ' + symbol
    return quote

def sendSMS(apikey, numbers, sender, message):
	data = 'apikey='+apikey+'&numbers='+str(numbers)+'&message='+message+'&sender='+sender
	request = urllib.urlopen("http://api.txtlocal.com/send?"+data)

currentValue = float(get_quote(stockSymbol))
profit = currentValue-buyPrice
overallProfit = numStock*profit
sendSMS(apikey,recipients,"StockUpdate",stockSymbol+" stock at "+str(currentValue)+"\nDiff: "+str(profit)+"\nValue: "+str(overallProfit)+"\n")
