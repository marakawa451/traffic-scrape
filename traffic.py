#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
from operator import itemgetter
import argparse

parser = argparse.ArgumentParser(description='POP')
parser.add_argument('pop',metavar='POP')
parser.add_argument("-p", "--platform", default="cache", help="enter the platform, cache is default")
args = parser.parse_args()

if args.platform=="cache":
        url = "http://grids.com:9000/cache-report?pop=" + args.pop + "&groups=bw"
else:
        url = "http://grids.com:9000/" + args.platform + "-report?pop=" + args.pop + "&groups=bw"

r = requests.get(url)
soup = BeautifulSoup(r.content)

g_data = soup.find_all("td", {"trend": "CacheMbits"})

def newfloat(key):
        new_key = key.split('M')[0]
        return float(new_key)

bwlist = {}
for item in g_data:
        bwlist.update({item.contents[0].get("href"): newfloat(item.contents[0].text)})

bestats = []
for key, value in sorted(bwlist.iteritems(), reverse=True, key=lambda (k,v): (v,k)):
        bestats.append(key)

def get_key(key):
        try:
                return float(key)
        except ValueError:
                exit

print("Top 4 Bw/out servers sorted by bytes")

for item in bestats[:4]:
        print(" ")
        print item
        print(" ")
        beurl = requests.get(item, verify=False)
        soupstats = BeautifulSoup(beurl.content)
        links = soupstats.find_all("tr")
        topcust = []
        for link in links:
                topcust.append([link.contents[0].string.strip(), get_key(link.contents[1].text),
                link.contents[2].string.strip()])
        maxcust = []
        for item in range(4):
                maxcust.append(max(topcust, key=itemgetter(1)))
                topcust.remove(max(topcust, key=itemgetter(1)))
        print("hex        bytes        cx")
        for hex, bw, cx in maxcust[:]:
                print hex, ' ',  bw, ' ',  cx

