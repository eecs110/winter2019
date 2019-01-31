# CHALLENGE:
# refactor this code so that it uses a function
# then use that function to play any song (not just HAPPY_BIRTHDAY)
# coming soon: better ways of representing songs to account for
# rhythm -- not just notes!
import psonic
HAPPY_BIRTHDAY = [
    48, 48, 50, 48, 53, 52, 48, 48, 50, 48, 55, 53,
    48, 48, 60, 57, 53, 52, 50, 58, 58, 57, 53, 55, 53
]

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

psonic.use_synth(psonic.PIANO)
psonic.play(HAPPY_BIRTHDAY[0])
psonic.sleep(0.25)
psonic.play(HAPPY_BIRTHDAY[1])
psonic.sleep(0.25)
psonic.play(HAPPY_BIRTHDAY[2])
psonic.sleep(0.25)
psonic.play(HAPPY_BIRTHDAY[3])
psonic.sleep(0.25)
psonic.play(HAPPY_BIRTHDAY[4])
psonic.sleep(0.25)
psonic.play(HAPPY_BIRTHDAY[5])
psonic.sleep(0.25)
psonic.play(HAPPY_BIRTHDAY[6])
psonic.sleep(0.25)
psonic.play(HAPPY_BIRTHDAY[7])
psonic.sleep(0.25)
psonic.play(HAPPY_BIRTHDAY[8])
psonic.sleep(0.25)
psonic.play(HAPPY_BIRTHDAY[9])
psonic.sleep(0.25)
psonic.play(HAPPY_BIRTHDAY[10])
psonic.sleep(0.25)
psonic.play(HAPPY_BIRTHDAY[11])
psonic.sleep(0.25)
psonic.play(HAPPY_BIRTHDAY[12])
psonic.sleep(0.25)
psonic.play(HAPPY_BIRTHDAY[13])
psonic.sleep(0.25)
psonic.play(HAPPY_BIRTHDAY[14])
psonic.sleep(0.25)
psonic.play(HAPPY_BIRTHDAY[15])
psonic.sleep(0.25)
psonic.play(HAPPY_BIRTHDAY[16])
psonic.sleep(0.25)
psonic.play(HAPPY_BIRTHDAY[17])
psonic.sleep(0.25)
psonic.play(HAPPY_BIRTHDAY[18])
psonic.sleep(0.25)
psonic.play(HAPPY_BIRTHDAY[19])
psonic.sleep(0.25)
psonic.play(HAPPY_BIRTHDAY[20])
psonic.sleep(0.25)
psonic.play(HAPPY_BIRTHDAY[21])
psonic.sleep(0.25)
psonic.play(HAPPY_BIRTHDAY[22])
psonic.sleep(0.25)
psonic.play(HAPPY_BIRTHDAY[23])
psonic.sleep(0.25)
psonic.play(HAPPY_BIRTHDAY[24])
psonic.sleep(0.25)