import random
import psonic
play = psonic.play      # shortcut (aliasing for less typing)
sleep = psonic.sleep    # shortcut (aliasing for less typing)
sample = psonic.sample


def make_song():
    # do something interesting here with sound:
    psonic.use_synth(psonic.PIANO)
    sample(psonic.DRUM_BASS_HARD)
    play(60)
    # ...