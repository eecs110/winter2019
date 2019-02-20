def in_between(num, low, high):
    return high > num and num > low

print(in_between(90, 20, 70))
print(in_between(30, 20, 70))