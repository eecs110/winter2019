# ## Example 1:  If Statement
# year = 2019  # set year to 2020 and see what happens:
# print('February 26')
# print('February 27')
# print('February 28')
# if year % 4 == 0:
#     print('February 29')
# print('March 1')

# ## for debugging:
# # print(2019 % 4)
# # print(2020 % 4)
# ## End Example 1




# ## Example 2: If / Else Statement
# def even_or_odd(num):
#     if num % 2 == 0:
#         return 'even'
#     else:
#         return 'odd'
# print('5:', even_or_odd(5))
# print('10:', even_or_odd(10))
# print('11:', even_or_odd(11))
# print('18:', even_or_odd(18))
# ## End Example 2




# ## Example 3:  If / Elif / Else Statement
# def give_grade(score):
#     if score >= 90:
#         return 'A'
#     elif score >= 80:
#         return 'B'
#     elif score >= 70:
#         return 'C'
#     elif score >= 60:
#         return 'D'
#     else:
#         return 'F'
# print('65:', give_grade(65))
# print('99:', give_grade(99))
# print('84:', give_grade(84))
# print('76:', give_grade(76))
# print('20:', give_grade(20))
# ## Visualize this execution (a visual representation): https://goo.gl/RPqCLc
# ## End Example 3




# ## Example 4: If / Elif / Else Statement (just another example)
# def move_avatar(direction, units):
#     if direction == 'up':
#         print('subtract', units, 'from y-position')
#     elif direction == 'down':
#         print('add', units, 'to y-position')
#     elif direction == 'left':
#         print('subtract', units, 'to x-position')
#     elif direction == 'right':
#         print('add', units, 'to x-position')

# move_avatar('up', 10)
# move_avatar('down', 15)
# move_avatar('left', 2)
# move_avatar('right', 3)
# # ## End Example 4






# ## Example 5: If / Elif / Else Statement (yet another example)
# def change_song_speed(direction, units):
#     if direction == 'up':
#         # make the song faster by decreasing the wait time between notes:
#         print('make the sleep interval shorter by', units, 'milliseconds')
#     elif direction == 'down':
#         # make the song slower by increasing the wait time between notes:
#         print('make the sleep interval longer by', units, 'milliseconds')
#     else:
#         print(direction, 'is not a valid direction. Please use "up" or "down"')

# change_song_speed('up', 10)
# change_song_speed('down', 15)
# # ## End Example 5