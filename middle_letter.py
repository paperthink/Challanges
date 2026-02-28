def get_middle(s):
    can_middle = False
    size = len(s)
    if size % 2 != 0:
        can_middle = True
        if can_middle ==True:
            for a in range(size):
                if a == size//2:#median formula(for odd)
                    #we know that indices count from 0 so anything/2 is always +1 from our expectations
                    print(s[a])
                    break
    if size % 2==0:
        can_middle = False
        if can_middle == False:
            print(s[size//2 - 1]+s[size//2])

get_middle(input("Enter any String: "))