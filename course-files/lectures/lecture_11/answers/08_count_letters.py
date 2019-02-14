word = 'supercalifragilisticexpialidocious'
letter_counts = {}
for letter in word:
    if letter_counts.get(letter) is None:
        letter_counts[letter] = 0
    letter_counts[letter] += 1

for key in letter_counts:
    print(key + ':', letter_counts[key])
