from dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI
import bcolors

domain = 'google.com'

print("Domain that you want to searched",domain)
Domain_Search = DNSDumpsterAPI(True).search(domain)

print('Domain',Domain_Search)

print('\nDomain Name:',Domain_Search['domain'])


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
