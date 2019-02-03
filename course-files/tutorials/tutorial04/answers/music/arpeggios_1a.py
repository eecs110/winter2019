import psonic

c_arpeggio = psonic.scale(psonic.C2, psonic.MAJOR, num_octaves=4)
print(c_arpeggio)
psonic.use_synth(psonic.PIANO)

previous_note = 0
for note in c_arpeggio:
    if note == previous_note:
        continue
    psonic.play(note)
    psonic.sleep(0.2)
    previous_note = note