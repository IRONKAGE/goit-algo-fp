import turtle

def binary_fractal_tree(t, branch_len, angle, level):
    if level == 0:
        return

    t.forward(branch_len)
    pos = t.position()
    heading = t.heading()

    # Рекурсивний виклик для правої гілки
    t.right(angle)
    binary_fractal_tree(t, branch_len * 0.75, angle, level - 1)
    t.penup()
    t.goto(pos)
    t.setheading(heading)
    t.pendown()

    # Рекурсивний виклик для лівої гілки
    t.left(angle)
    binary_fractal_tree(t, branch_len * 0.75, angle, level - 1)
    t.penup()
    t.goto(pos)
    t.setheading(heading)
    t.pendown()

# Приклад використання:
def render_tree_scene():
    try:
        recursion_level = int(input("Введіть бажаний рівень рекурсії (наприклад, 7-10): "))
    except ValueError:
        print("Невірний ввід. Використовується рівень за замовчуванням: 9")
        recursion_level = 9

    # Налаштування вікна та черепашки
    screen = turtle.Screen()
    screen.setup(width=800, height=700)
    screen.bgcolor("white")
    screen.title(f"Бінарне фрактальне дерево (Рівень {recursion_level})")

    t = turtle.Turtle()
    t.speed("fastest")
    t.color("#9A162B")
    t.pensize(2)
    t.penup()
    t.goto(0, -280)
    t.setheading(90)
    t.pendown()
    binary_fractal_tree(t, 100, 35, recursion_level)
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    render_tree_scene()
