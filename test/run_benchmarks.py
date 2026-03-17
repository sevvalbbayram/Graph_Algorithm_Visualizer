import time
import dijkstar
from dijkstar import Graph, find_path
import sys
import os

# Add the parent directory to sys.path to access the components folder
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
from components.grid import Grid
from components.spot import Spot
from algorithms.dijkstra import dijkstra
from tests.benchmark_utils import dijkstra_non_graphical

def prepare_grid(rows, cols, start_pos, end_pos, barriers=None):
    grid = Grid(rows, cols, 500, 500)  # Adjust the size as needed
    if barriers:
        for row, col in barriers:
            grid.grid[row][col].set_barrier()
    grid.update_neighbors()
    return grid, grid.grid[start_pos[0]][start_pos[1]], grid.grid[end_pos[0]][end_pos[1]]

def prepare_dijkstar_graph(grid):
    graph = Graph()
    for row in grid.grid:
        for spot in row:
            if not spot.is_barrier():
                for neighbor in spot.get_neighbors(grid.grid):
                    graph.add_edge(spot.get_pos(), neighbor.get_pos(), {'cost': 1})
    return graph

def benchmark_algorithm(algorithm, setup, runs=10):
    total_time = 0
    for _ in range(runs):
        grid, start, end = setup()
        start_time = time.perf_counter()
        algorithm(grid, start, end)
        end_time = time.perf_counter()
        total_time += end_time - start_time
    return total_time / runs

def run_dijkstar(graph, start, end):
    return find_path(graph, start.get_pos(), end.get_pos(), cost_func=lambda u, v, edge, prev_edge: edge['cost'])

def benchmark():
    rows, cols = 50, 50
    width = 500
    total_rows = 50
    start_pos, end_pos = (0, 0), (49, 49)
    barriers = [(row, 24) for row in range(20, 30)]

    setup_my_dijkstra = lambda: prepare_grid(rows, cols, start_pos, end_pos, barriers)
    setup_dijkstar = lambda: (
        prepare_dijkstar_graph(prepare_grid(rows, cols, start_pos, end_pos, barriers)[0]), 
        Spot(*start_pos, width, total_rows), 
        Spot(*end_pos, width, total_rows)
    )

    my_dijkstra_time = benchmark_algorithm(lambda grid, start, end: dijkstra_non_graphical(grid, start, end), setup_my_dijkstra)

    # Benchmark Dijkstar implementation
    dijkstar_time = benchmark_algorithm(lambda graph, start, end: run_dijkstar(graph, start, end), setup_dijkstar)

    print(f"My Dijkstra Average Time: {my_dijkstra_time:.6f} seconds")
    print(f"Dijkstar Average Time: {dijkstar_time:.6f} seconds")

    if my_dijkstra_time < dijkstar_time:
        print("My Dijkstra implementation is faster.")
    elif my_dijkstra_time > dijkstar_time:
        print("Dijkstar implementation is faster.")
    else:
        print("Both implementations have the same average time.")

if __name__ == "__main__":
    benchmark()
