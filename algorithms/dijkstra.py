import pygame
import time

def dijkstra(draw, grid, start, end):
    start_time = time.perf_counter()  # Start timing
    count = 0
    open_set = [start]
    nodes_traversed = 0
    nodes_skipped = 0

    # Initialize g values for all nodes
    for row in grid.grid:
        for node in row:
            node.g = float('inf')  # Set all g values to infinity
    start.g = 0  # The cost to move from the start to itself is 0

    while open_set:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = min(open_set, key=lambda node: node.g)
        open_set.remove(current)
        nodes_traversed += 1

        if current == end:
            path_length = 0
            while current.came_from:
                current = current.came_from
                current.make_path()
                draw()
                path_length += 1
            end.make_end()
            end_time = time.perf_counter()
            time_taken = end_time - start_time
            return time_taken, nodes_traversed, path_length, nodes_skipped, True

        current.make_closed()

        for neighbor in current.neighbors:
            if neighbor.is_barrier() or neighbor.is_closed():
                nodes_skipped += 1
                continue
            temp_g = current.g + 1  # Every edge has a weight of 1 in this context

            if temp_g < neighbor.g:
                neighbor.came_from = current
                neighbor.g = temp_g
                if neighbor not in open_set:
                    open_set.append(neighbor)
                    neighbor.make_open()

        draw()

    end_time = time.perf_counter()
    time_taken = end_time - start_time
    return time_taken, nodes_traversed, 0, nodes_skipped, False  # No path exists
