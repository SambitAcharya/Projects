'''

Created For Mega Projects Repository

Enter an IP or host address and have it look it up through whois and
return the results to you.

@author: Sambit

'''

#Imports
from ipwhois import IPWhois
from pprint import pprint
import ipgetter

#Fetching the IP Address of own system
IP = ipgetter.myip()

obj = IPWhois(IP)
# Change the IP above for some other location

# Creates the dictionary containing the information returned
results = obj.lookup()

#Printing the output to the console
pprint(results)
