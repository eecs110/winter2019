import psonic

MARIO_NOTES = [
    76, 76, 76, 72, 76, 79, 67, 72, 67, 64, 69, 71,
    70, 69, 67, 76, 79, 81, 77, 79, 76, 72, 74, 71
]
note_number = 0

while note_number < len(MARIO_NOTES):
    psonic.use_synth(psonic.PIANO)
    print(note_number, '/', len(MARIO_NOTES), 'MIDI NOTE:', MARIO_NOTES[note_number])
    
    # this just pauses the execution until the 
    # user presses enter (which resumes the loop)
    input('Press enter to play next note') 
    psonic.play(MARIO_NOTES[note_number])
    note_number += 1

print('End loop. No more notes')