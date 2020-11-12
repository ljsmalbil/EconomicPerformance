import pandas as pd
import numpy as np


from indicators import Indicators
from numpy import diff

consumer_conf_data_eu = pd.read_csv('eu_consumer_conf_2000_2020.csv')
print(consumer_conf_data_eu.head())



object = Indicators()
object.consumer_confidence(data = consumer_conf_data_eu)