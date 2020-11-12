import numpy as np
import re

class Indicators:
    def __init__(self, country = 'NLD', begin = '2018-01', end = '2019-12'):
        self.country = country
        self.begin = begin
        self.end = end

    def consumer_confidence(self, data):
        # Subset Country
        data = data[data['LOCATION'] == self.country]

        # Subset for the given time frame
        subset = data[data.TIME.str.startswith((self.begin, self.end))]

        # Compute the difference
        delta = (np.array(subset['Value'])[1] - np.array(subset['Value'])[0]) / np.array(subset['Value'])[1]

        # Return the difference
        print('Consumer Confidence in ' + self.country + ' from ' + self.begin + ' to ' + self.end + ' has ' + str(
            'decreased' if delta < 0 else 'increased') + ' by ' + str(round(delta, 3)) +'.')

    def gdp(self, data):
        # Subset Country
        data = data[data['LOCATION'] == self.country]

        begin_year = re.search('[0-9]{4}', self.begin)
        end_year = re.search('[0-9]{4}', self.end)

        begin_year = int(begin_year.group(0))
        end_year = int(end_year.group(0))

        # Subset for the given time frame
        subset = data[(data['TIME'] == begin_year) | (data['TIME'] == end_year)]

        # Compute the difference
        delta = (np.array(subset['Value'])[1] - np.array(subset['Value'])[0]) / np.array(subset['Value'])[1]

        print('The per capita GDP (in dollars) in ' + str(begin_year) + ' was ' + str(np.round(
            np.array(subset['Value'])[0],2)) + '.\nThe GDP in ' + str(end_year) + ' was ' + str(np.round(
            np.array(subset['Value'])[1],2)) + '.')

        # Return the difference
        print('The per capita GDP in ' + self.country + ' from ' + str(begin_year) + ' to ' + str(end_year) + ' has ' + str(
            'decreased' if delta < 0 else 'increased') + ' by ' + str(round(delta, 3)) +'.')

    def household_debt(self, data):
        # Subset Country
        data = data[data['LOCATION'] == self.country]

        begin_year = re.search('[0-9]{4}', self.begin)
        end_year = re.search('[0-9]{4}', self.end)

        begin_year = int(begin_year.group(0))
        end_year = int(end_year.group(0))

        # Subset for the given time frame
        subset = data[(data['TIME'] == begin_year) | (data['TIME'] == end_year)]

        # Compute the difference
        delta = (np.array(subset['Value'])[1] - np.array(subset['Value'])[0]) / np.array(subset['Value'])[1]

        # Return the difference
        print('The household debt in ' + str(begin_year) + ' was '+ str(np.array(subset['Value'])[0]) + '.\nThe household debt in ' + str(end_year) + ' was ' + str(np.array(subset['Value'])[1]) +  '.')

        print('The household debt in ' + self.country + ' from ' + str(begin_year) + ' to ' + str(end_year) + ' has ' + str(
            'decreased' if delta < 0 else 'increased') + ' by ' + str(round(delta, 3)) + '.')

    def unemployement(self, data):
        # Subset Country
        data = data[data['LOCATION'] == self.country]

        begin_year = re.search('[0-9]{4}', self.begin)
        end_year = re.search('[0-9]{4}', self.end)

        begin_year = int(begin_year.group(0))
        end_year = int(end_year.group(0))

        # Subset for the given time frame
        subset = data[(data['TIME'] == begin_year) | (data['TIME'] == end_year)]

        # Compute the difference
        delta = (np.array(subset['Value'])[1] - np.array(subset['Value'])[0]) / np.array(subset['Value'])[1]

        # Return the difference
        print('The unemployment rate in ' + str(begin_year) + ' was ' + str(np.round(
            np.array(subset['Value'])[0],2)) + '.\nThe unemployment rate in ' + str(end_year) + ' was ' + str(np.round(
            np.array(subset['Value'])[1],2)) + '.')

        print('The unemployment rate in ' + self.country + ' from ' + str(begin_year) + ' to ' + str(
            end_year) + ' has ' + str(
            'decreased' if delta < 0 else 'increased') + ' by ' + str(round(delta, 3)) + '.')

    def disposable_income(self, data):
        # Subset Country
        data = data[data['LOCATION'] == self.country]

        begin_year = re.search('[0-9]{4}', self.begin)
        end_year = re.search('[0-9]{4}', self.end)

        begin_year = int(begin_year.group(0))
        end_year = int(end_year.group(0))

        # Subset for the given time frame
        subset = data[(data['TIME'] == begin_year) | (data['TIME'] == end_year)]

        # Compute the difference
        delta = (np.array(subset['Value'])[1] - np.array(subset['Value'])[0]) / np.array(subset['Value'])[1]

        # Return the difference
        print('The disposable income (in percentage points) in ' + str(begin_year) + ' was ' + str(np.round(
            np.array(subset['Value'])[0],2)) + '.\nThe disposable income in ' + str(end_year) + ' was ' + str(np.round(
            np.array(subset['Value'])[1],2)) + '.')

        print('The disposable income rate in ' + self.country + ' from ' + str(begin_year) + ' to ' + str(
            end_year) + ' has ' + str(
            'decreased' if delta < 0 else 'increased') + ' by ' + str(round(delta, 3)) + '.')

    def wages(self, data):
        # Subset Country
        data = data[data['LOCATION'] == self.country]

        begin_year = re.search('[0-9]{4}', self.begin)
        end_year = re.search('[0-9]{4}', self.end)

        begin_year = int(begin_year.group(0))
        end_year = int(end_year.group(0))

        # Subset for the given time frame
        subset = data[(data['TIME'] == begin_year) | (data['TIME'] == end_year)]

        # Compute the difference
        delta = (np.array(subset['Value'])[1] - np.array(subset['Value'])[0]) / np.array(subset['Value'])[1]

        # Return the difference
        print('The average wage (in dollars) in ' + str(begin_year) + ' was ' + str(np.round(
            np.array(subset['Value'])[0],2)) + '.\nThe dollar wage in ' + str(end_year) + ' was ' + str(np.round(
            np.array(subset['Value'])[1],2)) + '.')

        print('The dollar income rate in ' + self.country + ' from ' + str(begin_year) + ' to ' + str(
            end_year) + ' has ' + str(
            'decreased' if delta < 0 else 'increased') + ' by ' + str(round(delta, 3)) + '.')

    def tax_revenue(self, data):
        # Subset Country
        data = data[data['LOCATION'] == self.country]

        begin_year = re.search('[0-9]{4}', self.begin)
        end_year = re.search('[0-9]{4}', self.end)

        begin_year = int(begin_year.group(0))
        end_year = int(end_year.group(0))

        # Subset for the given time frame
        subset = data[(data['TIME'] == begin_year) | (data['TIME'] == end_year)]

        # Compute the difference
        delta = (np.array(subset['Value'])[1] - np.array(subset['Value'])[0]) / np.array(subset['Value'])[1]

        # Return the difference
        print('The tax revenue (as percentage of GDP) in ' + str(begin_year) + ' was ' + str(np.round(
            np.array(subset['Value'])[0], 2)) + '.\nThe tax revenue (as percentage of GDP) in ' + str(end_year) + ' was ' + str(np.round(
            np.array(subset['Value'])[1], 2)) + '.')

        print('The tax revenue rate in ' + self.country + ' from ' + str(begin_year) + ' to ' + str(
            end_year) + ' has ' + str(
            'decreased' if delta < 0 else 'increased') + ' by ' + str(round(delta, 3)) + '.')




