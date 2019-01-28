from psonic import *

def play_riff_1(speed):
    sample(DRUM_BASS_HARD, rate=1)
    sleep(.25 * speed)
    sample(DRUM_SNARE_HARD)
    sleep(.125 * speed)
    sample(DRUM_BASS_HARD, rate=1)
    sleep(.25 * speed)
    sample(DRUM_BASS_HARD, rate=1)
    sleep(.125 * speed)
    sample(DRUM_SNARE_HARD)
    sleep(0.25 * speed)

def play_riff_2(speed):
    for i in range(16):
        r = random.randrange(1,10)
        sample(DRUM_BASS_HARD, rate=r)
        sleep(0.125 * speed)

def play_riff_3(speed):

    use_synth(PROPHET)
    sc = scale(E2, MINOR)
    s = random.choice([
        0.125 * speed,
        0.25 * speed,
        0.5 * speed
    ])
    for i in range(8):
        r = random.choice([0.125, 0.25, 1, 2])
        n = random.choice(sc)
        co = random.randint(30,100)
        play(n, release = r, cutoff = co)
        sleep(s)

def play_base_beat(speed):
    # print base beat
    for i in range(4):
        sample(DRUM_CYMBAL_PEDAL)
        sleep(speed / 2)