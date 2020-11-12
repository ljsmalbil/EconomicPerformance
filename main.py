"""

Author: L.Smalbil

This tool is meant to quickly retrieve important financial and economic information for a given country in a
given period.

"""

import pandas as pd
from indicators import Indicators
import re

if __name__ == "__main__":
    # Read Data

    consumer_conf_data_eu = pd.read_csv('eu_consumer_conf_2000_2020.csv')
    gdp_eu = pd.read_csv('eu_gdp_2000_2020.csv')
    house_hold_debt_eu = pd.read_csv('eu_household_debt_2000_2019.csv')
    unemployement_eu = pd.read_csv('eu_unemployement_2000_2020.csv')
    disposable_income_eu = pd.read_csv('eu_disposable_income_2000_2019.csv')

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

    # Return Information to User
    object = Indicators(country = country, begin = begin, end = end)
    object.consumer_confidence(data=consumer_conf_data_eu)
    print('\n')
    object.gdp(data = gdp_eu)
    print('\n')
    object.household_debt(data = house_hold_debt_eu)
    print('\n')
    object.unemployement(data = unemployement_eu)
    print('\n')
    object.disposable_income(data=disposable_income_eu)

