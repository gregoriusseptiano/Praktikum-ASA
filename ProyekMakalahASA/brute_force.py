# Nama : Gregorius Septiano Ariadi
# NIM : 24060124120026

import heapq
import time
from skenario import heuristic, get_neighbors, reconstruct_path

def brute_force(grid, start, goal):
    start_time = time.time()
    best_path = None
    best_length = float('inf')
    nodes = 0

    def dfs(current, path, visited):
        nonlocal best_path
        nonlocal best_length
        nonlocal nodes
        nodes += 1

        if len(path) >= best_length:
            return
        if current == goal:
            if len(path) < best_length:
                best_length = len(path)
                best_path = path.copy()
            return

        for neighbor in get_neighbors(current, grid):
            if neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)
                dfs(neighbor, path, visited)
                path.pop()
                visited.remove(neighbor)

    dfs(start, [start], {start})
    end_time = time.time()
    return {
        "path": best_path,
        "nodes": nodes,
        "time": end_time - start_time}