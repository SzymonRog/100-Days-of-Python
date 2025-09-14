import turtle
import pandas

# setup ekranu
screen = turtle.Screen()
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

screen.title("U.S. States Game")
screen.bgpic("blank_states_img.gif")
screen.setup(width=725, height=491)

# dane
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []

def update_game():
    if len(guessed_states) == 50:
        screen.title("You Win!")
        save_missing_states()
        return

    guess = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?"
    )

    if guess is None or guess.title() == "Exit":
        save_missing_states()
        return

    guess = guess.title()
    if guess in states and guess not in guessed_states:
        state_data = data[data.state == guess]
        guessed_states.append(guess)

        writer.goto(state_data.x.iloc[0], state_data.y.iloc[0])
        writer.write(guess, font=("Arial", 8, "bold"))
    else:
        print(f"{guess} is not valid or already guessed.")

    update_game()

def save_missing_states():
    states_to_learn = [state for state in states if state not in guessed_states]
    new_data = pandas.DataFrame(states_to_learn, columns=["states_to_learn"])
    new_data.to_csv("states_to_learn.csv", index=False)
    print("Missing states saved to states_to_learn.csv")
    screen.bye()  # zamyka okno

# start
update_game()
screen.mainloop()
