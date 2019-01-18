# psonic documentation: # https://github.com/gkvoelkl/python-sonic
# MIDI Reference: http://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies
# play function reference: https://docs.google.com/spreadsheets/d/1AlzpwvzsPou_gr532h8XKFWWlJY8l7QAfWFU2XXVgvI/edit#gid=860514818
# TODO: Ensure that your Sonic Pi is running before you run this Python file


import random
import psonic
play = psonic.play      # shortcut (aliasing for less typing)
sleep = psonic.sleep    # shortcut (aliasing for less typing)
sample = psonic.sample

SUPER_MARIO_NOTES = [
    76, 76, 76, 72, 76, 79, 67, 72, 67, 64, 69, 71,
    70, 69, 67, 76, 79, 81, 77, 79, 76, 72, 74, 71,
    79, 78, 77, 75, 76, 68, 69, 72, 69, 72, 74, 79,
    78, 77, 75, 76, 84, 79, 78, 77, 75, 76, 68, 69,
    72, 69, 72, 74, 75, 74, 72, 72, 74, 76, 72, 69,
    67, 72, 74, 76, 72, 74, 76, 72, 69, 67, 76, 72,
    76, 79, 67, 76, 72, 67, 68, 69, 77, 69, 71, 81,
    79, 77, 76, 72, 69, 67, 76, 72, 67, 68, 69, 77,
    69, 71, 77, 76, 74, 72
]
SUPER_MARIO_NOTES_FIRST_24 = SUPER_MARIO_NOTES[0:24]

HAPPY_BIRTHDAY = [
    48, 48, 50, 48, 53, 52, 48, 48, 50, 48, 55, 53,
    48, 48, 60, 57, 53, 52, 50, 58, 58, 57, 53, 55, 53
]

def play_happy_birthday():
    psonic.use_synth(psonic.PIANO)
    play(HAPPY_BIRTHDAY[0])
    sleep(0.25)
    play(HAPPY_BIRTHDAY[1])
    sleep(0.25)
    play(HAPPY_BIRTHDAY[2])
    sleep(0.25)
    play(HAPPY_BIRTHDAY[3])
    sleep(0.25)
    play(HAPPY_BIRTHDAY[4])
    sleep(0.25)
    play(HAPPY_BIRTHDAY[5])
    sleep(0.25)
    play(HAPPY_BIRTHDAY[6])
    sleep(0.25)
    play(HAPPY_BIRTHDAY[7])
    sleep(0.25)
    play(HAPPY_BIRTHDAY[8])
    sleep(0.25)
    play(HAPPY_BIRTHDAY[9])
    sleep(0.25)
    play(HAPPY_BIRTHDAY[10])
    sleep(0.25)
    play(HAPPY_BIRTHDAY[11])
    sleep(0.25)
    play(HAPPY_BIRTHDAY[12])
    sleep(0.25)
    play(HAPPY_BIRTHDAY[13])
    sleep(0.25)
    play(HAPPY_BIRTHDAY[14])
    sleep(0.25)
    play(HAPPY_BIRTHDAY[15])
    sleep(0.25)
    play(HAPPY_BIRTHDAY[16])
    sleep(0.25)
    play(HAPPY_BIRTHDAY[17])
    sleep(0.25)
    play(HAPPY_BIRTHDAY[18])
    sleep(0.25)
    play(HAPPY_BIRTHDAY[19])
    sleep(0.25)
    play(HAPPY_BIRTHDAY[20])
    sleep(0.25)
    play(HAPPY_BIRTHDAY[21])
    sleep(0.25)
    play(HAPPY_BIRTHDAY[22])
    sleep(0.25)
    play(HAPPY_BIRTHDAY[23])
    sleep(0.25)
    play(HAPPY_BIRTHDAY[24])
    sleep(0.25)


def get_play_function_signature():
    import inspect
    print('The optional and required parameters for the "play" function are:',
          inspect.signature(psonic.play))


def play_c_scale():
    # MIDI Notes available here:
    # https://docs.google.com/spreadsheets/d/1AlzpwvzsPou_gr532h8XKFWWlJY8l7QAfWFU2XXVgvI/edit#gid=0
    psonic.use_synth(psonic.PIANO)
    play(48)  # these are MIDI note numbers
    sleep(0.5)
    play(50)
    sleep(0.5)
    play(52)
    sleep(0.5)
    play(53)
    sleep(0.5)
    play(55)
    sleep(0.5)
    play(57)
    sleep(0.5)
    play(59)
    sleep(0.5)
    play(60)
    sleep(0.5)
    play(59)
    sleep(0.5)
    play(57)
    sleep(0.5)
    play(55)
    sleep(0.5)
    play(53)
    sleep(0.5)
    play(52)
    sleep(0.5)
    play(50)
    sleep(0.5)
    play(48)

    # play arpeggio (w/o sleep functions, notes play simultaneously):
    sleep(1)
    play(48)
    play(52)
    play(55)
    play(60)
    sleep(1)


def demo_play_sustain():
    # controls how long the note lasts
    psonic.use_synth(psonic.SUBPULSE)  # select a synthesizer:
    play(48)  # default
    sleep(1)
    play(50, sustain=1)  # a little longer
    sleep(1)
    play(52, sustain=2)  # a little longer
    sleep(1)
    play(53, sustain=4.5)  # even longer
    sleep(1)


def demo_play_volume_adjust():
    # controls how loud the note lasts
    psonic.use_synth(psonic.SUBPULSE)
    play(48)  # default
    sleep(1)
    play(50, sustain_level=0.2)  # soft
    sleep(1)
    play(52, sustain_level=0.4)  # a little louder
    sleep(1)
    play(53, sustain_level=0.6)  # even louder
    sleep(1)
    play(55, sustain_level=1.6)  # even louder
    sleep(1)


def demo_play_fadein():
    # controls the fade-in time
    psonic.use_synth(psonic.SUBPULSE)
    play(48)  # default
    sleep(1)
    play(50, attack=0.5)  # fade in
    sleep(1)
    play(52, attack=1)  # longer fade in
    sleep(1)
    play(53, attack=2)  # even longer fade in
    sleep(1)


def demo_play_fadeout():
    # controls the time it takes to fade-out time
    psonic.use_synth(psonic.SUBPULSE)
    play(48)  # default
    sleep(1)
    play(50, release=0.1)  # fade out
    sleep(1)
    play(52, release=0.2)  # longer fade in
    sleep(1)
    play(53, release=0.6)  # even longer fade in
    sleep(1)


def demo_play_combo():
    # demonstration of the optional parameters available using
    # the play function. To read about these, take a look at the
    # spreadsheet of documentation that I made for you:
    # https://docs.google.com/spreadsheets/d/1AlzpwvzsPou_gr532h8XKFWWlJY8l7QAfWFU2XXVgvI/edit#gid=860514818
    psonic.use_synth(psonic.SUBPULSE)
    play(48, amp=0.2, sustain=2, attack=1, decay=1)


def play_super_mario():
    # play the first 24 notes of Super Mario Brothers theme music
    # audio demo: https://vimeo.com/85685770
    psonic.use_synth(psonic.PIANO)
    play(SUPER_MARIO_NOTES_FIRST_24[0])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[1])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[2])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[3])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[4])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[5])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[6])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[7])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[8])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[9])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[10])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[11])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[12])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[13])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[14])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[15])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[16])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[17])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[18])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[19])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[20])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[21])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[22])
    sleep(0.1)
    play(SUPER_MARIO_NOTES_FIRST_24[23])
    sleep(0.1)


def play_c_scale_builtin():
    # so you don't have to build your scales manually
    scale_C2 = psonic.scale(psonic.C2, psonic.MAJOR)
    scale_C3 = psonic.scale(psonic.C3, psonic.MAJOR)
    scale_C4 = psonic.scale(psonic.C4, psonic.MAJOR)
    print('C2 Scale:', scale_C2)
    print('C3 Scale:', scale_C3)
    print('C4 Scale:', scale_C4)

    # listening demo:
    psonic.use_synth(psonic.PIANO)
    play(scale_C3[0])
    sleep(0.5)
    play(scale_C3[1])
    sleep(0.5)
    play(scale_C3[2])
    sleep(0.5)
    play(scale_C3[3])
    sleep(0.5)
    play(scale_C3[4])
    sleep(0.5)
    play(scale_C3[5])
    sleep(0.5)
    play(scale_C3[6])
    sleep(0.5)
    play(scale_C3[7])


##########################
## Working with Samples ##
##########################
# For a list of all of the samples:
# https://docs.google.com/spreadsheets/d/1AlzpwvzsPou_gr532h8XKFWWlJY8l7QAfWFU2XXVgvI/edit#gid=195217270

def get_sample_function_signature():
    import inspect
    print('The optional and required parameters for the "sample" function are:',
          inspect.signature(psonic.play))


def drum_4_beats():
    # Note: rate controls how far the sample is stretched
    sample(psonic.DRUM_BASS_HARD, rate=1)  # default rate
    sleep(0.125)
    sample(psonic.DRUM_BASS_HARD, rate=5)
    sleep(0.125)
    sample(psonic.DRUM_BASS_HARD, rate=10)
    sleep(0.125)
    sample(psonic.DRUM_BASS_HARD, rate=15)
    sleep(0.125)


def drum_3_random_beats():
    sample(psonic.DRUM_BASS_HARD, rate=random.randrange(1, 50))
    sleep(0.125)
    sample(psonic.DRUM_BASS_HARD, rate=random.randrange(1, 50))
    sleep(0.125)
    sample(psonic.DRUM_BASS_HARD, rate=random.randrange(1, 50))
    sleep(0.125)


def drum_continuous_random_beats():
    import random
    while True:
        sample(psonic.DRUM_BASS_HARD, rate=random.randrange(1, 50))
        sleep(0.125)
        # Note: type Control C to cancel.


def drum_continuous_low_beats():
    while True:
        sample(psonic.DRUM_BASS_HARD, rate=random.randrange(1, 5))
        sleep(0.125)
        # Note: type Control C to cancel.


def drum_continuous_high_beats():
    while True:
        sample(psonic.DRUM_HEAVY_KICK, rate=random.randrange(30, 50))
        sleep(0.125)
        # Note: type Control C to cancel.


def vinyl_scratch():
    sample(psonic.VINYL_HISS)
    sleep(2)
    sample(psonic.VINYL_SCRATCH)
    sleep(0.25)
    sample(psonic.VINYL_SCRATCH)
    sleep(0.25)
    sample(psonic.VINYL_SCRATCH)
    sleep(0.25)
    sample(psonic.VINYL_SCRATCH)
    sleep(0.25)


def custom_sound():
    # play any wav file that you choose (just save it in the same directory)
    # you can download them from the internet (e.g. https://freewavesamples.com/)
    # or make your own:
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    sound_file = os.path.join(dir_path,'sounds/harley_davidson.wav')
    start = 0.0  # float between 0 and 1
    finish = 1.0  # float between 0 and 1
    file_path = os.path.abspath(sound_file)
    command = 'sample "{0}", start: {1}, finish: {2}'.format(
        file_path, start, finish)

    psonic.run(command)
