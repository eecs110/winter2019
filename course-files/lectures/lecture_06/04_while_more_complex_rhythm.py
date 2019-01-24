import psonic
import random

# Challenges:  
# 1. How would I only play the DRUM_CYMBAL_CLOSED sound 
#    every fourth beat?
# 2. How would I play a symbol crash every 20th beat?
#    List of samples: https://docs.google.com/spreadsheets/d/1AlzpwvzsPou_gr532h8XKFWWlJY8l7QAfWFU2XXVgvI/edit#gid=0
# 3. How would I play a series of notes in addition to the rhythms?
while True:
    psonic.sample(psonic.DRUM_BASS_HARD, rate=random.randrange(1, 5))
    psonic.sample(psonic.DRUM_CYMBAL_CLOSED)
    psonic.sleep(0.125)