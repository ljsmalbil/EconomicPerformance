import pandas as pd
from indicators import Indicators
import re

if __name__ == "__main__":
    consumer_conf_data_eu = pd.read_csv('eu_consumer_conf_2000_2020.csv')

    while True:
        begin = str(input('Please enter the begin time as follows: yyyy-mm. '))
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

    print('test')

    object = Indicators(begin = begin, end = end)
    object.consumer_confidence(data=consumer_conf_data_eu)