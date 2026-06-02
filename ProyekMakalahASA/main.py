# Nama : Gregorius Septiano Ariadi
# NIM : 24060124120026

import matplotlib.pyplot as plt
from skenario import grid1, grid2, grid3, grid4, grid5, grid6, scenarios, start, goal, draw_grid
from dijkstra import dijkstra
from ucs import ucs
from gbfs import gbfs
from astar import astar
from brute_force import brute_force

algorithms = {
    "Dijkstra": dijkstra,
    "UCS": ucs,
    "GBFS": gbfs,
    "A*": astar,
    "Brute Force": brute_force
}

for scenario_name, grid in scenarios.items():
    print("\n")
    print("=" * 60)
    print("SKENARIO:")
    print(scenario_name)
    print("=" * 60)

    for algo_name, algo_func in algorithms.items():
        result = algo_func(grid, start, goal)
        print("\n")
        print("ALGORITMA:", algo_name)

        if result and result["path"]:
            print("Panjang Path:", len(result["path"]))
            print("Node Dikunjungi:", result["nodes"])
            print("Waktu Eksekusi:", result["time"])
        else:
            print("Path tidak ditemukan")

algorithms = {
    "Dijkstra": dijkstra,
    "UCS": ucs,
    "GBFS": gbfs,
    "A*": astar,
    "Brute Force": brute_force
}

selected_grid = grid5 # untuk memilih grid mana yang ingin ditampilkan visualisasinya
for algo_name, algo_func in algorithms.items():
    print("\n")
    print("=" * 50)
    print("VISUALISASI")
    print(algo_name)
    print("=" * 50)
    result = algo_func(selected_grid, start, goal)

    if result and result["path"]:
        print("Panjang Path:", len(result["path"]))
        print("Node Dikunjungi:", result["nodes"])
        print("Waktu Eksekusi:", result["time"])
        draw_grid(selected_grid, result["path"], algo_name)
    else:
        print("Path tidak ditemukan")

algorithms_name = [
    "Dijkstra",
    "UCS",
    "GBFS",
    "A*",
    "Brute Force"
]

times = []
for algo in algorithms_name:
    if algo == "Dijkstra":
        result = dijkstra(grid5, start, goal)
    elif algo == "UCS":
        result = ucs(grid5, start, goal)
    elif algo == "GBFS":
        result = gbfs(grid5, start, goal)
    elif algo == "A*":
        result = astar(grid5, start, goal)
    elif algo == "Brute Force":
        result = brute_force(grid5, start, goal)

    if result and "time" in result:
        times.append(result["time"])
    else:
        times.append(0)

plt.figure(figsize=(10,5))
plt.bar(algorithms_name, times)
plt.title("Perbandingan Waktu Eksekusi Semua Algoritma")
plt.xlabel("Algoritma")
plt.ylabel("Waktu Eksekusi (detik)")
plt.show()