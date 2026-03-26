def dis(daam, discount):
    if daam < 0:
        print("invalid")
        exit()

    if discount < 0: 
        print("invalid")
        exit()

    final = (100-discount)/100 * daam
    return round(final, 2)

p = int(input("Enter the CP: "))

