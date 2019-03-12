# write a function called bedazzle that takes a list of names as
# an argument and prints an asterisk-delimited row of names.
# Below, I show how I would call your function and what it would 
# output to the screen.

def bedazzle(names):
    print(' * '.join(names))

bedazzle(['Curly', 'Moe', 'Larry'])
bedazzle(['Ana', 'Beatrice', 'Carlos'])
bedazzle(['June', 'Reuben', 'Shu', 'Yessica'])

# Curly * Moe * Larry
# Ana * Beatrice * Carlos
# June * Reuben * Shu * Yessica
