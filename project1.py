# project 1, this project serves as an initial python project to refamiliarize myself with the python language as well as
# getting comfortable with using neovim and git/github. If you happened to clone this repo thinking it would be cool then
# I've got some bad news. But anyway, here goes nothing!

# prospective project idea:
# Determine if an IP address provided by a user is within a given cidr range


#part 0: Call your variables, eat your vegetables
from math import exp2

ip_address = input("What is the IP address?")
cidr_range = input("What is the IP Range to check?")

cidr_range = int(cidr_range[cidr_range.find('/') +1:])

# Thought process here is that for CIDR ranges /24 and greater the address space is contained within the last octet so it's a 
# simple comparison of the values of that one octet. Should probably run a an if/else statement here to check for that possibility
# which will avoid the more complicated work of CIDR ranges that spread across more than one octet.

if cidr_range >= 24:

    print(cidr_range) # diagnostics, delete for final

    cidr_range = 32 - int(cidr_range)
    print(cidr_range) #diagnostic, delete for final

    cidr_range = int(exp2(cidr_range))
    print(cidr_range) # yup you guessed it, another diagnostic print statement

    

else:
    print("I have not built that part of this script yet, be patient")



#Core Method:
#Parse the CIDR notation into an IP address and a prefix length (e.g., 192.168.1.0/24 → network IP: 192.168.1.0, prefix: 24). 
#Convert both the target IP and the CIDR network IP to 32-bit integers.
#Create a subnet mask based on the prefix length:
#For /24, the mask is 255.255.255.0 → 0xFFFFFF00 in hex → 4294967040 in decimal.
#Apply the mask to both the target IP and the CIDR network IP using a bitwise AND operation. 
#Compare the results:
#If they are equal, the IP is within the CIDR range. 
#If they differ, it is not.

#Total IP addresses in a CIDR block:
#$ 2^{(32 - \text{prefix length})} $
#Example: For 192.168.1.0/26:
#$ 2^{(32 - 26)} = 2^6 = 64 $ total addresses. 
#Usable IP addresses:
#Subtract 2 (the network address and broadcast address):
#$ 64 - 2 = 62 $ usable addresses. 
#Subnet mask:
#Convert the prefix length to a binary mask (e.g., /24 → 11111111.11111111.11111111.00000000 → 255.255.255.0). 


# part 2: evaluate for CIDR range

# part 3: return True or False (boolean)
