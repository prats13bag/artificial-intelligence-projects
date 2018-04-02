# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        #iterating over all states and over all possible actions from each of these states
        #complexity of each iteration is O(S*A*S); S is no. of states and A is all possible actions from that state

        for each in range(0, self.iterations):
            states = self.mdp.getStates()        
            stateValuePair = util.Counter()
            for state in states:
                #get all possible actions which can be taken from this state
                actions = self.mdp.getPossibleActions(state)
                actionValuePair = util.Counter()
                for action in actions:
                    #compute QValue for each action for this state and store it in actionValuePair dictionary
                    actionValuePair[action] = self.computeQValueFromValues(state, action)
                stateValuePair[state] = actionValuePair[actionValuePair.argMax()]
            
            for state in states:
                self.values[state] = stateValuePair[state]

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        Qvalue = 0
        allTransitions = self.mdp.getTransitionStatesAndProbs(state, action)
        for transition in allTransitions:
            # transition[0] has the successor state (s-prime) represented in co-ordinates
            # transition[1] has the probablity of reaching a particular successor state (s-prime) from state, action pair
            rewardValue = self.mdp.getReward(state, action, transition[0])
            Qvalue+=transition[1] * (rewardValue + self.discount * self.values[transition[0]])
        return Qvalue
        util.raiseNotDefined()

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        value=util.Counter()
        if len(self.mdp.getPossibleActions(state))==0:
            return None #returns None when there is no possible actions
        else:
            for action in self.mdp.getPossibleActions(state):
                value[action] = self.computeQValueFromValues(state, action)
            return value.argMax() #returns that action which has maxmium among all QValues
        util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
