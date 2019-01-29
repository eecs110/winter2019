import psonic
MARIO_NOTES = [
    76, 76, 76, 72, 76, 79, 67, 72, 67, 64, 69, 71,
    70, 69, 67, 76, 79, 81, 77, 79, 76, 72, 74, 71
]

# Challenge: play every third note in the MARIO_NOTES list:

# Solution 1 (of many), using modulus:
counter = 0
for note in MARIO_NOTES:
    if counter % 3 == 0:
        psonic.play(note)
        psonic.sleep(.3)
    counter += 1
# end Solution 1

# Solution 2 (of many), using range function:
for i in range(0, len(MARIO_NOTES), 3):  # start at 0, end at len(MARIO_NOTES), increment by 3
    psonic.play(MARIO_NOTES[i])
    psonic.sleep(.3)
# end Solution 1
