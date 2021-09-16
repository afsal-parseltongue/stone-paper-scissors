import random

print("\nWelcome to stone paper scissor game")

name = input("\nPlease enter your name: ")

valid_entries = ['st', 'pa', 'sc']

choice_name_map = {
    "st": "Stone",
    "pa": "Paper",
    "sc": "Scissor"
}


def start_game():
    while True:
        user_score = 0
        cpu_score = 0
        print("\nHi {} let start the play".format(name))
        print("Instruction: Please enter\n \t st for stone\n \t pa for paper \n \t sc for scissors")
        while user_score <5 and cpu_score <5:
            entry = input("\nPlease enter your choice: ")
            while not entry in valid_entries:
                entry = input("\nPlease enter your choice: ")
            cpu_entry = random.choices(valid_entries)[0]
            print("Cpu show a {}".format(choice_name_map[cpu_entry]))
            if entry == "st":
                if cpu_entry == "st":
                    print("Tie")
                elif cpu_entry == "pa":
                    print("cpu get one point")
                    cpu_score += 1
                else:
                    print("you get one point")
                    user_score += 1
            elif entry == "pa":
                if cpu_entry == "st":
                    print("you get one point")
                    user_score += 1
                elif cpu_entry == "pa":
                    print("Tie")
                else:
                    print("cpu get one point")
                    cpu_score += 1
            else:
                if cpu_entry == "st":
                    print("cpu get one point")
                    cpu_score += 1
                elif cpu_entry == "pa":
                    print("you get one point")
                    user_score += 1
                else:
                    print("tie")
        if user_score == 5:
            print("You win")
        else:
            print("\nCpu win")

        want_to_continue = input("Enter y to continue else press any key")
        if not want_to_continue in ["y", "Y"]:
            break


if __name__ == "__main__":
    start_game()

