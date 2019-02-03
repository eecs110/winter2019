import psonic

for i in range(5):
    psonic.sample(psonic.DRUM_BASS_HARD)
    psonic.sleep(0.2)
    psonic.sample(psonic.DRUM_CYMBAL_PEDAL)
    psonic.sleep(0.2)


# # Alternate solution
# counter = 0
# while counter < 5:
#     psonic.sample(psonic.DRUM_BASS_HARD)
#     psonic.sleep(0.2)
#     psonic.sample(psonic.DRUM_CYMBAL_PEDAL)
#     psonic.sleep(0.2)
#     counter += 1
