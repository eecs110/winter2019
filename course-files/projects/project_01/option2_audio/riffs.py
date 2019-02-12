import psonic

# These are just some simple riffs (placeholders)
# replace these with your own!

def controller_riff(tempo=1):
    psonic.sample(psonic.DRUM_BASS_SOFT)
    psonic.sleep(tempo)

def riff_1(tempo=1):
    for i in range(3):
        psonic.sample(psonic.DRUM_SNARE_SOFT)
        psonic.sleep(tempo * 0.5)
    psonic.sample(psonic.DRUM_SNARE_SOFT)

def riff_2(tempo=1):
    psonic.sample(psonic.DRUM_CYMBAL_OPEN)
    psonic.sleep(tempo * 0.99)

def riff_3(tempo=1):
    for i in range(3):
        psonic.sample(psonic.DRUM_SNARE_SOFT)
        psonic.sleep(tempo * .25) 
    psonic.sample(psonic.DRUM_SNARE_SOFT)

def riff_4(tempo=2):
    psonic.sample(psonic.DRUM_BASS_HARD, rate=1)
    psonic.sleep(.25 * tempo)
    psonic.sample(psonic.DRUM_SNARE_HARD)
    psonic.sleep(.125 * tempo)
    psonic.sample(psonic.DRUM_BASS_HARD, rate=1)
    psonic.sleep(.25 * tempo)
    psonic.sample(psonic.DRUM_BASS_HARD, rate=1)
    psonic.sleep(.125 * tempo)
    psonic.sample(psonic.DRUM_SNARE_HARD)
    psonic.sleep(0.24 * tempo) # make the last sleep a little shorter

def riff_5(tempo=2):
    psonic.sample(psonic.AMBI_LUNAR_LAND)
    #psonic.sample(psonic.AMBI_DRONE)
    psonic.sleep(3.99 * tempo) # make the last sleep a little shorter

def riff_6(tempo=1):
    psonic.sample(psonic.DRUM_TOM_HI_SOFT, rate=1)
    psonic.sleep(.25 * tempo)
    psonic.sample(psonic.DRUM_TOM_HI_SOFT)
    psonic.sleep(.125 * tempo)
    psonic.sample(psonic.DRUM_TOM_HI_SOFT, rate=1)
    psonic.sleep(.25 * tempo)
    psonic.sample(psonic.DRUM_TOM_HI_SOFT, rate=1)
    psonic.sleep(.125 * tempo)
    psonic.sample(psonic.DRUM_TOM_HI_SOFT)
    psonic.sleep(0.24 * tempo) # make the last sleep a little shorter

def riff_7(tempo=1):
    for i in range(4):
        psonic.sample(psonic.DRUM_CYMBAL_PEDAL)
        psonic.sleep(tempo * 0.25)

def riff_8(tempo):
    for i in range(6):
        psonic.sample(psonic.DRUM_HEAVY_KICK, rate=0.8)
        psonic.sleep(tempo * 0.5)
    
    for i in range(7):
        psonic.sample(psonic.DRUM_HEAVY_KICK, rate=0.8)
        psonic.sleep(tempo * .125)
    psonic.sample(psonic.DRUM_HEAVY_KICK, rate=0.8)

def play_harley_sound(tempo=1):
    # play any wav file that you choose (just save it in the same directory)
    # you can download them from the internet (e.g. https://freewavesamples.com/)
    # or make your own:
    import sys
    import os
    dir_path = os.path.dirname(sys.argv[0])
    sound_file = os.path.join(dir_path, 'sounds/harley_davidson.wav')
    file_path = os.path.abspath(sound_file)
    # start and finish anywhere between 0 and 1:
    command = 'sample "{0}", start: {1}, finish: {2}'.format(
        file_path, 0.4, 0.42)
    psonic.run(command)