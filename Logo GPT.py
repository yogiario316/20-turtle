import turtle

# Membuat layar
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Spinning GPT Logo")

# Membuat turtle
pen = turtle.Turtle()
pen.speed(0)  # kecepatan maksimal
pen.color("light blue")

# Fungsi untuk menggambar satu bagian dari logo
def draw_shape():
    for _ in range(6):
        pen.forward(100)
        pen.right(60)
        pen.forward(100)
        pen.right(120)

# Menggambar pola berputar
for i in range(36):
    draw_shape()
    pen.right(10)

# Menyembunyikan turtle
pen.hideturtle()

# Menunggu untuk menutup layar
screen.mainloop()
