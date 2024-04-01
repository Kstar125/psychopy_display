The following script is used to display fixation cross and visual text stimuli during EEG sessions as required.

To start the script use PsychoPy (v2023.2.3) and configure the following parameters.

By default:

Frames per second (Hz): 144

Session Length: 21 minutes (20 minute stimulus and 4 blocks of 15 second instruction texts)

HZ_DISPLAY = 144 (adjust frame rate as needed for the host computer running the experiment)

NUM_MINUTES = 20 (adjust minutes of stimulus presentation as needed)

FRAME_NUM (Converting NUM_MINUTES and HZ_DISPLAY into a format workable for PsychoPy)

BLOCK_TIME (Time per experiment block, three blocks within the 20 minute period)

INSTRUCTION_FRAME_NUM = HZ_DISPLAY * 15 (Adjust as needed for the length of instruction text presentation on screen in seconds)

Once configured, the Python Script should present three blocks and four instruction text periods with no input from either
administrator or participant.