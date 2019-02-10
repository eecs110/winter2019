import psonic

def play_riff_1(speed=2):
    print('playing riff 1...')
    psonic.sample(psonic.DRUM_BASS_HARD, rate=1)
    psonic.sleep(.25 * speed)
    psonic.sample(psonic.DRUM_SNARE_HARD)
    psonic.sleep(.125 * speed)
    psonic.sample(psonic.DRUM_BASS_HARD, rate=1)
    psonic.sleep(.25 * speed)
    psonic.sample(psonic.DRUM_BASS_HARD, rate=1)
    psonic.sleep(.125 * speed)
    psonic.sample(psonic.DRUM_SNARE_HARD)
    psonic.sleep(0.24 * speed) # make the last sleep a little shorter

def play_riff_2(speed=2):
    print('playing riff 2...')
    psonic.sample(psonic.AMBI_LUNAR_LAND)
    #psonic.sample(psonic.AMBI_DRONE)
    psonic.sleep(3.99 * speed) # make the last sleep a little shorter

def play_riff_3(speed=2):
    print('playing riff 3...')
    psonic.sample(psonic.DRUM_TOM_HI_SOFT, rate=1)
    psonic.sleep(.25 * speed)
    psonic.sample(psonic.DRUM_TOM_HI_SOFT)
    psonic.sleep(.125 * speed)
    psonic.sample(psonic.DRUM_TOM_HI_SOFT, rate=1)
    psonic.sleep(.25 * speed)
    psonic.sample(psonic.DRUM_TOM_HI_SOFT, rate=1)
    psonic.sleep(.125 * speed)
    psonic.sample(psonic.DRUM_TOM_HI_SOFT)
    psonic.sleep(0.24 * speed) # make the last sleep a little shorter

def play_base_beat(speed=2):
    # print base beat
    print('base:', 4 * 0.25)
    for i in range(4):
        psonic.sample(psonic.DRUM_CYMBAL_PEDAL)
        psonic.sleep(speed * 0.25)