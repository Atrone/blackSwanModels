import historicalCryptoTrendsGenerator
import cryptoInvestmentAdvisor
import datetime
import os
import tools

os.environ['generate'] = "Y"
os.environ['amountToInvest'] = "100"

if __name__ == "__main__":
    assert int(os.environ['amountToInvest'])
    if(os.environ['generate'] == "Y"):
        cryptoInvestmentAdvisor.getResults(historicalCryptoTrendsGenerator.getResults(
            datetime.datetime(2021, 7, 11), 336, 10)
                                           ,int(os.environ['amountToInvest']))
    elif(os.environ['generate'] == "N"):
        cryptoInvestmentAdvisor.getResults(tools.generateHistoricalCryptoTrendsGeneratorResultsFromCSV(datetime.datetime(2021, 7, 11))
                                           ,int(os.environ['amountToInvest']))
    else:
        print("please enter a valid generate value")