import bcolors
import sys, argparse
import os
import requests
from dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI

def banner():
    print("""
                ██████╗░███╗░░██╗░██████╗░░░░░░██████╗░███████╗░█████╗░░█████╗░██████╗░██████╗░░██████╗
                ██╔══██╗████╗░██║██╔════╝░░░░░░██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝
                ██║░░██║██╔██╗██║╚█████╗░█████╗██████╔╝█████╗░░██║░░╚═╝██║░░██║██████╔╝██║░░██║╚█████╗░
                ██║░░██║██║╚████║░╚═══██╗╚════╝██╔══██╗██╔══╝░░██║░░██╗██║░░██║██╔══██╗██║░░██║░╚═══██╗
                ██████╔╝██║░╚███║██████╔╝░░░░░░██║░░██║███████╗╚█████╔╝╚█████╔╝██║░░██║██████╔╝██████╔╝
                ╚═════╝░╚═╝░░╚══╝╚═════╝░░░░░░░╚═╝░░╚═╝╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░╚═════╝░
                                                                                           Code By: NG
              """
          )
if len(sys.argv) > 1:
    banner()
    if (sys.argv[1] != 'd'):
        try:
            input_url = sys.argv[2]
            input_location = sys.argv[2]
            parser = argparse.ArgumentParser()
            parser.add_argument("-d", required=True)

            print(bcolors.BITALIC + "**********************************************************Testing for DNS records**************************************************")
            if(os.path.exists(input_location) == True):
                file = open(input_location,"r")
                lines = file.readlines()
                for te in lines:
                    domain = te.strip()

                    print("Domain that you want to searched", domain)
                    Domain_Search = DNSDumpsterAPI(True).search(domain)

                    print('\nDomain Name:', Domain_Search['domain'])
                    print('\n***********DNS Records******************')
                    for detail in Domain_Search['dns_records']['dns']:
                        print(detail)

                    print('\n**********MX Records********************')
                    for detail in Domain_Search['dns_records']['mx']:
                        print(detail)

                    print('\n*********HOST Records*******************')
                    for detail in Domain_Search['dns_records']['host']:
                        print(detail)

                    print('\n*********TXT Records********************')
                    for detail in Domain_Search['dns_records']['txt']:
                        print(detail)

            elif(os.path.exists(input_location) != True):
                domain = input_url
                print("Domain that you want to searched", domain)
                Domain_Search = DNSDumpsterAPI(True).search(domain)

                print('\nDomain Name:', Domain_Search['domain'])
                print('\n***********DNS Records******************')
                for detail in Domain_Search['dns_records']['dns']:
                    print(detail)

                print('\n**********MX Records********************')
                for detail in Domain_Search['dns_records']['mx']:
                    print(detail)

                print('\n*********HOST Records*******************')
                for detail in Domain_Search['dns_records']['host']:
                    print(detail)

                print('\n*********TXT Records********************')
                for detail in Domain_Search['dns_records']['txt']:
                    print(detail)

        except:
            print(bcolors.OKMSG + 'Please enter python dnsRecords.py -u <valid Doamin without https:// or http://> ')
    elif (sys.argv[1] == '-h'):
        print(bcolors.BOLD + 'usage: dnsRecords.py [-h] -u URL' '\n' 'OPTIONS:' '\n' '-h,--help    '
                             'show this help message and exit' '\n''-u Domian')
    elif (sys.argv[1] != '-d'):
        print(bcolors.OKMSG + 'Please enter -d < valid domain without http:// or https:// >')
else:
    banner()
    print(bcolors.ERR + 'Please select at-least 1 option from -d or -h, with a valid domain')



