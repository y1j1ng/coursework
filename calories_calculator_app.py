"""
Calories Calculator Application

A program that recommend recipe based on the given file of foods and calories.

NAME: Yijing Wu
SEMESTER: Spring 2023
"""
from typing import List, Tuple, Dict
import itertools

def get_info() -> Tuple[str, float]:
    """
    Gets personal information from the user.

    For Example:
    >>> What is your sex (female / male)? male
        What is your age? 21
        What is your height (cm)? 180
        What is your weight (kg)? 70
    >>> ('male', 21, 180, 70)
    
    Return:
        Tuple[str, int, float, float]
    """
    gender = check_gender(input("What is your sex (female / male)? "))
    age = check_age(input("What is your age? "))
    height = check_height(input("What is your height (cm)? "))
    weight = check_weight(input("What is your weight (kg)? "))
    return gender, age, height, weight


def check_gender(gender: str) -> str:
    """
    Checks whether the input is valid.

    For Example:
    >>> check_gender("F")
        Must be female or male.
        What is your sex (female / male)?   female
    >>> "female"

    Args:
        gender (str)

    Return:
        str
    """
    gender = gender.strip()
    while gender != "female" and gender != "male":
        print("Must be female or male.")
        gender = input("What is your sex (female / male)? ")
        gender = gender.strip()
    return gender


def check_age(age: str) -> int:
    """
    Checks whether the input is valid.

    For Example:
    >>> check_age(' 121 ')
        Must be in the range of 0 - 120.
        What is your age?   120
    >>> 120

    Args:
        age (str)

    Return:
        int
    """
    age = age.strip()
    try:
        age = int(age)
        while age > 120 or age < 0:
            print("Must be in the range of 0 - 120.")
            age = input("What is your age? ")
            age = int(age.strip())
    except ValueError:
        print("Please enter a valid number.")
        age = input("What is your age? ")
        age = check_age(age)
    return age


def check_height(height: str) -> float:
    """
    Checks whether the input is valid.

    For Example:
    >>> check_height(' 261 ')
        Must be in the range of 0 - 260.
        What is your height?   260
    >>> 260.0

    Args:
        height (str)

    Return:
        float
    """
    height = height.strip()
    try:
        height = float(height)
        while height > 260 or height < 0:
            print("Must be in the range of 0 - 260.")
            height = input("What is your height? ")
            height = float(height.strip())
    except ValueError:
        print("Please enter a valid number.")
        height = input("What is your height? ")
        height = check_height(height)
    return height


def check_weight(weight: str) -> float:
    """
    Checks whether the input is valid.

    For Example:
    >>> check_weight(' f ')
        Please enter a valid number.
        What is your weight? 541
        Must be in the range of 0 - 541.
        What is your weight?   540
    >>> 540.0

    Args:
        weight (str)

    Return:
        float
    """
    weight = weight.strip()
    try:
        weight = float(weight)
        while weight > 540 or weight < 0:
            print("Must be in the range of 0 - 540.")
            weight = input("What is your weight? ")
            weight = float(weight.strip())
    except ValueError:
        print("Please enter a valid number.")
        weight = input("What is your weight? ")
        weight = check_weight(weight)
    return weight


def calculate_bmr(info: Tuple[str, float, float, float]) -> int:
    """
    Calculates the BMR based on the Mifflin-St Jeor formula.
    Round the result to integer.
    BMR = 9.99 * weight + 6.25 * height - 4.92 * age
    + (166 * gender (male = 1, female = 0) - 161)

    For Example:
    >>> calculate_bmr(("male", 21, 180.0, 70.0))
        1726

    Args:
        info (tuple): the tuple that contains gender, age, height and weight.

    Return:
        int
    """
    if info[0] == "female":
        sex = 0
    else:
        sex = 1
    bmr = 9.99 * info[3] + 6.25 * info[2] - 4.92 * info[1] + (166 * sex - 161)
    return round(bmr)


def load_food(filename: str) -> Dict[int, str]:
    """
    Loads the food list from the given file and returns a dictionary
    of calories and the corresponding foods.
    data from:
    http://www.totalcare.hk/healthy_diet/healthy_diet-article/calorie-table-eat-food-calories.html/comment-page-10

    Example:
        >>> load_food("foods.csv")
        {12: 'Cabbage',
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

    Args:
        filename (str): The name of the file to load the food list from.

    Returns:
        Dict[str, float]: A dictionary of calories and foods.
    """
    foods = {}
    file = open(filename, "r")
    for line in file:
        position = line.find(",")
        foods[int(line[:position])] = line[position + 1:].strip()
    return foods


def recipe(bmr: int, foods: Dict[int, str]) -> Tuple:
    """
    Generates a daily food plan, which can cover the needed calories.

    For Example:
    >>> foods = {12: 'Cabbage',
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
    >>> recipe(1000, foods)
        ('Lettuce', 'Corn', 'Sausage', 'White Rice')

    Args:
        bmr (int): the calories expended in a neutrally temperate environment
        foods (dict): the calories and corresponding foods
    
    Return:
        Tuple
    """
    calories = foods.keys()
    abs_min = sum(calories)
    for i in range(len(foods)):
        groups = itertools.combinations(calories, i+1)
        for group in groups:
            if abs(sum(group) - bmr) < abs_min:
                abs_min = abs(sum(group) - bmr)
                result = group
    recipe = []
    for item in result:
        recipe.append(foods[item])
    return tuple(recipe)


def print_recipe(bmr, recipe: Tuple):
    """
    Prints out the recipe in standard form.

    Args:
        bmr (int): the calories expended in a neutrally temperate environment
        recipe (tuple): the recommend foods
    """
    string = ', '.join(recipe)
    print(f'You need {bmr} calories every day.')
    print(f'Recommended recipes (100g each): {string}')


def run():
    """
    Runs the application.
    """
    info = get_info()
    bmr = calculate_bmr(info)
    foods = load_food('foods.csv')
    plan = recipe(bmr, foods)
    print_recipe(bmr, plan)


if __name__ == "__main__":
    run()
