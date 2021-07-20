import datetime
import os

from aiohttp import web
import main
import tools


async def handle(request):
    startDate = datetime.datetime.strptime(request.rel_url.query['startDate'],"%Y-%m-%d %H:%M:%S")
    startDatePlusOne = datetime.datetime.strptime(request.rel_url.query['startDate'],"%Y-%m-%d %H:%M:%S") + datetime.timedelta(days=1)

    main.createResponseCSVs(True,startDate,
                            int(request.rel_url.query['hours']),
                            int(request.rel_url.query['limit']),
                            int(request.rel_url.query['dollars']))
    priceData = (tools.make_json('price'+tools.dateTimeToMonthTDay(startDate)+".csv"))
    trendsData = (tools.make_json('trends'+tools.dateTimeToMonthTDay(startDate)+".csv"))
    trendBuysData = (tools.make_json('trendBuys'+tools.dateTimeToMonthDay(startDatePlusOne)+".csv"))

    return web.Response(text=(priceData + trendsData + trendBuysData))

if __name__ == "__main__":
    app = web.Application()
    app.router.add_get('/generateHistoricalPriceTrendsAndAdvise', handle)

    web.run_app(app, port=os.getenv('PORT'))
