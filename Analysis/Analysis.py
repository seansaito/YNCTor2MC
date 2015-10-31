import json

with open('relays.json') as data_file:
    relay_list = json.load(data_file)

def as_weight (relay_list):
    default = -5
    no_as = 'Unknown'
    as_dictionary = {}
    for i in range(0, len(relay_list)):
        relay = relay_list[i]
        as_number = relay.get('as_number',no_as)
        weight = relay['consensus_weight_fraction']
        if as_dictionary.get(as_number, default) == default:
            as_dictionary[as_number] = weight
        else:
            as_dictionary[as_number] = (weight + as_dictionary[as_number])
    print as_dictionary
    return as_dictionary

as_dictionary = as_weight (relay_list)

fp = open("as_weight_fraction.json", "w+")
fp.write(json.dumps(as_dictionary))
fp.close()
