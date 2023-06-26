###### Project: CPSC 481 - Pacman State Space Search
###### Group Name: Some Name
###### Authors: Gabriel Warkentin, Patrick Lin, Kevin Duarte, Olvin Bolanos

# About

**Pacman State Space Search Game** consists of learning BFS and DFS to find paths within the maze world, both to reach a particular location and to collect food efficiently. This program was written in Python 3.6. 

You should be able to play a game of Pacman by typing the following at the command line:

     python3 pacman.py

To test DFS, run the following commands:

     python pacman.py -l tinyMaze -p SearchAgent
     python pacman.py -l mediumMaze -p SearchAgent
     python pacman.py -l bigMaze -z .5 -p SearchAgent

To test BFS, run the following commands:

     python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
     python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5

# Installation Troubleshooting

This project requires a minimum of Python 3.6 but may not work if you are on Python 3.11 or above. If you have a newer version of Python and are having issues with running this project, you can make a separate environment using conda with the guide [here](https://stackoverflow.com/questions/43630002/conda-install-downgrade-python-version):

`conda create --name pacman python=3.6 anaconda`

Then:

`conda activate pacman`

When done running this project:

`conda deactivate`

## Additional Info

- Retrieve this code by either downloading a copy from Github or cloning the repository [here](https://github.com/Arbalest007/Pacman-State-Space-Search)