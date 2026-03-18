# project 1, this project serves as an initial python project to refamiliarize myself with the python language as well as
# getting comfortable with using neovim and git/github. If you happened to clone this repo thinking it would be cool then
# I've got some bad news. But anyway, here goes nothing!

# prospective project idea:
# Determine if an IP address provided by a user is within a given cidr range


#part 0: Call your variables, eat your vegetables


import sys

ip_address = sys.argv(0)
cidr_range = sys.argv(1)

#Core Method:
#Parse the CIDR notation into an IP address and a prefix length (e.g., 192.168.1.0/24 → network IP: 192.168.1.0, prefix: 24). 
#Convert both the target IP and the CIDR network IP to 32-bit integers.
#Create a subnet mask based on the prefix length:
#For /24, the mask is 255.255.255.0 → 0xFFFFFF00 in hex → 4294967040 in decimal.
#Apply the mask to both the target IP and the CIDR network IP using a bitwise AND operation. 
#Compare the results:
#If they are equal, the IP is within the CIDR range. 
#If they differ, it is not.



# part 2: evaluate for CIDR range

# part 3: return True or False (boolean)
