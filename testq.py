from gridworld import *
from q_learning import *

mdp = GridWorld()

agent = q_agent(mdp, alpha=0.5, epsilon=0.1)

agent.solve(num_episodes=1000)

policy = {state: agent.epsilon_greedy(state) for state in mdp.get_states()}

print("Policy:", policy)

values = {state: agent.state_value(state) for state in mdp.get_states()}

print("Values:", values)