import psonic

c_arpeggio = psonic.scale(psonic.C2, psonic.MAJOR, num_octaves=4)
print(c_arpeggio)
psonic.use_synth(psonic.PIANO)

previous_note = 1000000
start = len(c_arpeggio) - 1
end = -1  # -1 b/c range function does not include the endpoint
for i in range(start, end, -1):
    print(i)    # for debugging
    note = c_arpeggio[i]
    if note == previous_note:
        continue
    psonic.play(note)
    psonic.sleep(0.2)
    previous_note = note