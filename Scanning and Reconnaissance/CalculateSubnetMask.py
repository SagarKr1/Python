
def calculateSubnetMask(subnet="0.0.0.0"):
    mask = subnet.split(".")
    bin_list = []
    total_subnet=0
    for i in mask:
        binary_data = bin(int(i))[2:].zfill(8)
        total_subnet += binary_data.count('1')
        bin_list.append(binary_data)
    
    # print(bin_list)
    return {
        "list":bin_list,
        "total_subnet":total_subnet
    }

# Example usage
sbnet_mask = "255.255.254.0"
total=calculateSubnetMask(sbnet_mask)

print(total)