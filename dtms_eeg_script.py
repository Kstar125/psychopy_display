from psychopy import visual, core, clock

#Constants

win = visual.Window([1920, 1080]) #PsychoPy display size.
 
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
    """Render the free_gaze_block stimulus on-screen."""
    free_gaze_msg.draw()

def fixation_block():
    """Render the fixation_block stimulus on-screen."""
    fixation.draw()
    
def close_eye_block():
    """Render the close_eye_msg stimulus on-screen."""
    close_eye_msg.draw()
    
def stimulus_block(stimulus_choice):
    """
    Chooses from the three possible stimulus options 
    (chosen with stimulus_choice) and renders the stimulus on-screen.

    The stimulus will be visible on-screen for a default of 1/3 of the 
    NUM_MINUTES constant on a 144 Hz system. Adjust the value and the 
    HZ_DISPLAY constant to optimize stimulus presentation time.
    """
    
    if stimulus_choice == 0: #Free Gaze Block
        for frameN in range(BLOCK_TIME):
            if frameN < BLOCK_TIME:
                free_gaze_block()
            win.flip()
                
    if stimulus_choice == 1: #Fixation Block
        for frameN in range(BLOCK_TIME):
            if frameN < BLOCK_TIME:
                fixation_block()
            win.flip()
                
    if stimulus_choice == 2: #Closed Eye Block
        for frameN in range(BLOCK_TIME):
            if frameN < BLOCK_TIME:
                close_eye_block()
            win.flip()
            

    
def instruction_block(instruction_choice):
    """
    Chooses from the four possible instruction texts (chosen with 
    instance_count and renders the instructions on-screen. 

    The instructions will be viewable on-screen for a default of 15 seconds 
    (adjust the INSTRUCTION_FRAME_NUM constant to change this time value).
    """
    
    for instructionFrameN in range(INSTRUCTION_FRAME_NUM):
        if instructionFrameN < INSTRUCTION_FRAME_NUM:
            if instruction_choice == 0:
                first_phase_instruction_msg.draw()
            if instruction_choice == 1:
                second_phase_instruction_msg.draw()
            if instruction_choice == 2:
                third_phase_instruction_msg.draw()
            if instruction_choice == 3:
                complete_phase_instruction_msg.draw()
        win.flip()

def main():
    
    instruction_block(0)
    
    stimulus_block(0)
    
    instruction_block(1)  
    
    stimulus_block(1)

    instruction_block(2)
    
    stimulus_block(2)
        
    instruction_block(3)
    
if __name__ == "__main__":
    main()

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