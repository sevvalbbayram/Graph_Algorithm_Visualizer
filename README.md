
# Graph Algorithm Visualizer

## Introduction

In this project, we developed a tool to visualize different graph traversal algorithms in Python. The main focus of the project was on Dijkstra and A* algorithms but we also implemented BFS (Breadth-First Search) and DFS (Depth-First Search). The methodology and descriptions of the algorithms are discussed in the “Algorithms” section. 
The pathfinding visualization demonstrates an animation to trace paths according to the algorithms. It utilizes Pygame to visualize. The animation allows one to choose start and end points and build borders before finding a path. Different features and keys are explored in “Usage.” 


## Project Structure

- **algorithms**
  - `dijkstra.py`: Implementation of Dijkstra's algorithm.
  - `a_star.py`: Implementation of A* algorithm for pathfinding.
  - `bfs.py`: Implementation of BFS algorithm.
  - `dfs.py`: Implementation of DFS algorithm.
- **components**
  - `spot.py`: Definition and management of a spot/node in the grid.
  - `grid.py`: Handling grid functionality, drawings, and updates.
- **tests**
  - `benchmark_utils.py`: Benchmarking utilities for all the algorithms. Non Graphical Versions of algorith,s
  - `run_benchmarks.py`: Benchmarking to compare Python's built-in Dijkstra's Algoritm and our version.
  - `test_algorithms.py`: Unit tests for the algorithms.
- **assets**
  - `demo.mov`: A demonstration video providing an example of expected outcomes.
- **main.py**: Main script to execute the application.
- **pyproject.toml**: Configuration file for Poetry, outlining project dependencies.

## Prerequisites

- **Python** (3.11 or later preferred to run Poetry)
- **Poetry** : A tool to manage dependencies
- **Pygame** : A Python library for creating games and multimedia applications.
- **dijkstar** : A Python library for graph algorithms

If you haven't installed Poetry, you can do so following the instructions here.
```bash
pip install poetry
```
To install dependencies, use Poetry and it will install all the dependencies:
```bash
poetry install
```

Active the virtual environment before running the project.

## Usage
- Running python3 main.py will run the program. A clear, white grid appears.
- To start, position a starting point (green point) and ending point (red point) using the left click. 
- After that, borders (black blocks) can be drawn using the left click.
- Finally, selected algorithm runs according to the keys.
- When the algorithm finds the path, it will appear in yellow.
- The terminal displays the time taken, nodes traversed, path length and nodes skipped after the path is found.

## Interacting with the Grid

**Set Start and End Points:** **Left-click** to place the start (green) and end (red) points on the grid.

**Create Barriers:** After setting start and end points, additional left-clicks create barriers (black).

**Remove Elements:** **Right-click** to remove a barrier, start, or end point.

**Drag to Create Barriers:** Click and drag the left mouse button to draw continuous barriers.

**Using Keyboard Shortcuts**
**A* Algorithm*: Press **Space** to run the A* algorithm.

**Dijkstra's Algorithm:** Press **D** to run Dijkstra's algorithm.

**Breadth-First Search (BFS):** Press **B** to run the BFS algorithm.

**Depth-First Search (DFS):** Press **F** to run the DFS algorithm.

**Clear Path:** Press **C** to clear the path and traces, retaining barriers and points.

**Reset Grid:** Press **R** to reset the grid completely.

## Output Statistics

After each algorithm run, statistics such as time taken, nodes traversed, path length, and nodes skipped are printed to the console. This information helps compare the efficiency and characteristics of each algorithm.
EXAMPLE : “Dijkstra's Time: 2.971236 seconds, Nodes Traversed: 1805, Path Length: 43, Nodes Skipped: 3470”


## Algorithms

### A*
A*, or A Star, is a graph traversal algorithm that is often used to find the shortest path. It employes a heuristic function and considers both costs of the path from starting point to the current node and from the current node to the end point. 

### BFS
Breadth-First Search, often abbreviated as BFS, is a graph traversal and search algorithm that guarantees to find the shortest path. It visits all the nodes in the depth level before going into the next depth level, using a queue to maintain the order.

### DFS
Depth-First Search, often abbreviated as DFS, is another algorithm for traversing and searching graphs. It visits explore all the branches of the current node in depth before moving to the next one, uses stack to maintain the order. Although it doesn’t guarantee the shortest path, it is preferred for maze solving tasks.

### Dijkstra
Dijkstra’a algorithm is a greedy, single source shortest path algorithm. It iteratively finds the shortest path from the source to other nodes and updates until the shortest path is found. 


## Challenges
- One of the challenges was to test and validate our algorithms. It was hard to decide how we wanted to test them, the algorithm file itself or the application run by main.py. We tried different techniques but finally found the one that works the best for the algorithm.

- We tried the find the optimal way to print the statistics. After trying several methods, such as printing with the visualization tool and printing on the terminal, we concluded that printing on the terminal is the most efficient way. It allows us to compare algorithms after running them on the same scenario as the statistics stay on the terminal after every run.

- Benchmarking for the bonus part was also challenging. It required further understanding of the Dijkstra's algorithm and out-of-the-box thinking. We tried our best to beat the Dijkstar module implementation but were unable to do so.

## Contributors
Nathan Wongkar (nathan.wongkar@u.yale-nus.edu.sg) and Sevval Begum Bayram (sbayram@u.yale-nus.edu.sg)

November 2023
