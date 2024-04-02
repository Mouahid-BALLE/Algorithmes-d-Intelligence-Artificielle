from mdp import *
from gridworld import *
import numpy.linalg as l 
import numpy as np 

class dp_agent():
    mdp=GridWorld()
    dicoV = {}
    dicoV_bis = {}
    ''' add attributes here! '''
    
    def __init__(self, mdp): #and here...
        self.mdp=mdp
        self.dicoV = {s : 0 for s in self.mdp.get_states()}
        self.dicoV_bis = {s : 0 for s in self.mdp.get_states()}

    def get_value(self,s,dicoV):
        #return the value of a specific state s according to value function v
        return dicoV[s]
        
    def get_width(self,v,v_bis):
        #return the absolute norm between two value functions
        return max(abs(v[s]-v_bis[s]) for s in self.mdp.get_states())

    def solve(self):
        #main solving loop
        eps=0.001
        continue_loop = True
        print(" ici ")
        print(self.get_width(self.dicoV, self.dicoV_bis))
        while(continue_loop):
            self.dicoV_bis = self.dicoV.copy()
            for etat in self.mdp.get_states():
                self.dicoV[etat]=self.update(etat)
            print(" la ")
            print(self.get_width(self.dicoV, self.dicoV_bis))
            if self.get_width(self.dicoV, self.dicoV_bis) < eps:
                continue_loop = False
        return self.dicoV

    def sumPV(self, s, action):
        somme=0
        for s_next, proba in self.mdp.get_transitions( s,action):
            somme += proba * self.dicoV_bis[s_next]
        return somme

    def getR(self, s, action):
        sum=0
        for s_next, proba in self.mdp.get_transitions( s,action):
            sum+= proba * self.mdp.get_reward( s, action, s_next)
        return sum



    def update(self,s):
        #updates the value of a specific state s
        tab = [None] * len(self.mdp.get_actions(s))
        t=0
        for action in self.mdp.get_actions(s) :
            tab[t]= self.getR(s, action) + self.mdp.get_discount_factor() * self.sumPV(s, action)
            t=t+1

        return max(tab)

    def get_policy(self):
        policy = {}
        for s in self.mdp.get_states():
            best_action = None
            best_value = -float('inf')
            for a in self.mdp.get_actions(s):
                action_value = self.getR(s, a) + self.mdp.get_discount_factor() * self.sumPV(s, a)
                if action_value > best_value:
                    best_value = action_value
                    best_action = a
            policy[s] = best_action
        return policy