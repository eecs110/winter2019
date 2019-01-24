##################################################################################################
# Before you begin:
#   1. Download and install Sonic Pi: https://sonic-pi.net/
#   2. Install the psonic module using PIP. Run the following on the command line:
#      $ pip install python-sonic
#   3. Ensure that your Sonic Pi is running
#   
#
# Useful documentation:
#   1. psonic documentation: # https://github.com/gkvoelkl/python-sonic
#   2. MIDI Reference: http://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies
#   3. play function reference: https://docs.google.com/spreadsheets/d/1AlzpwvzsPou_gr532h8XKFWWlJY8l7QAfWFU2XXVgvI/edit#gid=860514818
##################################################################################################

import psonic

# Challenge: 
# 1. Use a while loop to repeat the drum beat below over and over again (forever)
# 2. When you're done with part 1, edit your while loop so that the loop breaks 
#    after 200 drum beats

psonic.sample(psonic.DRUM_BASS_HARD)
psonic.sleep(0.2)
psonic.sample(psonic.DRUM_CYMBAL_PEDAL)
psonic.sleep(0.2)