# write a function called sentence that takes a sentence
# and a word as positional arguments and returns a boolean
# value indicating whether or not the word is in the sentence.
# Ensure that your function is case in-sensitive. It does not
# have to match on a whole word -- just part of a word.
# Below, I show how I would call your function and what it would 
# output to the screen.
 
def is_word_in_sentence(sentence, char_string):
    if char_string.lower() in sentence.lower():
        return True
    return False

def is_word_in_sentence_1(sentence, char_string):
    if sentence.lower().find(char_string.lower()) != -1:
        return True
    return False

print('\nMethod 1...')
print(is_word_in_sentence('Here is a fox', 'Fox'))
print(is_word_in_sentence('Here is a fox', 'bird'))
print(is_word_in_sentence('Here is a fox', 'Ox'))
print('\nMethod 2...')
print(is_word_in_sentence_1('Here is a fox', 'Fox'))
print(is_word_in_sentence_1('Here is a fox', 'bird'))
print(is_word_in_sentence_1('Here is a fox', 'Ox'))

