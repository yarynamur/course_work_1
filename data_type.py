import json
import http.client
import quandl
from atd import MoviesBase
quandl.ApiConfig.api_key = 'rH3PSfJfH94wkuv_RCgt'


class MoviesFull:
    def __init__(self, year):
        self.year = year
        self.movies = MoviesBase(year)
        self.movies.set_movies_dict()
        self.stock_pr = {'MGM': None, 'DIS': None, 'TWX': None, 'FOX': None,
                         'UVV': None, 'LGF': None, 'NFLX': None, 'DRH': None, 'WWE': None}
        self.found_year = {'MGM': 1990, 'DIS': 1962, 'TWX': 1992, 'FOX': 1987,
                           'UVV': 1988, 'LGF': 1998, 'NFLX': 2002, 'DRH': 2005, 'WWE': 1999}
        self.set_prices()

    def stock_price(self, company, year, month):
        data = quandl.get_table('WIKI/PRICES', ticker=[company],
                                qopts={'columns': [
                                    'ticker', 'date', 'adj_close']},
                                date={'gte': year + '-' + month + '-01',
                                      'lte': year + '-' + month + '-31'},
                                paginate=True)
        new = data.set_index('date')
        clean_data = new.pivot(columns='ticker')
        with open('stock.txt', 'w') as outf:
            outf.write(str(clean_data))

    def get_month_stock_price(self, company, year, month):
        try:
            self.stock_price(company, year, month)
            average_stock = 0
            dates_amount = 0
            f = open("stock.txt", "r")

            for line in f:
                line = line.split()
                if line[0] != 'adj_close' and line[0] != 'date' and line[0] != 'ticker':
                    dates_amount += 1
                    average_stock += float(line[1])

            f.close()
            return round((average_stock / dates_amount), 2)
        except ValueError:
            return False

    def year_stock_price(self, company):
        monthly = []
        for month in range(12):
            try:
                stock = self.get_month_stock_price(
                    company, self.year, str(month+1))
            except ValueError:
                continue
            if stock != False:
                monthly.append(stock)
            else:
                stock = 0
                monthly.append(stock)
        counter = 0
        for num in monthly:
            if num != 0:
                counter += 1
        try:
            yearly = sum(monthly) / counter
            return round(yearly, 2)
        except:
            return None

    def set_prices(self):
        for comp in self.stock_pr:
            if int(self.year) >= self.found_year[comp]:
                self.stock_pr[comp] = self.year_stock_price(comp)
