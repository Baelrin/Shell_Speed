import turtle
import time
import random


def get_number_of_racers():
    while True:
        try:
            racers = int(input("Enter the number of racers (2 - 10): "))
            if 2 <= racers <= 10:
                return racers
            else:
                print("Number not in range 2-10. Try Again!")
        except ValueError:
            print("Input is not a number. Try Again!")


def race(colors, turtles):
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            _, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                winner_color = colors[turtles.index(racer)]
                break
        else:
            continue
        break
    return winner_color


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles


def init_turtle():
    global WIDTH, HEIGHT, COLORS  # Используем глобальные переменные внутри функции
    WIDTH, HEIGHT = 700, 600
    COLORS = [
        "red",
        "green",
        "blue",
        "orange",
        "yellow",
        "black",
        "purple",
        "pink",
        "brown",
        "cyan",
    ]
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Shell_Speed")
    screen.bgcolor("white")  # Устанавливаем фоновый цвет


try:
    racers = get_number_of_racers()
    init_turtle()

    random.shuffle(COLORS)
    colors = COLORS[:racers]

    turtles = create_turtles(colors)
    winner = race(colors, turtles)
    print("The winner is the turtle with color:", winner)
    time.sleep(5)
except Exception as e:
    print("An error occurred:", e)
