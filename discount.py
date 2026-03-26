def dis(daam, discount): #function
    if daam < 0:
        print("invalid")
        exit()

    if discount < 0: 
        print("invalid")
        exit()

    final = (100-discount)/100 * daam
    return round(final, 2)


print(dis(124432, 23)) #sample number, You can customize


