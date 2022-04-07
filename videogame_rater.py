#
# videogame_rater.py
# Rates video games
#
# KJ
# 08/04


def print_dictionary(dictionary):
    """ Accepts a Dictionary and loops through it and prints the keys and values (games and rating)"""
    for game, rating in dictionary.items():
        print("{} has a {} out of 5 stars rating".format(game, rating))


if __name__ == "__main__":
    videogames = {"Minecraft":5, "Call of Duty":1, "Angry Birds":4, "Splatoon 2":5, "Animal Crossing":4,}

    print_dictionary(videogames)
