'''

Created For Mega Projects Repository

Enter an IP address and find the country that IP is registered in.
Optional: Find the Ip automatically.

@author: Sambit

'''

#Imports
from ipwhois import IPWhois
import ipgetter

#Fetching the IP Address of own system
IP = ipgetter.myip()

obj = IPWhois(IP)
# Change the IP above for some other location

# Creates the dictionary containing the information returned
results = obj.lookup()

#Printing the output to the console
print results['nets'][0]['country']
