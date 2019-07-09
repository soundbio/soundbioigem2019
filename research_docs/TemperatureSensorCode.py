
def binarytotemp(binary, positive): # binary is a string, positive is a boolean
    if positive:
        return sum([2**i for i in range(12) if binary[11-i]=="1"])/16
    else:
        return -(sum([2**i for i in range(12) if binary[11-i]=="0"])+1)/16
