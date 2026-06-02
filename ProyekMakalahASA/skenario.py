# Nama : Gregorius Septiano Ariadi
# NIM : 24060124120026

import heapq
import time
import matplotlib.pyplot as plt

start = (0, 0)
goal = (9, 9)

grid1 = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,0,1,1,1,1,0],
    [0,0,0,1,0,0,0,0,1,0],
    [1,1,0,1,0,1,1,0,1,0],    # Skenario Normal
    [0,0,0,0,0,0,1,0,0,0],
    [0,1,1,1,1,0,1,1,1,0],
    [0,0,0,0,1,0,0,0,1,0],
    [0,1,1,0,1,1,1,0,1,0],
    [0,0,0,0,0,0,0,0,1,0],
    [0,1,1,1,1,1,1,0,0,0]
]
grid2 = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,0,1,1,1,1,0],
    [0,1,1,1,0,0,0,0,1,0],
    [0,1,1,1,0,1,1,0,1,0],    # Skenario Koridor Tertutup
    [0,0,0,0,0,0,1,0,0,0],
    [0,1,1,1,1,0,1,1,1,0],
    [0,0,0,0,1,0,0,0,1,0],
    [0,1,1,0,1,1,1,0,1,0],
    [0,0,0,0,0,0,0,0,1,0],
    [0,1,1,1,1,1,1,0,0,0]
]
grid3 = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,1,0],
    [1,1,1,1,1,1,1,0,1,0],    # Skenario Jalur Utama Terhalang
    [0,0,0,0,0,0,1,0,0,0],
    [0,1,1,1,1,0,1,1,1,0],
    [0,0,0,0,1,0,0,0,1,0],
    [0,1,1,0,1,1,1,0,1,0],
    [0,0,0,0,0,0,0,0,1,0],
    [0,1,1,1,1,1,1,0,0,0]
]
grid4 = [
    [0,1,0,0,0,0,1,0,0,0],
    [0,1,0,1,1,0,1,0,1,0],
    [0,0,0,1,0,0,0,0,1,0],
    [1,1,0,1,0,1,1,0,1,0],    # Skenario Hambatan Acak
    [0,0,0,0,0,0,1,0,0,0],
    [0,1,1,1,1,0,1,1,1,0],
    [0,0,0,0,1,0,0,0,1,0],
    [0,1,1,0,1,1,1,0,1,0],
    [0,0,0,0,0,0,0,0,1,0],
    [0,1,1,1,1,1,1,0,0,0]
]
grid5 = [
    [0,1,1,1,0,1,1,1,1,0],
    [0,1,0,1,0,1,0,0,1,0],
    [0,1,0,1,0,1,0,1,1,0],
    [0,0,0,1,0,0,0,1,0,0],    # Skenario Hambatan Tinggi
    [1,1,0,1,1,1,0,1,0,1],
    [0,0,0,0,0,1,0,0,0,0],
    [0,1,1,1,0,1,1,1,1,0],
    [0,0,0,1,0,0,0,0,1,0],
    [1,1,0,1,1,1,1,0,1,0],
    [0,0,0,0,0,0,0,0,0,0]
]
grid6 = [
    [0,1,1,1,1,1,1,1,1,1],
    [0,1,1,1,1,1,1,1,1,1],
    [0,1,1,1,1,1,1,1,1,1],
    [0,1,1,1,1,1,1,1,1,1],    # Skenario Tidak Ada Jalur
    [0,1,1,1,1,1,1,1,1,1],
    [0,1,1,1,1,1,1,1,1,1],
    [0,1,1,1,1,1,1,1,1,1],
    [0,1,1,1,1,1,1,1,1,1],
    [0,1,1,1,1,1,1,1,1,1],
    [0,1,1,1,1,1,1,1,1,0]
]

scenarios = {
    "Normal": grid1,
    "Koridor Tertutup": grid2,
    "Jalur Utama Terhalang": grid3,
    "Hambatan Acak": grid4,
    "Hambatan Tinggi": grid5,
    "Tidak Ada Jalur": grid6
}

def draw_grid(grid, path=None, algo_name="Algoritma"):
    display = []
    for row in grid:
        display.append(row.copy())
    if path:
        for x, y in path:
            display[x][y] = 2
    sx, sy = start
    gx, gy = goal
    display[sx][sy] = 3
    display[gx][gy] = 4
    plt.figure(figsize=(6,6))
    plt.imshow(display, cmap='viridis')
    plt.grid(True, which='both', color='white', linestyle='-', linewidth=0.5)
    plt.title(f"Simulasi Jalur Evakuasi - {algo_name}", fontsize=12, fontweight='bold')
    plt.show()

def get_neighbors(node, grid):
    x, y = node
    neighbors = []
    directions = [
        (-1,0),
        (1,0),
        (0,-1),
        (0,1)]
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if (0 <= nx < len(grid)
            and
            0 <= ny < len(grid[0])
            and
            grid[nx][ny] == 0):
            neighbors.append((nx, ny))
    return neighbors

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def reconstruct_path(parent, start, goal):
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = parent[current]
    path.append(start)
    path.reverse()
    return path