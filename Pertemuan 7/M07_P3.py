import numpy as np
import matplotlib.pyplot as plt

# Titik a dan b
xa, ya = 100, 200
xb, yb = 100, 1000

# Persamaan SPL-2
mx = (xb - xa) / (yb - ya)

# Ukuran gambar
width, height = 1200, 1200

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

# Gambar titik a dan b
draw_point(xa, ya)
draw_point(xb, yb)

# Gambar garis g
y = ya
while y <= yb:
    x = int(mx * (y - ya) + xa)
    draw_point(x, y, (255, 0, 0))
    y += 1

# Tampilkan gambar
plt.imshow(gambar)
plt.show()
