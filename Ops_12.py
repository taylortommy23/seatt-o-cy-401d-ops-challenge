import ipaddress

# Creating an object of IPv4Address class and
# initializing it with an IPv4 address.
ip = ipaddress.IPv4Address('112.79.234.30')

# Print total number of bits in the ip.
print("Total no of bits in the ip: ", ip.max_prefixlen)

# Print True if the IP address is reserved for multicast use.
print("Is multicast: ", ip.is_multicast)

# Print True if the IP address is allocated for private networks.
print("Is private: ", ip.is_private)

# Print True if the IP address is global.
print("Is global: ", ip.is_global)

# Print True if the IP address is unspecified.
print("Is unspecified: ", ip.is_unspecified)

# Print True if the IP address is otherwise IETF reserved.
print("Is reversed: ", ip.is_reserved)

# Print True if the IP address is a loopback address.
print("Is loopback: ", ip.is_loopback)

# Print True if the IP address is Link-local
print("Is link-local: ", ip.is_link_local)

# next ip address
ip1 = ip + 1
print("Next ip: ", ip1)

# previous ip address
ip2 = ip - 1
print("Previous ip: ", ip2)

# Print True if ip1 is greater than ip2
print("Is ip1 is greater than ip2: ", ip1 > ip2)
