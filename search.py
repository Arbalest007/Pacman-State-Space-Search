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
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

# def depthFirstSearch(problem):
#     """
#     Search the deepest nodes in the search tree first.

#     Your search algorithm needs to return a list of actions that reaches the
#     goal. Make sure to implement a graph search algorithm.

#     To get started, you might want to try some of these simple commands to
#     understand the search problem that is being passed in:

#     print("Start:", problem.getStartState())
#     print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
#     print("Start's successors:", problem.getSuccessors(problem.getStartState()))
#     """
#     "*** YOUR CODE HERE ***"
#     # print("Start:", problem.getStartState())
#     # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
#     # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    
#     # board = util.Stack()
#     # startState = problem.getStartState()

#     # for state in problem.getSuccessors:
#     #     print state[1]

#     # print(problem2Sub)
    
#     path = util.Stack()
#     startState = problem.getStartState()

#     item = [[], [problem.getStartState()]]
#     for state in problem.getSuccessors(startState):
#         print(state[0])
#         print(state[1])

#     util.raiseNotDefined()
        
# # Recursive DFS Solution
# # def DFS(problem, item):
# #     paths = util.Stack()

# #     if problem.isGoalState(item[1][-1]):
# #         return item[0]

# #     print([item[1]]) \
# #     [ paths.push([item[0]+[state[1]], item[1]+[state[0]]]) \
# #         for state in problem.getSuccessors(item[1][-1]) if not state[0] in item[1]]

# #     while not paths.isEmpty():
# #         directions = DFS(problem, paths.pop())

# #         if directions:
# #             return directions

# # def DFS(problem, node, visited):
# #     if

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
    directions = []
    visitedNodes = []

    return DFS(problem, problem.getStartState(), directions, visitedNodes + [problem.getStartState()])
        
def DFS(problem, currentPosition, directions, visitedNodes):
    children = util.Stack()

    print(directions)
    print(visitedNodes)

    if(problem.isGoalState(currentPosition)):
        return directions

    # for state in problem.getSuccessors(currentPosition):
    #     if state[0] not in visitedNodes:
    #         children.push(state)
        
    # while not children.isEmpty():
    #     possiblePath = children.pop()

    #     finalDirections = DFS(problem, possiblePath[0], directions + [possiblePath[1]], visitedNodes + [possiblePath[0]])

    #     if finalDirections is not None:
    #         return finalDirections

    # for state in problem.getSuccessors(currentPosition):
    #     if state[0] not in visitedNodes:
    #         finalDirections = DFS(problem, state[0], directions + [state[1]], visitedNodes + [state[0]])
                
    #         if finalDirections is not None:
    #             return finalDirections

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
