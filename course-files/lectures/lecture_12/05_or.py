def give_movie_discount(is_student, is_senior, is_child):
    return is_student or is_senior or is_child


print(give_movie_discount(True, True, True))
print(give_movie_discount(True, False, False))
print(give_movie_discount(True, False, True))
print(give_movie_discount(True, True, False))
print(give_movie_discount(False, True, True))
print(give_movie_discount(False, False, True))
print(give_movie_discount(False, True, False))
print(give_movie_discount(False, False, False))