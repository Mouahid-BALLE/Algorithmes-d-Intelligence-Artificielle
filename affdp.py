from gridworld import *
from dynamic_programming import *

mdp = GridWorld()

# Generate the policy
agent = dp_agent(mdp)
agent.solve()
policy = agent.get_policy()

while True:
    state = mdp.get_initial_state()
    action = policy[state]
    new_state, _ = mdp.execute(state, action)
    mdp.initial_state = new_state
    mdp.visualise()