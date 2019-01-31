import psonic

speed = 2

while True:
    psonic.sample(psonic.DRUM_BASS_HARD, rate=1)
    psonic.sleep(.25 * speed)
    psonic.sample(psonic.DRUM_SNARE_HARD)
    psonic.sleep(.125 * speed)
    psonic.sample(psonic.DRUM_BASS_HARD, rate=1)
    psonic.sleep(.25 * speed)
    psonic.sample(psonic.DRUM_BASS_HARD, rate=1)
    psonic.sleep(.125 * speed)
    psonic.sample(psonic.DRUM_SNARE_HARD)
    psonic.sleep(0.25 * speed)