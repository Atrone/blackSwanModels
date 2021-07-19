import historicalCryptoTrendsGenerator
import cryptoInvestmentAdvisor
import datetime

if __name__ == "__main__":
    cryptoInvestmentAdvisor.getResults(historicalCryptoTrendsGenerator.getResults(
        datetime.datetime(2021, 7, 11), 336, 10)
                                       ,100)