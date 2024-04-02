from gridworld import *
from q_learning import *

mdp = GridWorld()

# Generate the policy
agent = q_agent(mdp)
agent.solve(num_episodes=1000)  # You may need to adjust the number of episodes
policy = {state: max(agent.Q[state], key=agent.Q[state].get) for state in mdp.get_states()}

while True:
    state = mdp.get_initial_state()
    action = policy[state]
    new_state, _ = mdp.execute(state, action)
    mdp.initial_state = new_state
    mdp.visualise()