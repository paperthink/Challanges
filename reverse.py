def reverse(input_text):
    for letter in input_text:
        input_text = letter + input_text

    return input_text

a = reverse(input("Enter any word: "))
print(a)