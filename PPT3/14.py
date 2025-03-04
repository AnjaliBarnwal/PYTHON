14. Create an acronym or an abbreviation for the name 'Python For Everyone'.
def create_acronym(phrase):
words = phrase.split()
acronym = ''.join([word[0].upper() for word in words])
return acronym

phrase = "Python For Everyone"
acronym = create_acronym(phrase)

print("Acronym for '{}' is: {}".format(phrase, acronym))

