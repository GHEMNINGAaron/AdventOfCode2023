with open('../puzzle_Input1_Day1.txt', 'r') as file:
    words1 = file.readlines()
    words1 = [word.replace('\n', '') for word in words1]

with open('../input.txt', 'r') as file:
    words2 = file.readlines()
    words2 = [word.replace('\n', '') for word in words2]

def digitsInWord(word):
    word = numbersInWordToDigits(word)
    digits_in_word = [c for c in word if c.isdigit()]
    return int(digits_in_word[0] + digits_in_word[-1])


def numbersInWordToDigits(word):
    numbers = {
        "nine": 9,
        "eight": 8,
        "seven": 7,
        "six": 6,
        "five": 5,
        "four": 4,
        "three": 3,
        "two": 2,
        "one": 1,
        "zero": 0,
    }


    #for key, value in numbers.items():
        #word = word.replace(key, str(value))

    mot = ""
    result = ""
    for c in word:
        mot += c
        for key, value in numbers.items():
            if mot.endswith(key):
                result += mot[:-len(key)] + str(value)
                mot = mot[-1]
                break
    result += mot

    return result


def calibrationValue(words):
    calibration = 0
    for word in words:
        calibration += digitsInWord(word)

    return calibration


print(calibrationValue(words2))
