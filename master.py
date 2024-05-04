import turtle
import time
import random

# Screen dimension constants
WIDTH, HEIGHT = 700, 600
# List containing potential turtle colors
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


def get_number_of_racers():
    """Prompts the user to enter the number of racers and ensures it is between 2 and 10."""
    while True:
        try:
            racers = int(
                input("Enter the number of racers (2 - 10): ")
            )  # Get user input for the number of racers
            if 2 <= racers <= 10:  # Check if the number of racers is between 2 and 10
                return racers
            else:
                print(
                    "Number not in range 2-10. Try Again!"
                )  # Print error if number not in range
        except ValueError:
            print(
                "Input is not a number. Try Again!"
            )  # Handle the error when input is not a number


def race(colors, turtles):
    """Runs the race and returns the color of the winning turtle."""
    while True:
        for racer in turtles:  # Loop through each turtle
            distance = random.randrange(1, 20)  # Random distance for the turtle to move
            racer.forward(distance)  # Move the turtle forward by 'distance'

            _, y = racer.pos()  # Get y-coordinate of the turtle
            if y >= HEIGHT // 2 - 10:  # Check if the turtle crosses the finish line
                winner_color = colors[
                    turtles.index(racer)
                ]  # Determine the color of the winning turtle
                break
        else:
            continue  # Continue if no turtle has won yet
        break
    return winner_color


def create_turtles():
    """Creates and positions turtles based on the number of racers and returns a list of turtles."""
    turtles = []  # List to store turtle objects
    spacingx = WIDTH // (
        len(COLORS) + 1
    )  # Calculate horizontal spacing between turtles
    for i, color in enumerate(COLORS):  # Create and position each turtle
        racer = turtle.Turtle()  # Create a new turtle object
        racer.color(color)  # Set the color of the turtle
        racer.shape("turtle")  # Set the shape of turtle
        racer.left(90)  # Rotate turtle to face upwards
        racer.penup()  # Lift the pen so the turtle does not draw
        x_pos = -WIDTH // 2 + (i + 1) * spacingx  # Calculate x position for the turtle
        y_pos = -HEIGHT // 2 + 20  # y position for turtle at starting line
        racer.setpos(x_pos, y_pos)  # Set the position of the turtle
        racer.pendown()  # Place the pen down to start drawing when moving
        turtles.append(racer)  # Add the turtle to the list of turtles
    return turtles


def init_game_environment():
    """Initializes the Turtle graphics window with specific dimensions and a title."""
    screen = turtle.Screen()  # Create a new screen object
    screen.setup(WIDTH, HEIGHT)  # Set the width and height of the screen
    screen.title("Shell_Speed")  # Set the title of the screen
    screen.bgcolor("white")  # Set the background color of the screen


# Main execution block
try:
    racers = get_number_of_racers()  # Get the total number of racers from the user
    init_game_environment()  # Initialize the game environment

    random.shuffle(COLORS)  # Randomly shuffle the colors
    colors = COLORS[:racers]  # Select the first 'racers' colors

    turtles = create_turtles()  # Create turtles for the race
    winner = race(colors, turtles)  # Start the race and get the winner
    print("The winner is the turtle with color:", winner)  # Output the winner's color
    time.sleep(5)  # Wait for 5 seconds before closing
except Exception as e:
    print("An error occurred:", e)  # Print any exceptions that occur during the race
