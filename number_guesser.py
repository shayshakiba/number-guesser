from math import ceil, log2


def print_empty_line():
    print()


def greet_user():
    print("Hello there!")
    print("Let's play a game!")
    print_empty_line()


def give_game_instructions():
    print("First, choose a range of numbers.")
    print("Next, think of a number in your mind which is within that range.")
    print("Then, I'll try to guess your number.")
    print_empty_line()


def farewell_user():
    print("Take care!")
    print_empty_line()


def input_minimum_number():
    while True:
        try:
            value = int(input("The minimum number: "))
        except ValueError:
            print("Invalid Input: Please enter an integer!")
            continue

        print_empty_line()
        break

    return value


def input_maximum_number(minimum_number):
    while True:
        try:
            value = int(input("The maximum number: "))
        except ValueError:
            print("Invalid Input: Please enter an integer!")
            continue

        if minimum_number >= value:
            print(
                "Invalid Input: Your maximum number have to be greater than your minimum number!"
            )
            continue

        print_empty_line()
        break

    return value


def check_guess(guess, number_of_guesses):
    print(
        f"Guess {number_of_guesses}: Is {guess} less than, more than, or equal to your number? "
    )

    while True:
        response = input("Response: ").lower()

        if response in ["m", "more"]:
            response = 1
        elif response in ["l", "less"]:
            response = -1
        elif response in ["e", "equal"]:
            response = 0
        else:
            print("Invalid Input: Please enter '(m)ore', '(l)ess', or '(e)qual'!")
            continue

        print_empty_line()
        break

    return response


def play_one_round():
    min = input_minimum_number()
    max = input_maximum_number(min)

    print(f"I'll guess your number in {ceil(log2(max - min + 1)) + 1} steps or less.")
    print("Let's start...")
    print_empty_line()

    number_of_guesses = 0

    while True:
        if min > max:
            print("No such number exists! Are you cheating?")
            print_empty_line()
            break

        guess = (min + max) // 2
        number_of_guesses += 1

        guess_status = check_guess(guess, number_of_guesses)

        if guess_status == 1:
            max = guess - 1
        elif guess_status == -1:
            min = guess + 1
        else:
            print("Yeahhh!")
            print_empty_line()
            break


def user_wants_to_play_again():
    print("Do you want to play again?")

    while True:
        response = input("Reponse: ").lower()

        if response in ["y", "yes"]:
            response = True
        elif response in ["n", "no"]:
            response = False
        else:
            print("Invalid Input: Please enter '(y)es' or '(n)o'!")
            continue

        print_empty_line()
        break

    return response


def play():
    while True:
        play_one_round()

        if not user_wants_to_play_again():
            break


def main():
    greet_user()

    give_game_instructions()

    play()

    farewell_user()


if __name__ == "__main__":
    main()
