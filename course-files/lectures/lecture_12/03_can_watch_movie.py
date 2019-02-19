person_13 = { 'age': 13, 'with_parent': True }
person_12 = { 'age': 12, 'with_parent': False }
person_27 = { 'age': 27, 'with_parent': False }

movie_r = { 'title': 'A Star is Born', 'rating': 'R' }
movie_pg = { 'title': 'The LEGO Movie 2', 'rating': 'PG' }

def can_watch_movie(age, with_parent, rating):
    if age > 17:
        return True
    if rating != 'R':
        return True
    return with_parent

def can_watch_movie_alt(age, with_parent, rating):
    return age > 17 or rating != 'R' or with_parent

print(can_watch_movie_alt(13, True, 'R'))
print(can_watch_movie_alt(13, False, 'R'))
print(can_watch_movie_alt(13, True, 'PG'))
print(can_watch_movie_alt(13, False, 'PG'))
print(can_watch_movie_alt(18, True, 'R'))
print(can_watch_movie_alt(18, False, 'R'))
print(can_watch_movie_alt(18, True, 'PG'))
print(can_watch_movie_alt(18, False, 'PG'))


# print(can_watch_movie(13, True, 'R'))
# print(can_watch_movie(13, False, 'R'))
# print(can_watch_movie(13, True, 'PG'))
# print(can_watch_movie(13, False, 'PG'))
# print(can_watch_movie(18, True, 'R'))
# print(can_watch_movie(18, False, 'R'))
# print(can_watch_movie(18, True, 'PG'))
# print(can_watch_movie(18, False, 'PG'))