from psychopy import visual, core, clock

#Constants

win = visual.Window([1920, 1080])
 
HZ_DISPLAY = 144 #Computer FPS.
 
NUM_MINUTES = 20 # Session time in minutes.
 
FRAME_NUM = HZ_DISPLAY * 60 * NUM_MINUTES #Number of Hz * 60s * Number of Minutes

BLOCK_TIME = int(FRAME_NUM / 3) 

INSTRUCTION_FRAME_NUM = HZ_DISPLAY * 15 #144 Hz * 15s

free_gaze_msg = visual.TextStim(win, text="Feel free to let your mind wander and look anywhere on the screen.")

fixation = visual.TextStim(win, text="+")
fixation.size = 1.2

close_eye_msg = visual.TextStim(win, text="Please close your eyes for this portion of the session.")

#Instruction messages

first_phase_instruction_msg = visual.TextStim(win, text="Welcome!\n For the first phase of the session, feel free to look anywhere on the screen.")

second_phase_instruction_msg = visual.TextStim(win, text="Please look at the fixation cross at the centre of the screen for this phase of the session (approximately 7 minutes).")

third_phase_instruction_msg = visual.TextStim(win, text="For the last phase of the session (approximately 7 minutes), please close your eyes. The session administrators will let you know when the phase ends.")

complete_phase_instruction_msg = visual.TextStim(win, text="Thank you for participating in this session! The administrators will let you know about next steps shortly.")

#Block functions

def free_gaze_block():
    free_gaze_msg.draw()

def fixation_block():
    fixation.draw()
    
def close_eye_block():
    close_eye_msg.draw()
    
def instruction_block(instance_count):
    for instructionFrameN in range(INSTRUCTION_FRAME_NUM):
        if instructionFrameN < INSTRUCTION_FRAME_NUM:
            if instance_count == 0:
                first_phase_instruction_msg.draw()
            if instance_count == 1:
                second_phase_instruction_msg.draw()
            if instance_count == 2:
                third_phase_instruction_msg.draw()
            if instance_count == 3:
                complete_phase_instruction_msg.draw()
        win.flip()

#First 15 seconds for instruction presentation followed by one third of
#time allocated for the first block, then 15 seconds for another instruction
#block and so on...

instruction_block(0)

for frameN in range(BLOCK_TIME):
    if frameN < BLOCK_TIME:
        free_gaze_block()
    win.flip()
    
instruction_block(1)  

for frameN in range(BLOCK_TIME):
    if frameN < BLOCK_TIME:
        fixation_block()
    win.flip()
    
instruction_block(2)

for frameN in range(BLOCK_TIME):
    if frameN < BLOCK_TIME:
        close_eye_block()
    win.flip()
        
instruction_block(3)

#Proof of Concept
#Using a 144 Hz screen to display 1 minute of stimulus in 4 sections
# 144 * 60 = 8640

#gabor = visual.GratingStim(win, tex='sin', mask='gauss', sf= 5, name = 'gabor',
#    autoLog=False)
#fixation = visual.GratingStim(win, tex=None, mask='gauss', sf=0, size =0.02,
#    name = 'fixation', autoLog=False)

#for frameN in range(8640):
#    if 0 <= frameN < 2160:
#        fixation.draw()
#    if 2161 <= frameN < 4320:
#        gabor.phase += 0.1
#        gabor.draw()
#    if 4321 <= frameN < 6480:
#        fixation.draw()
#    if 6481 < frameN < 8640:
#        gabor.phase += 0.1
#        gabor.draw()
#    win.flip()