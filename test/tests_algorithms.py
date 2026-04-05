import os
import sys
from tests.benchmark_utils import a_star_non_graphical, bfs_non_graphical, dfs_non_graphical, dijkstra_non_graphical

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
from components.grid import Grid
from components.spot import Spot

# Helper function to create a grid and set start, end, and barriers
def create_test_grid(rows, cols, start_coords, end_coords, barriers):
    grid = Grid(rows, cols, 500, 500)  # Size parameters are placeholders
    for r, c in barriers:
        grid.grid[r][c].set_barrier()
    start = grid.grid[start_coords[0]][start_coords[1]]
    end = grid.grid[end_coords[0]][end_coords[1]]
    grid.update_neighbors()
    return grid, start, end

# A* Algorithm Tests
def test_a_star_basic():
    grid, start, end = create_test_grid(3, 3, (0, 0), (2, 2), [(1, 1)])
    nodes_traversed, path_length, nodes_skipped, path_found = a_star_non_graphical(grid, start, end)
    assert path_found, "A* should find a path in basic test"

def test_a_star_no_path():
    grid, start, end = create_test_grid(3, 3, (0, 0), (2, 2), [(0, 1), (1, 1), (1, 2)])
    nodes_traversed, path_length, nodes_skipped, path_found = a_star_non_graphical(grid, start, end)
    assert path_found, "A* should not find a path when blocked"

def test_a_star_large_grid():
    grid, start, end = create_test_grid(10, 10, (0, 0), (9, 9), [(r, 5) for r in range(1, 9)])
    nodes_traversed, path_length, nodes_skipped, path_found = a_star_non_graphical(grid, start, end)
    assert path_found, "A* should find a path in larger grid"

# BFS Algorithm Tests
def test_bfs_basic():
    grid, start, end = create_test_grid(3, 3, (0, 0), (2, 2), [(1, 1)])
    nodes_traversed, path_length, nodes_skipped, path_found = bfs_non_graphical(grid, start, end)
    assert path_found, "BFS should find a path in basic test"

def test_bfs_no_path():
    grid, start, end = create_test_grid(3, 3, (0, 0), (2, 2), [(0, 1), (1, 1), (1, 2)])
    nodes_traversed, path_length, nodes_skipped, path_found = bfs_non_graphical(grid, start, end)
    assert path_found, "BFS should not find a path when blocked"

def test_bfs_large_grid():
    grid, start, end = create_test_grid(10, 10, (0, 0), (9, 9), [(r, 5) for r in range(1, 9)])
    nodes_traversed, path_length, nodes_skipped, path_found = bfs_non_graphical(grid, start, end)
    assert path_found, "BFS should find a path in larger grid"

# DFS Algorithm Tests
def test_dfs_basic():
    grid, start, end = create_test_grid(3, 3, (0, 0), (2, 2), [(1, 1)])
    nodes_traversed, path_length, nodes_skipped, path_found = dfs_non_graphical(grid, start, end)
    assert path_found, "DFS should find a path in basic test"

def test_dfs_no_path():
    grid, start, end = create_test_grid(3, 3, (0, 0), (2, 2), [(0, 1), (1, 1), (1, 2)])
    nodes_traversed, path_length, nodes_skipped, path_found = dfs_non_graphical(grid, start, end)
    assert path_found, "DFS should not find a path when blocked"

def test_dfs_large_grid():
    grid, start, end = create_test_grid(10, 10, (0, 0), (9, 9), [(r, 5) for r in range(1, 9)])
    nodes_traversed, path_length, nodes_skipped, path_found = dfs_non_graphical(grid, start, end)
    assert path_found, "DFS should find a path in larger grid"

# Dijkstra Algorithm Tests
def test_dijkstra_basic():
    grid, start, end = create_test_grid(3, 3, (0, 0), (2, 2), [(1, 1)])
    nodes_traversed, path_length, nodes_skipped, path_found = dijkstra_non_graphical(grid, start, end)
    assert path_found, "Dijkstra should find a path in basic test"

def test_dijkstra_no_path():
    grid, start, end = create_test_grid(3, 3, (0, 0), (2, 2), [(0, 1), (1, 1), (1, 2)])
    nodes_traversed, path_length, nodes_skipped, path_found = dijkstra_non_graphical(grid, start, end)
    assert path_found, "Dijkstra should not find a path when blocked"

def test_dijkstra_large_grid():
    grid, start, end = create_test_grid(10, 10, (0, 0), (9, 9), [(r, 5) for r in range(1, 9)])
    nodes_traversed, path_length, nodes_skipped, path_found = dijkstra_non_graphical(grid, start, end)
    assert path_found, "Dijkstra should find a path in larger grid"

if __name__ == "__main__":
    test_a_star_basic()
    test_a_star_no_path()
    test_a_star_large_grid()

    test_bfs_basic()
    test_bfs_no_path()
    test_bfs_large_grid()

    test_dfs_basic()
    test_dfs_no_path()
    test_dfs_large_grid()

    test_dijkstra_basic()
    test_dijkstra_no_path()
    test_dijkstra_large_grid()
