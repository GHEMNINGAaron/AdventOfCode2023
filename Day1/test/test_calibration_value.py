import pytest

from Day1.calibration.calibration_value import (calibrationValue, digitsInWord,
                                                numbersInWordToDigits)

def test_numbersInWordToDigits():
    assert numbersInWordToDigits("two1nine") == "219"
    assert numbersInWordToDigits("eightwothree") == "8wo3"
    assert numbersInWordToDigits("zoneight234") == "z1ight234"
    assert numbersInWordToDigits("7pqrstsixteen") == "7pqrst6teen"

def test_digitsInWord1():
    assert digitsInWord("1abc2") == 12
    assert digitsInWord("pqr3stu8vwx") == 38


def test_calibration_value1():
    assert calibrationValue(["1abc2", "pqr3stu8vwx",
                             "a1b2c3d4e5f", "treb7uchet"]) == 142
    assert calibrationValue(["two1nine", "eightwothree",
                             "abcone2threexyz", "xtwone3four",
                             "4nineeightseven2", "zoneight234",
                             "7pqrstsixteen"]) == 281