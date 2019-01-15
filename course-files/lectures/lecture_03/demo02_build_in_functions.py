# ## Example 1: Required (positional) parameters:

# pow()     # this will throw an error
# pow(3)    # this will also throw an error
result1 = pow(3, 2)   # order matters
result2 = pow(2, 3)   # order matters
print(result1)
print(result2)
# ## End Example 1



# ## Example 2: Required (positional) and optional (keyword) parameters:
# enumerate(iterable, start=0)
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(sorted(seasons))
print(sorted(seasons, reverse=True))


# ## Example 3: print:
# Take a look at the documentation:
# https://docs.python.org/3/library/functions.html#print
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False):
#   (a) the *objects parameter notation means that 0 or more arguments can
#   be passed into print.
#   (b) sep=' ', end='\n', file=sys.stdout, and flush=False are optional
#   keyword arguments:
print()  # doesn't throw an error, but doesn't do anything
print(result1, result2)

demofile = open("demofile.txt", "w")
print('I\'m printing to a file', file=demofile)
# use a pipe separator (|) instead of a space
print('Here are my results:', result1, result2, file=demofile, sep=' | ')
demofile.close()
# ## End Example 3