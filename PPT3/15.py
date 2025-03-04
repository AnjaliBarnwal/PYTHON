15. Find the position of the first occurrence of the word 'because' in the following sentence: 'You
cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
word = "because"

position = sentence.find(word)

if position != -1:
print(f"The first occurrence of the word '{word}' is at position: {position}")
else:
print(f"The word '{word}' is not found in the sentence.")

