import turtle

# Membuat layar
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Turtle Demo")

# Membuat turtle
pen = turtle.Turtle()
pen.speed(5)
pen.color("white")
pen.pensize(2)

# Mengangkat pena dan memindahkan turtle ke posisi awal di sebelah kiri atas
pen.penup()
pen.goto(-340, 150)
pen.pendown()

# Fungsi untuk menggambar bintang
def draw_star(size):
    for _ in range(5):
        pen.forward(size)
        pen.right(144)

# Menggambar beberapa bintang dengan warna berbeda
colors = ["red", "blue", "green", "yellow", "purple", "pink", "grey"]
size = 30
stars_per_row = 7
rows = 5

for row in range(rows):
    for color in colors:
        pen.color(color)
        draw_star(size)
        pen.penup()
        pen.right(90)  # Pindah ke bawah
        pen.forward(2 * size)  # Jarak vertikal antar bintang
        pen.left(70)
        pen.pendown()
    # Pindah ke posisi awal untuk baris berikutnya
    pen.penup()
    pen.goto(pen.xcor() + 180, 100)
    pen.pendown()


# Menyembunyikan turtle
pen.hideturtle()

# Menunggu untuk menutup layar
screen.mainloop()
