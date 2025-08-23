word = str(input("Enter a word or phrase: ")).lower()

if word == word[::-1]:
    print("Palindrome achieved.")
else:
    print("Ts is not a palindrome")