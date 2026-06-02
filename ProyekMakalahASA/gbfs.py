# Nama : Gregorius Septiano Ariadi
# NIM : 24060124120026

import heapq
import time
from skenario import heuristic, get_neighbors, reconstruct_path

def gbfs(grid, start, goal):
    start_time = time.time()
    pq = []
    heapq.heappush(pq, (heuristic(start, goal), start))

    visited = set()
    parent = {}
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
            if neighbor not in visited:
                parent[neighbor] = current
                priority = heuristic(neighbor, goal)
                heapq.heappush(pq, (priority, neighbor))
    return None