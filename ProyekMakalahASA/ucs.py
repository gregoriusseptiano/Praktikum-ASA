# Nama : Gregorius Septiano Ariadi
# NIM : 24060124120026

import heapq
import time
from skenario import heuristic, get_neighbors, reconstruct_path

def ucs(grid, start, goal):
    start_time = time.time()
    pq = []
    heapq.heappush(pq, (0, start))
    visited = set()
    parent = {}
    distance = {start: 0}
    nodes = 0

    while pq:
        current_cost, current = heapq.heappop(pq)
        if current in visited:
            continue
        visited.add(current)
        nodes += 1

        if current == goal:
            end_time = time.time()
            path = reconstruct_path(parent, start, goal)
            return {
                "path": path,
                "cost": current_cost,
                "nodes": nodes,
                "time": end_time - start_time}

        for neighbor in get_neighbors(current, grid):
            new_cost = current_cost + 1
            if neighbor not in distance or new_cost < distance[neighbor]:
                distance[neighbor] = new_cost
                parent[neighbor] = current
                heapq.heappush(pq, (new_cost, neighbor))
    return None