from gridworld import *
from dynamic_programming import *


mdp = GridWorld()

agent = dp_agent(mdp)

agent.solve()

agent.get_policy()

print(agent.dicoV)

