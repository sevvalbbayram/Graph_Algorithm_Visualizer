from collections import deque
import time

def bfs(draw_func, grid, start, end):
    start_time = time.perf_counter()  # Start timing
    queue = deque([start])
    visited = set([start])
    nodes_traversed = 0
    nodes_skipped = 0  # Initialize count of skipped nodes

    while queue:
        current = queue.popleft()
        nodes_traversed += 1  # Increment nodes traversed count

        if current == end:
            path_length, skipped_nodes = reconstruct_path(current, visited, draw_func)
            end_time = time.perf_counter()  # End timing
            time_taken = end_time - start_time  # Calculate time taken
            return time_taken, nodes_traversed, path_length, nodes_skipped, True  # Return statistics along with the success flag

        for neighbor in current.neighbors:
            if neighbor not in visited:
                neighbor.came_from = current
                queue.append(neighbor)
                visited.add(neighbor)
                neighbor.set_open()
            else:
                nodes_skipped += 1  # Increment skipped nodes count if already visited

        draw_func()

        if current != start:
            current.set_visited()

    end_time = time.perf_counter()  # End timing for cases where the path is not found
    time_taken = end_time - start_time  # Calculate time taken
    return time_taken, nodes_traversed, 0, nodes_skipped, False  # Return statistics along with the failure flag

def reconstruct_path(end, visited, draw_func):
    current = end
    path_length = 0
    while current.came_from:
        current = current.came_from
        current.set_path()
        draw_func()
        path_length += 1
    return path_length, len(visited) - path_length # Return the length of the path and skipped nodes
