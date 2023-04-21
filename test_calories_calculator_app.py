"""
Test Calories Calculator Application

NAME: Yijing Wu
SEMESTER: Spring 2023
"""
import itertools
from calories_calculator_app import (get_info, check_sex,
check_age, check_height, check_weight, calculate_bmr, load_food,
recipe, print_recipe)

foods = {12: 'Cabbage',
        28: 'Broccoli',
        18: 'Lettuce',
        44: 'Carrot',
        96: 'Corn',
        58: 'Apple',
        46: 'Orange',
        60: 'Banana',
        70: 'Grapes',
        32: 'Watermelon',
        45: 'Mango',
        75: 'Avocado',
        181: 'Ham',
        331: 'Roast Pork',
        520: 'Sausage',
        324: 'Fried Chicken Wing',
        131: 'Tuna',
        99: 'Boiled Shrimp',
        148: 'Boiled Egg',
        236: 'Fried Egg',
        366: 'White Rice',
        124: 'Spaghetti',
        455: 'Instant Noodles'}

def test_get_info():
    """Tests get_info"""
    tuple1 = ('male', 21, 180, 70)
    tuple2 = get_info()  # will prompt, enter male, 21, 180, 70 in order
    if tuple2 != tuple1:
        print("failed test_get_info!")
        return True
    return False


def test_check_sex():
    """Tests check_sex"""
    str1 = 'female'
    str2 = check_sex('  female ')
    if str2 != str1:
        print("failed test_check_sex!")
        return True
    return False


def test_check_age():
    """Tests check_age"""
    int1 = 120
    int2 = check_age(' 120 ')
    if int2 != int1:
        print("failed test_check_age!")
        return True
    return False


def test_check_height():
    """Tests check_height"""
    float1 = 0
    float2 = check_height(' 0 ')
    if float2 != float1:
        print("failed test_check_height!")
        return True
    return False


def test_check_weight():
    """Tests check_weight"""
    float1 = 540.00
    float2 = check_weight(' f ')  # will prompt, then enter 540
    if float2 != float1:
        print("failed test_check_weight!")
        return True
    return False


def test_calculate_bmr():
    """Tests calculate_bmr"""
    int1 = 1726
    int2 = calculate_bmr(("male", 21, 180.0, 70.0))
    if int2 != int1:
        print("failed test_calculate_bmr!")
        return True
    return False


def test_load_food():
    """Tests load_food"""
    file1 = foods
    file2 = load_food("foods.csv")
    if file2 != file1:
        print("failed test_load_food!")
        return True
    return False


def test_recipe():
    """Tests recipe"""
    tuple1 = ('Lettuce', 'Corn', 'Sausage', 'White Rice')
    tuple2 = recipe(1000, foods)
    if tuple2 != tuple1:
        print("failed test_recipe!")
        return True
    return False


def test_print_recipe():
    """Tests print_recipe"""
    print_recipe(1000, ('Lettuce', 'Corn', 'Sausage', 'White Rice'))


def main():
    counter = 0
    if test_get_info():
        counter += 1
    if test_check_sex():
        counter += 1
    if test_check_age():
        counter += 1
    if test_check_height():
        counter += 1
    if test_check_weight():
        counter += 1
    if test_load_food():
        counter += 1
    if test_calculate_bmr():
        counter += 1
    if test_recipe():
        counter += 1
    test_print_recipe()
    print(f"Failed: {counter} tests.")
    

main()
