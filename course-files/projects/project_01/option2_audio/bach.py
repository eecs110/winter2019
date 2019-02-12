import psonic
import threader

psonic.use_synth(psonic.BEEP)

def low_part(tempo):
    psonic.play([55,59])
    psonic.sleep(1)
    psonic.play_pattern_timed([57], 0.5)
    psonic.play_pattern_timed([59], 1.5)
    psonic.play_pattern_timed([60], 1.5)
    psonic.play_pattern_timed([59], 1.5)
    psonic.play_pattern_timed([57], 1.5) #b5
    psonic.play_pattern_timed([55], 1.5) #b6
    psonic.play_pattern_timed([62, 59, 55, 62], 0.5) #b7
    psonic.play_pattern_timed([50, 60, 59, 57], 0.25)


def high_part(tempo):
    # TODO: the tempo should be controlled by the tempo variable
    psonic.play_pattern_timed([74], 0.5)
    psonic.play_pattern_timed([67, 69, 71, 72], 0.25)
    psonic.play_pattern_timed([74, 67, 67], 0.5)
    psonic.play_pattern_timed([76], 0.5)
    psonic.play_pattern_timed([72, 74, 76, 78], 0.25)
    psonic.play_pattern_timed([79, 67, 67], 0.5)
    psonic.play_pattern_timed([72], 0.5)
    psonic.play_pattern_timed([74, 72, 71, 69],0.25)
    psonic.play_pattern_timed([71], 0.5)
    psonic.play_pattern_timed([72, 71, 69, 67], 0.25)
    psonic.play_pattern_timed([66], 0.5)
    psonic.play_pattern_timed([67, 69, 71, 67], 0.25)
    psonic.play_pattern_timed([71, 69], 0.5)


def controller_riff(tempo):
    # the controller synchronizes the threads
    # make it really soft:
    psonic.sample(psonic.DRUM_BASS_SOFT, amp=0.3)
    psonic.sleep(tempo)


# Play 
controller = threader.SonicPiController(tempo=0.5, riff=controller_riff)
low_loop_thread = threader.SonicPiLoop(controller, low_part)
high_loop_thread = threader.SonicPiLoop(controller, high_part)
low_loop_thread.start()
high_loop_thread.start()