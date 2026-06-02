# Nama : Gregorius Septiano Ariadi
# NIM : 24060124120026

import heapq
import time
from skenario import heuristic, get_neighbors, reconstruct_path

def astar(grid, start, goal):
    start_time = time.time()
    pq = []
    heapq.heappush(pq, (0, start))
    parent = {}
    g_cost = {start: 0}
    visited = set()
    nodes = 0

    while pq:
        _, current = heapq.heappop(pq)
        if current in visited:
            continue
        visited.add(current)
        nodes += 1

        if current == goal:
            end_time = time.time()
            path = reconstruct_path(parent, start, goal)
            return {
                "path": path,
                "nodes": nodes,
                "time": end_time - start_time}

        for neighbor in get_neighbors(current, grid):
            tentative_g = g_cost[current] + 1
            if (neighbor not in g_cost or
                tentative_g < g_cost[neighbor]):
                g_cost[neighbor] = tentative_g
                f = tentative_g + heuristic(neighbor, goal)
                parent[neighbor] = current
                heapq.heappush(pq, (f, neighbor))
    return None