import psonic
import random

counter = 0
while True:
    # note: the "rate" parameter adjusts pitch
    # you can read about it here:
    # 
    psonic.sample(psonic.DRUM_BASS_HARD, rate=random.randrange(1, 5))
    
    # Cymbal hit every third time:
    if counter % 3 == 0:
        psonic.sample(psonic.DRUM_CYMBAL_PEDAL)

    psonic.sleep(0.125)
    counter += 1