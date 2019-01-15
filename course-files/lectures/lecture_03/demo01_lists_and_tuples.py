list_of_strings = ['freshman', 'sophmore', 'junior', 'senior']
list_of_ints = [12, 24, 36, 48, 60]
list_of_booleans = [True, True, False]
list_of_tuples = [(20, 20), (20, 40), (40, 40), (40, 20)]
list_of_mixed_data_types = ['a', 123, (40, 40), False]

# ## Example 1: Items of a list can be of any type
print('\n\nlists of different types...')
print(type(list_of_strings))
print(list_of_strings)
print(list_of_ints)
print(list_of_booleans)
print(list_of_tuples)
print(list_of_mixed_data_types)
# ## End Example 1


# ## Example 2: A list can be of any length
print('\n\ncalculating length of a list...')
print(len(list_of_strings))
print(len(list_of_ints))
print(len(list_of_booleans))
print(len(list_of_tuples))
print(len(list_of_mixed_data_types))
# ## End Example 2



# ## Example 3: You can access any list element through 0-based indexing
print('\n\naccessing...')
first_word = list_of_strings[0]
second_word = list_of_strings[1]
third_word = list_of_strings[2]
fourth_word = list_of_strings[3]
print(first_word)
print(second_word)
print(third_word)
print(fourth_word)
# ## End Example 3



# ## Example 4: You can slice lists
print('\n\nslicing...')
first_2_words = list_of_strings[0:2]
last_2_words = list_of_strings[-2:]
all_but_first_word = list_of_strings[1:]
all_but_last_word = list_of_strings[:-1]
print(first_2_words)
print(last_2_words)
print(all_but_first_word)
print(all_but_last_word)
# ## End Example 4



# ## Example 5: You can concatenate lists
print('\n\nconcatenating...')
stickem_example_1 = list_of_strings + list_of_ints
stickem_example_2 = list_of_strings + ['masters', 'phd']
print(stickem_example_1)
print(stickem_example_2)
# ## End Example 5




# ## Example 6: You can sort a list
print('\n\nsorting...')
list_of_strings.sort()  # sorts in place, alphabetically (mutates the list)
print(list_of_strings)  
list_of_strings.sort(reverse=True)  # reverse sorts in place, alphabetically
print(list_of_strings)  
# ## End Example 6




# ## Example 7: You can add data to a list:
print('\n\nappending...')
print(list_of_strings)  
list_of_strings.append('rhino')  # append adds data to the end of the list
print(list_of_strings)  
list_of_strings.append('giraffe')
print(list_of_strings)
# ## End Example 7



# ## Example 8: You can remove data from a list:
print('\n\nremoving...')
print(list_of_strings)  
list_of_strings.pop()  # pop removes data from the end of the list
print(list_of_strings)  
list_of_strings.pop()
print(list_of_strings)
# ## End Example 8



# ## Example 9: You can update data in a list:
print('\n\nupdating data in a list...')
list_of_strings = ['freshman', 'sophmore', 'junior', 'senior']
print(list_of_strings)
list_of_strings[0] = 'freshling'
print(list_of_strings)
# ## End Example 9


# ## Example 10: 
# Note that while lists are surrounded by square brackets, tuples are
# surrounded by parenthesis
tuple_of_strings = ('freshman', 'sophmore', 'junior', 'senior')
# parenthesis optional, but recommended
tuple_alternate_method_to_initialize = 'freshman', 'sophmore', 'junior', 'senior'
tuple_of_ints = (12, 24, 36, 48, 60)
tuple_of_booleans = (True, True, False)
tuple_of_tuples = ((20, 20), (20, 40), (40, 40), (40, 20))
tuple_of_mixed_data_types = ('a', 123, (40, 40), False)
print('\n\ntuples of different types...')
print(type(tuple_of_strings))
print(tuple_of_strings)
print(tuple_alternate_method_to_initialize)
print(tuple_of_ints)
print(tuple_of_booleans)
print(tuple_of_tuples)
print(tuple_of_mixed_data_types)
# ## End Example 10



# ## Example 11: You can't edit add to, remove from, or update data in a tuple
# uncomment to see the errors
# print('\n\nYou can't edit add to, remove from, or update data in a tuple...')
# print(tuple_of_strings)  
# tuple_of_strings.pop()  # results in an error
# tuple_of_strings.append('masters')  # results in an  error
# tuple_of_strings[0] = 'freshling'  # results in an error
# print(list_of_strings)
# # ## End Example 11
