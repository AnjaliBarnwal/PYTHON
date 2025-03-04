16.Slice out the phrase 'because because because' in the following sentence: 'You cannot end a
sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
	
# Slice out the phrase 'because because because'
start_index = sentence.find("because because because")
end_index = start_index + len("because because because")

sliced_phrase = sentence[start_index:end_index]

print("Sliced phrase:", sliced_phrase)
