from my_class.get_yahoo_finance_csv import YahooCsv

yahoo = YahooCsv()

df = yahoo.get_csv2('ES=F', "2020-03-24", "1d")
print(df)