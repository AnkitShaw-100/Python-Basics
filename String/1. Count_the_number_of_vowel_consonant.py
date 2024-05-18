#count_the_number_of_vowel_ consonant
n = input("Enter a string : ")
l = len(n)
v = 0 
c = 0
for i in range (0,l):
    if n[i] == "A" or n[i] == "E" or n[i] == "I" or n[i] == "O" or n[i] == "U" or n[i] == "a" or n[i] == "e" or n[i] == "i" or n[i] == "o" or n[i] == "u" :
        v += 1
    else :
        c += 1

print(f"The number of Vowels found in a word {v}")
print(f"The number of Consonants found in a word {c}")
