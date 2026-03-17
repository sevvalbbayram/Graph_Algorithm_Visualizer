import time
import heapq
from collections import deque

def benchmark_algorithm(algorithm, graph, start, end):
    start_time = time.perf_counter()
    algorithm(graph, start, end)
    end_time = time.perf_counter()
    return end_time - start_time

def run_algorithm_test(algorithm, test_cases):
    results = []
    for graph, start, end in test_cases:
        time_taken = benchmark_algorithm(algorithm, graph, start, end)
        results.append((graph.size(), time_taken))
    return results

def dijkstra_non_graphical(grid, start, end):
    open_set = []
    heapq.heappush(open_set, (0, start.get_pos(), start))  # Using position as secondary key
    closed_set = set()
    nodes_traversed = 0
    nodes_skipped = 0

    # Initialize g values for all nodes
    for row in grid.grid:
        for node in row:
            node.g = float('inf')
    start.g = 0

    while open_set:
        current_g, _, current = heapq.heappop(open_set)
        if current in closed_set:
            continue

        closed_set.add(current)
        nodes_traversed += 1

        if current == end:
            path_length = 0
            while current.came_from:
                current = current.came_from
                path_length += 1
            return nodes_traversed, path_length, nodes_skipped, True

        for neighbor in current.neighbors:
            if neighbor in closed_set:
                nodes_skipped += 1
                continue

            temp_g = current_g + 1

            if temp_g < neighbor.g:
                neighbor.came_from = current
                neighbor.g = temp_g
                heapq.heappush(open_set, (temp_g, neighbor.get_pos(), neighbor))  # Using position as secondary key

    return nodes_traversed, 0, nodes_skipped, False  # No path exists

def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def a_star_non_graphical(grid, start, end):
    open_set = []
    count = 0
    nodes_traversed = 0
    nodes_skipped = 0

    heapq.heappush(open_set, (0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid.grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid.grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())
    open_set_hash = {start}
    
    while open_set:
        current = heapq.heappop(open_set)[2]
        open_set_hash.remove(current)
        nodes_traversed += 1

        if current == end:
            path_length = 0
            while current in came_from:
                current = came_from[current]
                path_length += 1
            return nodes_traversed, path_length, nodes_skipped, True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    heapq.heappush(open_set, (f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
            else:
                nodes_skipped += 1

    return nodes_traversed, 0, nodes_skipped, False  # If no path is found

def bfs_non_graphical(grid, start, end):
    queue = deque([start])
    visited = set([start])
    nodes_traversed = 0
    nodes_skipped = 0

    while queue:
        current = queue.popleft()
        nodes_traversed += 1

        if current == end:
            path_length = reconstruct_path_non_graphical(current)
            return nodes_traversed, path_length, nodes_skipped, True

        for neighbor in current.neighbors:
            if neighbor not in visited:
                neighbor.came_from = current
                queue.append(neighbor)
                visited.add(neighbor)
            else:
                nodes_skipped += 1

    return nodes_traversed, 0, nodes_skipped, False

def reconstruct_path_non_graphical(end):
    current = end
    path_length = 0
    while current.came_from:
        current = current.came_from
        path_length += 1
    return path_length

def dfs_non_graphical(grid, start, end):
    stack = [start]
    visited = set([start])
    nodes_traversed = 0
    nodes_skipped = 0

    while stack:
        current = stack.pop()
        nodes_traversed += 1

        if current == end:
            path_length = reconstruct_path_non_graphical(current)
            return nodes_traversed, path_length, nodes_skipped, True

        for neighbor in current.neighbors:
            if neighbor not in visited:
                neighbor.came_from = current
                stack.append(neighbor)
                visited.add(neighbor)
            else:
                nodes_skipped += 1

    return nodes_traversed, 0, nodes_skipped, False
