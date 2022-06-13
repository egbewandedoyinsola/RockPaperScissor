import random
player_input = ""

choices = ["R", "P", "S"]

cpu_answer = random.choice(choices)


def repeat():
    global player_input
    player_input = input(
        "select R for rock, S for scissors, P for paper:").upper() # players can enter the right option in any case of their choice


repeat()

while player_input not in choices:
    print("Error:Kindly select the right option\n")

    repeat()
    #When there is a tie program must repeat
else:
    while(player_input == cpu_answer):
        print("Player {} : CPU {}".format(player_input, cpu_answer))

        print("There is a tie!!!")

        repeat()
        #lets play the game and figure out the winner
    else:
        # Rock beats Scissors
        if(player_input == "R" and cpu_answer == "S"):
            print("Player {} : CPU {}".format(player_input, cpu_answer))
            print("Player wins!!!")
            # rock beats Scissors
        elif(player_input == "S" and cpu_answer == "R"):
            print("Player {} : CPU {}".format(player_input, cpu_answer))
            print("CPU wins!!!")
            # Scissors beats Paper
        elif(player_input == "P" and cpu_answer == "S"):
            print("Player  {} : CPU {}".format(player_input, cpu_answer))
            print("CPU wins!!!")

            # Scissors beats paper
        elif(player_input == "S" and cpu_answer == "P"):
            print("Player {} : CPU  {}".format(player_input, cpu_answer))
            print("Player wins!!!")
            # Paper beats Rock
        elif(player_input == "P" and cpu_answer == "R"):
            print("Player {} : CPU  {}".format(player_input, cpu_answer))
            print("Player wins!!!")
            # Rock beats Scissors
        elif(player_input == "R" and cpu_answer == "S"):
            print("Player  {} : CPU {}".format(player_input, cpu_answer))
            print("CPU wins!!!")
