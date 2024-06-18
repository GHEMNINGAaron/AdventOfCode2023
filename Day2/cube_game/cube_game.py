from pygments.lexer import words

with open('../puzzle_Input_Day2.txt', 'r') as file:
    words1 = [word.replace('\n', '') for word in file.readlines()]


def transform_game_in_dictionary(game):
    game = game.replace('Game ', "")

    game = game.split(":")
    dict_game = {int(game[0]): game[1].split(";")}

    values = []
    for i in range(len(dict_game[int(game[0])])):
        val = dict_game[int(game[0])][i].split(",")
        val = [c.replace(" ", "") for c in val]
        print(val)
        val = {"".join(filter(str.isalpha, c)): int("".join(filter(str.isdigit, c))) for c in val}
        print(val)
        values.append(val)

    dict_game[int(game[0])] = values
    return dict_game


print(transform_game_in_dictionary("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"))


def verifiy_numbers_of_cube(dict):
    limits_value = {'blue': 14, 'green': 13, 'red': 12}
    valeur = next(iter(dict.values()))

    for i in range(len(valeur)):
        key = [keys for keys in valeur[i] if keys in limits_value.keys()]
        for key in key:
            if valeur[i][key] > limits_value[key]:
                return False

    return True

def sum_of_id_of_possible_games(words):

    sum = 0
    for word in words:
        dict = transform_game_in_dictionary(word)
        if verifiy_numbers_of_cube(dict):
            sum += int(next(iter(dict.keys())))

    return sum


def fewest_number_of_cubes(dict):
    fewest = {"blue": 0, "green": 0, "red": 0}
    valeur = next(iter(dict.values()))
    for i in range(len(valeur)):
        key = [keys for keys in valeur[i] if keys in fewest.keys()]
        for key in key:
            if valeur[i][key] > fewest[key]:
                fewest[key] = valeur[i][key]
    return fewest


def sum_of_power_of_a_set_of_games(words):

    sum=0
    for word in words:
        power = 1
        dict = transform_game_in_dictionary(word)
        fewest = fewest_number_of_cubes(dict)
        for fewest_value in fewest.values():
            power *= fewest_value
        sum += power
    return sum


