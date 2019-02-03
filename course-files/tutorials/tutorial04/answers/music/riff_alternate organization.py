import psonic

'''
NOTE: This example implements the same logic, but uses functions to make code more
readable and easier to follow.
'''


def fourth_cycle(speed):
    print('fourth cycle...')
    for i in range(8):
        psonic.sample(psonic.DRUM_TOM_HI_HARD, rate=(i*0.5+1))  # rate raises the pitch
        psonic.sleep(0.125 * speed)

def last_beat_final(speed):
    print('final beat...')
    psonic.sample(psonic.DRUM_CYMBAL_OPEN)

def last_beat_every_other(speed):
    print('last beat every other...')
    # alternate second cycle ending
    psonic.sample(psonic.DRUM_TOM_LO_HARD)
    psonic.sleep(0.125 * speed)
    psonic.sample(psonic.DRUM_TOM_MID_HARD)
    psonic.sleep(0.125 * speed)

def last_beat_default(speed):
    print('last beat default...')
    psonic.sample(psonic.DRUM_SNARE_HARD)
    psonic.sleep(0.25 * speed)

def main_rhythm(speed):
    print('main rhythm...')
    psonic.sample(psonic.DRUM_BASS_HARD, rate=1)
    psonic.sleep(.25 * speed)
    psonic.sample(psonic.DRUM_SNARE_HARD)
    psonic.sleep(.125 * speed)
    psonic.sample(psonic.DRUM_BASS_HARD, rate=1)
    psonic.sleep(.25 * speed)
    psonic.sample(psonic.DRUM_BASS_HARD, rate=1)
    psonic.sleep(.125 * speed)

speed = 1.5
counter = 0       
while counter < 8:
    print('counter:', counter)
    if counter == 3:
        fourth_cycle(speed)
    else:
        main_rhythm(speed)
        if counter == 7:
            last_beat_final(speed)
        elif counter % 2 == 1:
            last_beat_every_other(speed)
        else:
            last_beat_default(speed)

    # don't forget to increment the counter:
    counter += 1