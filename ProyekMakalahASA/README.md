# Optimasi Jalur Evakuasi pada Grid — Perbandingan Algoritma Pencarian

**Proyek Makalah Analisis dan Strategi Algoritma 2025/2026**  
S1 Informatika, Fakultas Sains dan Matematika, Universitas Diponegoro

> Nama: Gregorius Septiano Ariadi  
> NIM: 24060124120026

---

## Deskripsi

Proyek ini membandingkan lima algoritma pencarian jalur pada grid 10×10 dengan hambatan (rintangan). Masalah dimodelkan sebagai pencarian jalur terpendek dari titik `(0,0)` ke titik `(9,9)`, di mana `0` adalah sel yang bisa dilewati dan `1` adalah dinding/penghalang.

Setiap algoritma diuji pada **6 skenario grid** yang berbeda tingkat kesulitannya, lalu dibandingkan berdasarkan panjang jalur, jumlah node yang dikunjungi, dan waktu eksekusi.

### Algoritma yang Dibandingkan

| No | Algoritma | Jenis | Karakteristik |
|----|-----------|-------|---------------|
| 1 | Dijkstra | Uninformed | Menjamin jalur terpendek, eksplorasi berdasarkan biaya kumulatif |
| 2 | UCS (Uniform Cost Search) | Uninformed | Identik dengan Dijkstra pada bobot seragam |
| 3 | GBFS (Greedy Best-First Search) | Informed | Cepat, dipandu heuristik Manhattan, tidak selalu optimal |
| 4 | A* | Informed | Gabungan biaya nyata + heuristik, optimal dan efisien |
| 5 | Brute Force | Exhaustive | DFS lengkap mencari semua jalur, menjamin optimal tapi lambat |

---

## Struktur File

```
ProyekMakalahASA/
├── main.py          # Entry point: menjalankan semua skenario, visualisasi, dan grafik perbandingan
├── skenario.py      # Definisi 6 grid skenario, fungsi draw_grid, get_neighbors, heuristic, reconstruct_path
├── dijkstra.py      # Algoritma Dijkstra
├── ucs.py           # Algoritma Uniform Cost Search
├── gbfs.py          # Algoritma Greedy Best-First Search
├── astar.py         # Algoritma A*
└── brute_force.py   # Algoritma Brute Force (DFS exhaustive)
```

---

## Cara Menjalankan

### Prasyarat

- Python 3.8 atau lebih baru
- Library `matplotlib`

```bash
pip install matplotlib
```

### Jalankan Program

```bash
python main.py
```

Program akan secara otomatis:
1. Menjalankan semua 5 algoritma pada semua 6 skenario dan mencetak hasilnya di terminal
2. Menampilkan visualisasi jalur untuk setiap algoritma pada **Skenario Hambatan Tinggi** (`grid5`)
3. Menampilkan grafik bar perbandingan waktu eksekusi semua algoritma

---

## Skenario Grid

Semua grid berukuran **10×10**. Start: `(0,0)` (kiri atas), Goal: `(9,9)` (kanan bawah).

| Skenario | Variabel | Deskripsi |
|----------|----------|-----------|
| Normal | `grid1` | Hambatan standar, jalur cukup terbuka |
| Koridor Tertutup | `grid2` | Blok hambatan besar, koridor sempit |
| Jalur Utama Terhalang | `grid3` | Rute langsung diblokir, memaksa detour panjang |
| Hambatan Acak | `grid4` | Rintangan tersebar tidak beraturan |
| Hambatan Tinggi | `grid5` | Kepadatan hambatan tinggi, jalur sangat terbatas |
| Tidak Ada Jalur | `grid6` | Dinding memblokir total, tidak ada jalur ke goal |

---

## Output Program

### Terminal
Untuk setiap kombinasi skenario × algoritma, program mencetak:
- **Panjang Path** — jumlah sel dalam jalur yang ditemukan
- **Node Dikunjungi** — total sel yang dieksplorasi
- **Waktu Eksekusi** — dalam satuan detik

### Visualisasi Grid
Jalur ditampilkan pada grid menggunakan `matplotlib` dengan colormap `viridis`:
- Sel putih = jalur terbuka
- Sel gelap = dinding
- Jalur ditemukan = ditandai warna berbeda
- Start & goal = ditandai khusus

### Grafik Perbandingan
Bar chart waktu eksekusi semua algoritma pada `grid5` (Skenario Hambatan Tinggi).

---

## Catatan Implementasi

- Semua algoritma menggunakan **4-directional movement** (atas, bawah, kiri, kanan — tanpa diagonal)
- Heuristik yang digunakan: **Manhattan Distance** — `|x1-x2| + |y1-y2|`
- Brute Force menggunakan DFS rekursif dengan pruning panjang jalur (berhenti jika sudah melebihi panjang terbaik yang ditemukan)
- Pada skenario `grid6` (Tidak Ada Jalur), semua algoritma akan mengembalikan `None` dan mencetak "Path tidak ditemukan"