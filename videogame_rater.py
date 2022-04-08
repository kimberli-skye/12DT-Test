#
# videogame_rater.py
# Rates video games
#
# KJ
# 08/04


def print_dictionary(dictionary):
    """ Accepts a Dictionary and loops through it and prints the keys and values (games and rating)"""
    for ID, game in dictionary.items():
        print("ID = {}, {} has a {} out of 5 stars rating".format(ID, game["name"], game["rating"]))

    



if __name__ == "__main__":
    videogames = {1:{"name":"Minecraft", "rating":5},
                              2:{"name":"Call of Duty", "rating":1},
                              3:{"name":"Angry Birds", "rating":4},
                              4:{"name":"Splatoon 2", "rating":5},
                              5:{"name":"Animal Crossing", "rating":4}
                              }

    print_dictionary(videogames)
