import datetime
import time
import pandas as pd
import pandas_datareader.data as web


class YahooCsv:
    '''
        Получени CSV с Yahoo
    '''

    @staticmethod
    def get_csv(symbol, date_start, interval="1d", events="history"):
        '''
            symbol: type str
            date_start: type str, имеет вид yyyy-mm-dd
            interval: type str, 1d
        '''
        date1 = datetime.datetime.strptime(date_start, '%Y-%m-%d').date()
        date2 = datetime.date.today()

        period1 = int(time.mktime(date1.timetuple()))
        period2 = int(time.mktime(date2.timetuple()))

        url_ticket = "https://query1.finance.yahoo.com/v7/finance/download/{}?period1={}&period2={}&interval={}&" \
                     "events=history&includeAdjustedClose=true".format(symbol, period1, period2, interval)
        csv_dataframe = pd.read_csv(url_ticket, parse_dates=True, index_col=0)
        csv_dataframe.to_csv('csv_date/{}.csv'.format(symbol))
        return "get \033[32m{}, {} - {}".format(symbol, date1, date2)

    @staticmethod
    def get_csv2(symbol, date_start, interval="1d", events="history"):
        '''
            symbol: type str
            date_start: type str, имеет вид yyyy-mm-dd
            interval: type str, 1d
        '''

        date1 = datetime.datetime.strptime(date_start, '%Y-%m-%d').date()
        date2 = datetime.date.today()

        csv_file = web.get_data_yahoo(symbol, date1, date2)
        csv_file.to_csv('csv_date/{}.csv'.format(symbol))

        return "get \033[32m{}, {} - {}".format(symbol, date1, date2)