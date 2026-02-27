#simple code to count the vowels in a string

vowel = ["a", "e", "i", "o", "u"]


user = str(input("Enter the word you want to count : "))
count = 0

    
for j in user:
    for i in vowel:
        if j == i:
            count += 1

print(f"So there are {count} vowels in this word mister/miss. hehehe ")