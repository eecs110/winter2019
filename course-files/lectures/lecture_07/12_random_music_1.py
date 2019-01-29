import psonic
import random

e = psonic.chord(psonic.E3, psonic.MINOR)
print(e)

# Challenge: Write a  loop that randomly plays a note from the 
# e minor cord, for either 0.25, or 0.5 length of time
# after it plays 30 notes it should stop
psonic.use_synth(psonic.PROPHET)
psonic.play(e[0], release=0.6)
psonic.sleep(0.5)