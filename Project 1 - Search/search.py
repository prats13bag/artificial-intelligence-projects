# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import time

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    print("!!!!!!!!!!!!!!!!!!!!!!!")
    print "Start:", problem.getStartState()
    import time
    time.sleep(10)
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())

    """
    #create a node in the beginning
    #p is parent node(which is a dictionary itself)
    #pos - Cordinates of current node's position
    #direction: E/W/N/S
    #Initial node has no parent
    vertex = {}
    vertex["p"] = None
    vertex["pos"] = problem.getStartState()
    vertex["direction"] = None
    frontier = util.Stack()
    frontier.push(vertex)
    frontier.push(vertex)
    
    explored = list()

    while not frontier.isEmpty():
        vertex = frontier.pop()
        current = vertex["pos"]
        if current in explored:
            continue
        explored.append(current) 
        if problem.isGoalState(current):
            break
        for actions in problem.getSuccessors(current):
            if actions[0] not in explored:
                successor_vertex = {}
                successor_vertex["pos"] = actions[0]
                successor_vertex["direction"] = actions[1]
                successor_vertex["p"] = vertex
                frontier.push(successor_vertex)
    result = []
    while(not vertex["p"]==None):
        result.insert(0, vertex["direction"])
        vertex = vertex["p"]
    return result
    util.raiseNotDefined()


def breadthFirstSearch(problem):
    vertex = {}
    vertex["p"] = None
    vertex["pos"] = problem.getStartState()
    vertex["direction"] = None
    frontier = util.Queue()
    frontier.push(vertex)
    frontier.push(vertex)
    explored = list()
    while not frontier.isEmpty():
        vertex = frontier.pop()
        current = vertex["pos"]
        if current in explored:
            continue
        explored.append(current) 
        if problem.isGoalState(current):
            break
        for actions in problem.getSuccessors(current):
            if actions[0] not in explored:
                successor_vertex = {}
                successor_vertex["pos"] = actions[0]
                successor_vertex["direction"] = actions[1]
                successor_vertex["p"] = vertex
                frontier.push(successor_vertex)
    result = []
    while(not vertex["p"]==None):
        result.insert(0, vertex["direction"])
        vertex = vertex["p"]
    return result
    util.raiseNotDefined()


def uniformCostSearch(problem):
    vertex = {}
    vertex["p"] = None
    vertex["pos"] = problem.getStartState()
    vertex["direction"] = None
    vertex["path_cost"] = 0
    frontier = util.PriorityQueue()
    frontier.push(vertex, vertex["path_cost"])
    explored = list()
    while not frontier.isEmpty():
        vertex = frontier.pop()
        current = vertex["pos"]
        path_cost = vertex["path_cost"]
        if current in explored:
            continue
        explored.append(current) 
        if problem.isGoalState(current):
            break
        for actions in problem.getSuccessors(current):
            if actions[0] not in explored:
                successor_vertex = {}
                successor_vertex["pos"] = actions[0]
                successor_vertex["direction"] = actions[1]
                successor_vertex["p"] = vertex
                successor_vertex["path_cost"] = actions[2] + path_cost
                frontier.update(successor_vertex, successor_vertex["path_cost"])
    result = []
    while(not vertex["p"]==None):
        result.insert(0, vertex["direction"])
        vertex = vertex["p"]
    return result
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    print("**********************************")
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    vertex = {}
    vertex["p"] = None
    vertex["pos"] = problem.getStartState()
    vertex["direction"] = None
    vertex["path_cost"] = 0
    vertex["hrstc"] = heuristic(vertex["pos"], problem)
    frontier = util.PriorityQueue()
    frontier.push(vertex, vertex["path_cost"] + vertex["hrstc"])
    explored = list()
    while not frontier.isEmpty():
        vertex = frontier.pop()
        current = vertex["pos"]
        path_cost = vertex["path_cost"]
        if current in explored:
            continue
        explored.append(current) 
        if problem.isGoalState(current):
            break
        for actions in problem.getSuccessors(current):
            if actions[0] not in explored:
                successor_vertex = {}
                successor_vertex["pos"] = actions[0]
                successor_vertex["direction"] = actions[1]
                successor_vertex["p"] = vertex
                successor_vertex["path_cost"] = actions[2] + path_cost
                successor_vertex["hrstc"] = heuristic(actions[0], problem)
                frontier.push(successor_vertex, successor_vertex["hrstc"] + successor_vertex["path_cost"])
    result = []
    while(not vertex["p"]==None):
        result.insert(0, vertex["direction"])
        vertex = vertex["p"]
    return result
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
