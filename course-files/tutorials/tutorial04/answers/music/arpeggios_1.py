import psonic

c_arpeggio = psonic.scale(psonic.C2, psonic.MAJOR, num_octaves=4)
print(c_arpeggio)
psonic.use_synth(psonic.PIANO)

for note in c_arpeggio:
    psonic.play(note)
    psonic.sleep(0.2)