import psonic

speed = 1.5
counter = 0
while counter < 8:
    # fourth cycle
    if counter == 3:
        for i in range(8):
            psonic.sample(psonic.DRUM_TOM_HI_HARD, rate=(i*0.5+1))  # rate raises the pitch
            psonic.sleep(0.125 * speed)
        counter += 1
        continue

    # default:
    psonic.sample(psonic.DRUM_BASS_HARD, rate=1)
    psonic.sleep(.25 * speed)
    psonic.sample(psonic.DRUM_SNARE_HARD)
    psonic.sleep(.125 * speed)
    psonic.sample(psonic.DRUM_BASS_HARD, rate=1)
    psonic.sleep(.25 * speed)
    psonic.sample(psonic.DRUM_BASS_HARD, rate=1)
    psonic.sleep(.125 * speed)
    
    if counter == 7:
        # last beat:
        psonic.sample(psonic.DRUM_CYMBAL_OPEN)
    elif counter % 2 == 1:
        # alternate second cycle ending
        psonic.sample(psonic.DRUM_TOM_LO_HARD)
        psonic.sleep(0.125 * speed)
        psonic.sample(psonic.DRUM_TOM_MID_HARD)
        psonic.sleep(0.125 * speed)
    else:
        # default ending:
        psonic.sample(psonic.DRUM_SNARE_HARD)
        psonic.sleep(0.25 * speed)
        
    counter += 1