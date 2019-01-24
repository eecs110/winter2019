import psonic

## PART 1:
while True:
    psonic.sample(psonic.DRUM_BASS_HARD)
    psonic.sleep(0.2)
    psonic.sample(psonic.DRUM_CYMBAL_PEDAL)
    psonic.sleep(0.2)
## END PART 1:


## PART 2:
# counter = 0
# while counter < 10:
#     psonic.sample(psonic.DRUM_BASS_HARD)
#     psonic.sleep(0.2)
#     psonic.sample(psonic.DRUM_CYMBAL_PEDAL)
#     psonic.sleep(0.2)
#     counter += 1
## END PART 2