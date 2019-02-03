import psonic

while True:
    psonic.sample(psonic.DRUM_BASS_HARD)
    psonic.sleep(0.2)
    psonic.sample(psonic.DRUM_CYMBAL_PEDAL)
    psonic.sleep(0.2)
