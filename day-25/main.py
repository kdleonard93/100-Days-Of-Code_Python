import turtle
import pandas as pd


def write_state(turtle, state_name, x, y):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x, y)
    turtle.write(state_name)


def main():
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)

    data = pd.read_csv("50_states.csv")
    all_states = data.state.to_list()
    guessed_states = []

    while len(guessed_states) < 50:
        answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                        prompt="What's another state's name?").title()
        if answer_state == "Exit":
            missing_states = [
                state for state in all_states if state not in guessed_states]
            pd.DataFrame(missing_states).to_csv("states_to_learn.csv")
            break

        if answer_state in all_states and answer_state not in guessed_states:
            guessed_states.append(answer_state)
            state_data = data[data.state == answer_state]
            write_state(turtle.Turtle(), answer_state,
                        int(state_data.x), int(state_data.y))


if __name__ == "__main__":
    main()
