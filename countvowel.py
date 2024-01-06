a = input("Enter your word: ")
vowel = 0
consonant = 0

for i in range(0, len(a)):
    if a[i].isalpha():  # Checking if the character is an alphabet
        if (a[i] == "a" or a[i] == "e" or a[i] == "i" or a[i] == "o" or a[i] == "u" 
            or a[i] == "A" or a[i] == "E" or a[i] == "I" or a[i] == "O" or a[i] == "U"):
            vowel = vowel + 1
        else:
            consonant = consonant + 1 

print("Vowel:", vowel)
print("Consonant:", consonant)