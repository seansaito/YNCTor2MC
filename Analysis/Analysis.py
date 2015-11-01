import json

with open('relays.json') as data_file:
    relay_list = json.load(data_file)

def as_analysis (relay_list):
    default = -5
    Unknown = 'Unknown'
    as_dictionary = {}
    for i in range(0, len(relay_list)):
        relay_dict = {}
        relay = relay_list[i]
        as_number = relay.get('as_number', Unknown)
        bw = relay.get('advertised_bandwidth', 0)
        or_addresses = relay['or_addresses']
        weight = relay['consensus_weight_fraction']
        fingerprint = [relay['fingerprint']]
        country = [relay.get('country_name', [])]
        if as_dictionary.get(as_number, default) == default:
            relay_dict['weight'] = weight
            relay_dict['bw'] = bw
            relay_dict['or_addresses'] = or_addresses
            relay_dict['fingerprint'] = fingerprint
            relay_dict['num'] = 1
            relay_dict['country'] = country
            as_dictionary[as_number] = relay_dict
        else:
            as_dictionary[as_number]['weight'] = as_dictionary[as_number]['weight'] + weight
            as_dictionary[as_number]['bw'] = as_dictionary[as_number]['bw'] + bw
            as_dictionary[as_number]['or_addresses'] = as_dictionary[as_number]['or_addresses'] + or_addresses
            as_dictionary[as_number]['fingerprint'] = as_dictionary[as_number]['fingerprint'] + fingerprint
            as_dictionary[as_number]['num'] = as_dictionary[as_number]['num'] + 1
            as_dictionary[as_number]['country'] = as_dictionary[as_number]['country'] + country
    print as_dictionary
    return as_dictionary

as_dictionary = as_analysis (relay_list)

fp = open("as_analysis.json", "w+")
fp.write(json.dumps(as_dictionary))
fp.close()
