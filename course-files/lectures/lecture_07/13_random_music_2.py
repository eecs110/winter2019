import random
import psonic

# Challenge: write a loop that plays 128 beats, using the 
# psonic.DRUM_BASS_HARD sample, that are each at a different
# pitch (from 1 to 10). Note that pitch is controlled by the "rate" keyword argument.
psonic.sample(psonic.DRUM_BASS_HARD, rate=1)
psonic.sleep(0.125)
psonic.sample(psonic.DRUM_BASS_HARD, rate=5)
psonic.sleep(0.125)
psonic.sample(psonic.DRUM_BASS_HARD, rate=8)
psonic.sleep(0.125)