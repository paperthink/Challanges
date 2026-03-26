def reverse(input_text):
    for letter in input_text:
        input_text = letter + input_text

    print(input_text)

a = reverse(input("Enter any word: "))
