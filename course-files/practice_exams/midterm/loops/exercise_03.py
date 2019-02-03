import psonic

for i in range(12):
    if i in [3, 7, 11]:
        psonic.sample(psonic.DRUM_CYMBAL_PEDAL)
        psonic.sleep(0.2)
    else:
        psonic.sample(psonic.DRUM_BASS_HARD)
        psonic.sleep(0.2)


# # Alternate (there are many valid solutions)
# for i in range(1, 13):
#     if i % 4 == 0:
#         psonic.sample(psonic.DRUM_CYMBAL_PEDAL)
#         psonic.sleep(0.2)
#     else:
#         psonic.sample(psonic.DRUM_BASS_HARD)
#         psonic.sleep(0.2)