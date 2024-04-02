'''
from gridworld import *
mdp = GridWorld () 

print ( " states : " ,mdp . get_states ( ) ) 
print ("terminal states : " , mdp.get_goal_states ()) 
print ("actions : " , mdp . get_actions ( ) ) 
print (mdp . get_transitions (mdp . get_initial_state () , mdp . UP)) 

def policy_custom (state) :
    return mdp . UP 

while(1): 
    state = mdp.get_initial_state () 
    new_state,_ = mdp.execute (state , policy_custom (state))
    mdp . initial_state = new_state
    mdp . visualise() 

'''
from pynput import keyboard
from gridworld import *

mdp = GridWorld()

# Define the action mapping
key_to_action = {
    keyboard.Key.up: mdp.UP,
    keyboard.Key.down: mdp.DOWN,
    keyboard.Key.left: mdp.LEFT,
    keyboard.Key.right: mdp.RIGHT,
}

# Define the event handler
def on_press(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    elif key in key_to_action:
        action = key_to_action[key]
        new_state, _ = mdp.execute(mdp.get_initial_state(), action)
        mdp.initial_state = new_state
        mdp.visualise()

# Start listening to keyboard events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()