#!/usr/bin/env python

import argparse, urllib2, json

def main():
        parser = argparse.ArgumentParser(description='Gets Circuit info from uber')
        parser.add_argument('name',metavar='circuit-name', help="Enter exact circuit name or to get all circuits for a provider in a pop")
        args = parser.parse_args()
        circuit = args.name
        jsonrequest = get_request(circuit)
        print_info(jsonrequest)

def get_request(circuit):
        w3tw2aPola3KxTr92a3nby3zq92380 = "api-key"
        url = 'https://api.com/circuit={}'.format(circuit)
        headers = ({'Authorization':'tok:' + w3tw2aPola3KxTr92a3nby3zq92380, 'Accept':'application/json'})
        r = urllib2.Request(url, None, headers)
        h = urllib2.urlopen(r)
        uberinfo =  json.loads(h.read())
        return uberinfo

# print json.dumps(y, indent=4)

def print_info(jsonrequest):
        print("\n[Name]                      "  + "[Circuit ID]        " + "[Remote WAN]    " + "[Local WAN]      " + "[ASN]")
        for i in jsonrequest:
                Name = i['Name']
                ID = i['VendorCircuitId']
                WAN = i['WanIPRemoteV4']
                LWAN = i['WanIPLocalV4']
                ASN = i['Asn']
                allcircuits = "{}      {}      {}     {}     {}".format(Name, ID, WAN, LWAN, ASN)
                print allcircuits

if __name__ == "__main__":
    main()
