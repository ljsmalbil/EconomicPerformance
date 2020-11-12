import numpy as np

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

