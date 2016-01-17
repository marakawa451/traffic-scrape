#!/usr/bin/env python

import os
import argparse

def main():
        gomezip, pop = parsing()
        logpull(pop)
        searchfile(gomezip)

def parsing():
        parser = argparse.ArgumentParser()
        parser.add_argument('ip',metavar='[ip]', help='Enter the gomez node ip.')
        parser.add_argument('pop', metavar='[pop]', help='Enter the POP.')
        args = parser.parse_args()
        return args.ip, args.pop.lower()

def logpull(pop):
        print "\n---Pulling logs for storage" + " in " + pop
        print('---If the script does not complete, you must delete the gomezlogs00101.log file manually so you do not take up space.')
        if pop=="vny":
                print("---" + pop)
                os.system('/find storage ' + pop + ' | xargs -I {} -P 50 sh -c "curl -s -k -m 30 https://{}:\&start=`date -d "600 secs ago" +%s`\&end=`date -d "now" +%s` >> gomezlogs00101.log"')
        elif pop=="cpm":
                print("---" + pop)
                os.system('/find storage ' + pop + ' | xargs -I {} -P 50 sh -c "curl -s -k -m 30 https://{}:\&start=`date -d "600 secs ago" +%s`\&end=`date -d "now" +%s` >> gomezlogs00101.log"')
        elif pop=="lax":
                print("---" + pop)
                os.system('/find storage ' + pop + ' | xargs -I {} -P 50 sh -c "curl -s -k -m 30 https://{}:\&start=`date -d "600 secs ago" +%s`\&end=`date -d "now" +%s` >> gomezlogs00101.log"')
        elif pop=="ams":
                print('---' + pop)
                os.system('/find storage ' + pop + ' | xargs -I {} -P 50 sh -c "curl -s -k -m 30 https://{}:\&start=`date -d "600 secs ago" +%s`\&end=`date -d "now" +%s` >> gomezlogs00101.log"')
        elif pop=="nja":
                print('--Pulling logs for nja')
                os.system('/find storage ' + pop + ' | xargs -I {} -P 50 sh -c "curl -s -k -m 30 https://{}:\&start=`date -d "600 secs ago" +%s`\&end=`date -d "now" +%s` >> gomezlogs00101.log"')
        else:
                print('POP is invalid. Choose another. ')

def searchfile(gomezip):
        print('\n---Searching file for ' + gomezip + "\n" )
        f = open('gomezlogs00101.log', 'r')
        for line in f:
                if gomezip in line and "Gomez" in line:
                        print line
                        loglist = []
                        for i in line.split()[:5]:
                                loglist.append(i)
                        print(loglist[4] + '\n')
        f.close()
        print('---Search complete. End of file.')
        print('---Removing log file.')
        os.remove('gomezlogs00101.log')
        print('---gomezlogs00101.log log file removed successfully.\n')

if __name__ == "__main__":
    main()
