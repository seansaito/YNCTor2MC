#Making calls from Onionoo
import httplib2, json

#class Calls(object):

#fields = "fields=fingerprint,or_addresses,country,as_number,consensus_weight_fraction,advertised_bandwith"
data = "details"
h = httplib2.Http(".cache")
url = "https://onionoo.torproject.org/{type}?running=true".format(type=data) #,fields=data)
content = h.request(url, "GET")
def convert_from_raw():
    data = "details"
    h = httplib2.Http(".cache")
    url = "https://onionoo.torproject.org/{type}?running=true".format(type=data) #,fields=data)
    resp, content = h.request(url, "GET")
    json_data = json.loads(content)
    print json_data["relays"]
    return json_data["relays"]

dictionary = convert_from_raw()

print dictionary

fp = open("relays.json", "w+")
fp.write(json.dumps(dictionary))
fp.close()
