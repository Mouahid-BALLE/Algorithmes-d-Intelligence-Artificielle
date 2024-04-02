from mdp import *
from gridworld import *
import random 
from matplotlib import pyplot as plt

class q_agent:

    mdp=GridWorld()
    Q = {}
    alpha = 0.5
    epsilon = 0.1
    '''
    add attributes here!
    '''

    def __init__(self, mdp, alpha=0.5, epsilon=0.1):# and here...
        self.mdp = mdp
        self.alpha = alpha
        self.epsilon = epsilon
        self.discount_factor = self.mdp.get_discount_factor()
        self.Q = {s : {a : 0 for a in self.mdp.get_actions(s)} for s in self.mdp.get_states()}

    def epsilon_greedy(self,s):
        #epsilon-greedy policy
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(self.mdp.get_actions(s))
        else:
            return max(self.mdp.get_actions(s), key=lambda a: self.Q[s][a])

    def solve(self, num_episodes):
        #main solving loop
        for _ in range(num_episodes):
            s = random.choice(self.mdp.get_states())
            while not self.mdp.is_terminal(s):
                a = self.epsilon_greedy(s)
                transitions = self.mdp.get_transitions(s, a)
                s_next = random.choices(
                    population=[state for state, prob in transitions],
                    weights=[prob for state, prob in transitions],
                    k=1
                )[0]
                reward = self.mdp.get_reward(s, a, s_next)
                delta = self.get_delta(reward, self.Q[s][a], s_next)
                self.Q[s][a] += self.alpha * delta
                s = s_next

    def get_delta(self, reward, q_value, next_state):
        #Compute delta for the update
        return reward + self.discount_factor * max(self.Q[next_state][a_next] for a_next in self.mdp.get_actions(next_state)) - q_value

    def state_value(self, state):
        #Get the value of a state
        return max(self.Q[state][a] for a in self.mdp.get_actions(state))