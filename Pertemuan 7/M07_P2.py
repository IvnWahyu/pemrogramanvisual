import numpy as np
import matplotlib.pyplot as plt

# Titik a dan b
xa, ya = 100, 200
xb, yb = 1800, 200

# Persamaan SPL-1
my = (yb - ya) / (xb - xa)

# Ukuran gambar
width, height = 2000, 600

# Inisialisasi gambar dengan background putih
gambar = np.ones((height, width, 3), dtype=np.uint8) * 255

# Fungsi untuk menggambar titik pada gambar
def draw_point(x, y, color=(0, 0, 0)):
    gambar[y, x] = color

# Fungsi untuk menggambar garis
def draw_line(x1, y1, x2, y2, color=(0, 0, 0)):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    p = 2 * dy - dx
    x, y = x1, y1
    while x <= x2:
        draw_point(x, y, color)
        x += 1
        if p < 0:
            p = p + 2 * dy
        else:
            y += 1
            p = p + 2 * (dy - dx)

# Gambar titik a dan b
draw_point(xa, ya)
draw_point(xb, yb)

# Gambar garis g
x = xa
while x <= xb:
    y = int(my * (x - xa) + ya)
    draw_point(x, y, (255, 0, 0))
    x += 1

# Tampilkan gambar
plt.imshow(gambar)
plt.show()
