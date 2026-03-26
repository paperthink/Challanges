def reverse(input_text):
    revers = ""
    for letter in input_text:
        revers = letter + revers

    return revers

a = reverse(input("Enter any word: "))
print(a)
