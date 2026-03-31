# project 1, this project serves as an initial python project to refamiliarize myself with the python language as well as
# getting comfortable with using neovim and git/github. If you happened to clone this repo thinking it would be cool then
# I've got some bad news. But anyway, here goes nothing!

# Determine if an IP address provided by a user is within a given cidr range

from math import exp2

ip_address = input("What is the IP address? ")
cidr_range = input("What is the IP Range to check? ")

cidr_host_range = int(cidr_range[cidr_range.find('/') +1:])
#diagnostic print statements
print(cidr_host_range)
print(cidr_range)

cidr_range = cidr_range.split("/",1)[0] # strips off the subnet so we can also ensure each octet is correct
print(cidr_range) #diagnostic

cidr_range = cidr_range.split('.')
print(cidr_range) #dianostic
# Thought process here is that for CIDR ranges /24 and greater the address space is contained within the last octet so it's a 
# simple comparison of the values of that one octet. Should probably run a an if/else statement here to check for that possibility
# which will avoid the more complicated work of CIDR ranges that spread across more than one octet.

# Since we now have cidr_range as a list with each element containing one octet we should add logic to check each element and ensure
# it matches the IP address. Need to figure out where to implement that logic. 

if cidr_host_range >= 24:

    cidr_host_range = 32 - int(cidr_host_range)
    cidr_host_range = int(exp2(cidr_host_range)) - 1

    ip_address = ip_address.rsplit('.', maxsplit=1)
    ip_address = int(ip_address[-1])

    if ip_address < cidr_host_range and ip_address > 0:
        print("Yeah, shit is in that subnet fam")

    elif ip_address == cidr_host_range:
        print("Why you sending me the broadcast address? It's part of that subnet but like why you sending me that? ")

    elif ip_address == 0:
        print("That's the network address...it's your first day isn't it?")

    elif ip_address > cidr_host_range:
        print("Outside that range")
        print(f"CIDR upperbound is: {cidr_range}")
        print(f"Your IP host range ends in: {ip_address}")

    else:
        print("You might want to check that IP address...shit don't look right on this end")

#elif 


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
