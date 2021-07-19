import historicalCryptoTrendsGenerator
import datetime
import time
from typing import List, Dict

def getTotalOverTrendForCryptos(result):
    totalOverTrend = {}
    for key, value in result['price'].items():
        for key1, value1 in result['trends'].items():
            if key == key1:
                totalOverTrend[key1]= (abs((sum(result['trends'].values())/value1)))
                break
    return totalOverTrend

def getBuysForCryptosAccordingToTrends(result,totalOverTrend,dollarAmount):
    buys = []
    for key, value in result['price'].items():
        for key1, value1 in result['trends'].items():
            if key == key1:
                buys.append({key1:(abs(totalOverTrend[key1]/sum(totalOverTrend))*dollarAmount/value)})
                break
    print(buys)
    return buys

def getBuysForCryptos(result,dollarAmount,results):
    buys = []
    for key, value in result['price'].items():
        for key1, value1 in result['trends'].items():
            if key == key1:
                buys.append({key1:(dollarAmount/len(results[0].keys()))/value})
                break
    print(buys)
    return buys


def getCurrentPortfolioWorthFromBuys(buys):
    total = 0
    for buy in buys:
        for key, value in buy.items():
            total += value*historicalCryptoTrendsGenerator.getPriceForCryptoAtTime(str(datetime.datetime.now()),key.split(" ")[0])
    print(total)
    return total

    # total / trend proportionate to price / crypto
    # it's a hype market

def getResults(results : List[Dict], amountToInvest):
    for result in results:

        print(result['date'])

        totalOverTrend = getTotalOverTrendForCryptos(result)

        buysAccordingToTrends = getBuysForCryptosAccordingToTrends(result,totalOverTrend,amountToInvest)

        historicalCryptoTrendsGenerator.updateCSVForListOfDict(buysAccordingToTrends, "trendBuys"+
                                str(datetime.datetime.now().month)+
                                str(datetime.datetime.now().day)+".csv")

        print(getCurrentPortfolioWorthFromBuys(buysAccordingToTrends))

        buys = getBuysForCryptos(result, amountToInvest,results)

        historicalCryptoTrendsGenerator.updateCSVForListOfDict(buys, "nonTrendBuys"+
                                str(datetime.datetime.now().month)+
                                str(datetime.datetime.now().day)+".csv")

        print(getCurrentPortfolioWorthFromBuys(buys))

        time.sleep(65)