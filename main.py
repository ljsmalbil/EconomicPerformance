import pandas as pd
from indicators import Indicators
import re

if __name__ == "__main__":
    consumer_conf_data_eu = pd.read_csv('eu_consumer_conf_2000_2020.csv')
    gdp_eu = pd.read_csv('eu_gdp_2000_2020.csv')

    while True:
        begin = str(input('Please enter the begin year as follows: yyyy-mm. '))
        if bool(re.match('[0-9]{4}-[0-9]{2}', begin)) == False:
            print('Sorry, I did not quite catch that. Please try again')
            continue
        else:
            break

    while True:
        end = str(input('Please enter the end time as follows: yyyy-mm. '))
        if bool(re.match('[0-9]{4}-[0-9]{2}', end)) == False:
            print('Sorry, I did not quite catch that. Please try again')
            continue
        else:
            break

    while True:
        country = str(input('Please enter the country code: '))
        if bool(re.match('[A-Z]{3}|[A-Z]{4}', country)) == False:
            print('Sorry, I did not quite catch that. Please try again')
            continue
        else:
            break
    
    object = Indicators(country = country, begin = begin, end = end)
    object.consumer_confidence(data=consumer_conf_data_eu)
    object.gdp(data = gdp_eu)
