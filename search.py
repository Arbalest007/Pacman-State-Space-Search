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

def depthFirstSearch(problem):
    return Most_of_Best_First(problem, algorithm='DFS')
    """
    Search the deepest nodes in the search tree first.
    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    """
    """
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """

def Most_of_Best_First(problem, algorithm):
    if algorithm == 'DFS':
        open_structure= util.Stack
    elif algorithm == 'BFS':
        open_structure= util.Queue
    else:
        raise NotImplementedError(f'algorithm {algorithm} not avaialable')
    
    open = open_structure() # if we put the children on in reverse order, then it is same as pulling from the left
    open.push(problem.getStartState())
    closed = util.Queue()
    parents = {}
    parents[problem.getStartState()] = None
    while not open.isEmpty():
        #print(f'open {open.list}')
        X = open.pop()
        #print(f'X {X}')
        #print(f'open after pop {open.list}')
        closed.push(X)

        if problem.isGoalState(X):
            path_list = util.Queue()
            parent = parents[X] # gives back a whole ('A', ('C', '1:A->C', 2.0))
            while parent is not None:
                path_list.push(parent[1][1]) # add just the path part
                parent = parents[parent[0]] # look up next parent
                
            return path_list.list

        # generate successors and filter down
        children = problem.getSuccessors(X)
        keep_children_labels = []
        for child in children:
            if not (child[0] in closed.list):
                if algorithm != 'BFS' or (not child[0] in open.list): # idk why this check is only good on BFS
                    keep_children_labels.append(child[0])
                    parents[child[0]] = (X, (child))  # set the child's id key, like 'B' to give it's parent (the current state) such as ('A', ('B', '0:A->B', 1.0))

        #kcl_reversed = keep_children_labels[::-1] # I guess don't reverse after all?
        kcl_reversed = keep_children_labels # hashtag justpythonthings
        for child in kcl_reversed:
            open.push(child) 

    return []
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()
    """

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    return Most_of_Best_First(problem, algorithm='BFS')

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
