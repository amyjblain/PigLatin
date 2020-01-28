def find_vowel(word):
    # This is from 0 to the length of the word
    for i in range(len(word)):
       if word[i] in VOWELS: 
         return i
    # Return an error value if there are not any (which solves another problem too!)
    return -1

VOWELS = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")

statement = input("Please enter a word: ")

words =  statement.split()
count = 0

for word in words:
  vowel = find_vowel(word)
  # No vowels found
  if(vowel == -1):
    print(word)
  # A vowel is the first letter
  elif(vowel == 0):
    print(word + "ay")
  else:
    # See how I split from the position of the vowel?
    print (word[vowel:] + word[:vowel] + "ay")
