import psonic
MARIO_NOTES = [
    76, 76, 76, 72, 76, 79, 67, 72, 67, 64, 69, 71,
    70, 69, 67, 76, 79, 81, 77, 79, 76, 72, 74, 71
]

# Challenge: using a for loop, break out of the loop if you
# get to a MIDI note that equals 67

for note in MARIO_NOTES:
    print(note)
    psonic.play(note)
    psonic.sleep(0.3)
    if note == 67:
        break
