import psonic
MARIO_NOTES = [
    76, 76, 76, 72, 76, 79, 67, 72, 67, 64, 69, 71,
    70, 69, 67, 76, 79, 81, 77, 79, 76, 72, 74, 71
]

# Challenge: skip over all of the MIDI notes that equal 67
for note in MARIO_NOTES:
    if note == 67:
        print('skipping...', note)
        continue
    psonic.play(note)
    psonic.sleep(0.3)
