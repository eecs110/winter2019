import psonic

c_arpeggio = psonic.scale(psonic.C2, psonic.MAJOR, num_octaves=4)
print(c_arpeggio)
psonic.use_synth(psonic.PIANO)

# play ascending arpeggio:
counter = 0
for note in c_arpeggio:
    if counter % 8 in [0, 2, 4]:
        psonic.play(note)
        psonic.sleep(0.2)
    counter += 1

# play top note:
psonic.play(c_arpeggio[-1])
psonic.sleep(0.2)


