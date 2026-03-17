import heapq  # To get the node with the lowest f-score from open_set
import pygame
import time

def h(p1, p2):
    # Heuristic function: Manhattan distance
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(came_from, current, draw_func):
    while current in came_from:
        current = came_from[current]
        current.set_path()
        draw_func()

def a_star_algorithm(draw_func, grid, start, end):
    start_time = time.perf_counter()  # Start timing
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
                current.set_path()
                draw_func()
                path_length += 1
            end.set_end()
            end_time = time.perf_counter()
            time_taken = end_time - start_time
            return time_taken, nodes_traversed, path_length, nodes_skipped, True

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
                    neighbor.set_open()
            else:
                nodes_skipped += 1

        draw_func()

        if current != start:
            current.set_visited()

    end_time = time.perf_counter()
    time_taken = end_time - start_time
    return time_taken, nodes_traversed, 0, nodes_skipped, False  # If no path is found
