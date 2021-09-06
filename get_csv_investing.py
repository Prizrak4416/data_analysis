import investpy
import pandas as pd

search_result = investpy.search_quotes(text='VX', countries=['united states'], n_results=1)
print(search_result)
his_date = search_result.retrieve_historical_data(from_date='01/01/2020', to_date='03/09/2021')
print(his_date.tail())
his_date.to_csv("csv_date/VX_US500.csv")

