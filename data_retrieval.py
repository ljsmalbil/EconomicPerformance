import pandas as pd
import numpy as np
import re

# Data was retrieved from https://data.oecd.org/hha/household-debt.htm#indicator-chart

from indicators import Indicators
from numpy import diff

consumer_conf_data_eu = pd.read_csv('eu_consumer_conf_2000_2020.csv')
print(consumer_conf_data_eu.head())



object = Indicators()
object.consumer_confidence(data = consumer_conf_data_eu)
