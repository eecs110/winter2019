import random
import psonic

# Challenge: write a loop that plays 128 beats, using the 
# psonic.DRUM_BASS_HARD sample, that are each at a different
# pitch (from 1 to 10). Note that pitch is controlled by the "rate" keyword argument.
while True:
    r = random.randrange(1,10)
    psonic.sample(psonic.DRUM_BASS_HARD, rate=r)
    psonic.sleep(0.125)