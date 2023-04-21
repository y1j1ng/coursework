# Final Project: Calorie Calculator Application

This application is designed to advise about the recipe for a day. The user needs to provide their ages, genders, heights, and weights, then the application will calculate the BMR (Basal metabolic rate) based on the Mifflin-St Jeor formula. In the end, it will return with a food plan based on it, which can meet the calories they need.

## 1. Get input from the users 
We need personal information (sex, age, height, and weight) from users to calculate their BMR (basal metabolic rate).

## 2. Check the input
We need to check all the inputs to see whether they are valid. The input from users could be various, the check functions will help to standardize inputs for the application. The limitation of each check function is set based on the world record I found in the wiki.

## 3. Calculate the BMR
BMR refers to the calories needed by the human body to maintain metabolism in a resting state, such as breathing, organ operation, body temperature maintenance, etc., even if lying still all day, it will consume the lowest calories. BMR decreases with age or weight loss and increases with muscle mass.

Calculate personal BMR based on the Mifflin-St Jeor formula.

BMR = 9.99 * weight + 6.25 * height - 4.92 * age + (166 * sex (male = 1, female = 0) - 161)
 
## 4. Load a file that contains calories and foods
Loads the calories and food list from the given file and returns a dictionary of calories and the corresponding foods.

The data in the given file 'foods.csv' is from here:

http://www.totalcare.hk/healthy_diet/healthy_diet-article/calorie-table-eat-food-calories.html/comment-page-10


## 5. Give advice about the food plan
Based on the calories and foods in the given file, the application will generate a food plan with the total calories closest to BMR.

```python
def recipe(bmr: int, foods: Dict[int, str]) -> Tuple:
    calories = foods.keys()
    abs_min = sum(calories)  # Set the initial value to the sum of all the foods
    for i in range(len(foods)):
        groups = itertools.combinations(calories, i+1)  # Return all subsets of length i+1 in calories 
        for group in groups:
            if abs(sum(group) - bmr) < abs_min:  # Compare the absolute value and abs_min
                abs_min = abs(sum(group) - bmr) 
                result = group
    recipe = []
    for item in result:
        recipe.append(foods[item])
    return tuple(recipe)
```

## 6. Print out the food plan
Print out the food plan in a standard format.