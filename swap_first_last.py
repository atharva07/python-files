def swap_list(newlist):
    size = len(newlist)

    # swapping formula 
    temp = newlist[0]
    newlist[0] = newlist[size-1]
    newlist[size-1] = temp

    
    return newlist

newlist = [3,5,4,6,7]

print(swap_list(newlist))
