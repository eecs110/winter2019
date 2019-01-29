import psonic
MARIO_NOTES = [
    76, 76, 76, 72, 76, 79, 67, 72, 67, 64, 69, 71,
    70, 69, 67, 76, 79, 81, 77, 79, 76, 72, 74, 71
]

# Challenge 1: use a *for* loop to PLAY all of the notes
# in the MARIO_NOTES list.
# for note in MARIO_NOTES:
#     psonic.play(note)
#     psonic.sleep(0.5)

# Challenge 2: when the song ends, play it again

while True:
    for note in MARIO_NOTES:
        psonic.play(note)
        psonic.sleep(0.2)
