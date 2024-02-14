#Vowels
word = str(input("Enter a word: "))
vowels = ["a","e","i","o","u","A","E","I","O","U"]
def count_vowels(word,vowels):
    count = 0
    for i in range(len(word)):
        if word[i] in vowels:
            count = count + 1
    return count
print(count_vowels(word,vowels))