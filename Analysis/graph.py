import json
import csv
from collections import Counter

with open('as_analysis.json') as data_file:
    as_data = json.load(data_file)
    del as_data["AS37002"]

def as_clean (as_data):
    default = -5
    country_dict = {}
    for i in range(0, len(as_data.items())):
        current_relay = as_data.items()[i][0]
        countrylist = as_data[current_relay]['country']
        country = Counter(countrylist).most_common(1)[0][0]
        weight = as_data[current_relay]['weight']
        if country_dict.get(country, default) == default:
            country_dict[country] = weight
        else:
            country_dict[country] = country_dict[country] + weight
    return country_dict

country_dict = as_clean (as_data)

with open('country_data.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                            quotechar='', quoting=csv.QUOTE_NONE)
    for i in range(0, len(country_dict.items())):
        writer.writerow([country_dict.items()[i][0], country_dict.items()[i][1]])
