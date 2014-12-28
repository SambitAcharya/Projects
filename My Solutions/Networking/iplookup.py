'''

Created For Mega Projects Repository

Enter an IP address and find the country that IP is registered in.
Optional: Find the Ip automatically.

@author: Sambit

'''

#Imports
from ipwhois import IPWhois
from ipwhois.utils import get_countries
import ipgetter

#Fetching the IP Address of own system
IP = ipgetter.myip()

countries = get_countries()

# Change the IP above for some other location
obj = IPWhois(IP)

# Creates the dictionary containing the information returned
results = obj.lookup(False)

#Printing the output to the console
print countries[results['nets'][0]['country']]
