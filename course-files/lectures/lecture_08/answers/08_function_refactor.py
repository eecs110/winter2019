# refactor this code so that it uses a function
# then use that function to play any song (not just HAPPY_BIRTHDAY)
# coming soon: better ways of representing songs to account for
# rhythm -- not just notes!
import psonic
HAPPY_BIRTHDAY = [
    48, 48, 50, 48, 53, 52, 48, 48, 50, 48, 55, 53,
    48, 48, 60, 57, 53, 52, 50, 58, 58, 57, 53, 55, 53
]

SUPER_MARIO_NOTES = [
    76, 76, 76, 72, 76, 79, 67, 72, 67, 64, 69, 71,
    70, 69, 67, 76, 79, 81, 77, 79, 76, 72, 74, 71,
    79, 78, 77, 75, 76, 68, 69, 72, 69, 72, 74, 79,
    78, 77, 75, 76, 84, 79, 78, 77, 75, 76, 68, 69,
    72, 69, 72, 74, 75, 74, 72, 72, 74, 76, 72, 69,
    67, 72, 74, 76, 72, 74, 76, 72, 69, 67, 76, 72,
    76, 79, 67, 76, 72, 67, 68, 69, 77, 69, 71, 81,
    79, 77, 76, 72, 69, 67, 76, 72, 67, 68, 69, 77,
    69, 71, 77, 76, 74, 72
]

def play_song(notes, speed):
    psonic.use_synth(psonic.PIANO)
    for note in notes:
        psonic.play(note)
        psonic.sleep(speed)

play_song(HAPPY_BIRTHDAY, 0.1)
play_song(SUPER_MARIO_NOTES, 0.1)