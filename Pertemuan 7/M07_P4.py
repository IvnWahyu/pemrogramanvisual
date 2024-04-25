import numpy as np
import matplotlib.pyplot as plt

# Ukuran gambar
width, height = 2000, 1200

# Inisialisasi gambar dengan background putih
gambar = np.ones((height, width, 3), dtype=np.uint8) * 255

# Fungsi untuk menggambar titik pada gambar
def draw_point(x, y, color=(0, 0, 0)):
    gambar[y, x] = color

# Fungsi untuk menggambar garis
def draw_line(x1, y1, x2, y2, color=(0, 0, 0)):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    p = 2 * dx - dy
    x, y = x1, y1
    while y <= y2:
        draw_point(x, y, color)
        y += 1
        if p < 0:
            p = p + 2 * dx
        else:
            x += 1
            p = p + 2 * (dx - dy)

# Titik-titik dan warna garis
points = [(100, 200, 100, 1000, (255, 0, 0)),  # Garis pertama
          (100, 200, 1800, 200, (0, 255, 0)),  # Garis kedua
          (100, 1000, 1800, 200, (0, 0, 255))]  # Garis ketiga

# Gambar ketiga garis
for point in points:
    x1, y1, x2, y2, color = point
    draw_line(x1, y1, x2, y2, color)

# Tampilkan gambar
plt.imshow(gambar)
plt.show()
