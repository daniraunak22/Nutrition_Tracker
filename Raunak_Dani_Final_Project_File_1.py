"""
Course Number: ENGR 13300
Semester: Fall 2024

Description:
    As my final project, the goal of this program is to be a nutrition logger. Thus, a user will input their desired 
    goals for calories and nutrients, and this program will be able to call an API containing this information and be 
    able to log the food that the user input.

Assignment Information:
    Assignment:     Individual Project
    Team ID:        LC5-13
    Author:         Raunak Dani, dani@purdue.edu
    Date:           11/19/2024

Contributors:
    Name, login@purdue [repeat for each]

    My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

import requests
from Raunak_Dani_Final_Project_File_2 import visualize_nutritional_progress

# API Details given from MyFitness Pal, given https://rapidapi.com/UnitedAPI/api/myfitnesspal2/playground/apiendpoint_6366f956-a637-4915-bbf7-42243844259e
API_URL = "https://myfitnesspal2.p.rapidapi.com/searchByKeyword"
API_KEY = "6cadefb81cmshabc116616c3cbd8p1a5715jsn1648a0f8d1e6"
HEADERS = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": "myfitnesspal2.p.rapidapi.com"
}

#The purpose of this function is to get user input for all the foods that the user inputs
def user_foods():
    foods = []
    while True:
        food = input("Enter the food you would like to log (or type 'STOP' to finish): ").strip()
        if not food:
            print("Food name cannot be empty. Please try again.")
            continue
        if food.upper() == "STOP":
            break
        foods.append(food)
    return foods

#Fetches nutritional data for a given food from the MyFitnessPal API
def get_food_data(food_name):
    #establishes the params and the response as the MyFitnessPal API code segment demonstrated
    params = {"keyword": food_name, "page": "1"}
    response = requests.get(API_URL, headers=HEADERS, params=params) #sends a request at the given API url and inputs the parameters
    if response.status_code == 200: #indicates that the request was a success
        data = response.json() #reads all data
        if isinstance(data, list) and len(data) > 0:
            return data  # return the full list of results if the data is a list and is a length > 0
        else:
            print(f"No data found for '{food_name}'.")
            return None
    else: #this is an error code of 400
        print(f"Error: {response.status_code} - {response.text}")
        return None

#displays all available food options for the user to choose from.
def display_food_choices(food_data):
    print("\nAvailable Options:")
    #this following segment is responsible for extracting the speicifc information based off of the list
    for i, food in enumerate(food_data):
        name = food.get("name", "Unknown")
        brand = food.get("brand", "Generic")
        serving_size = food["nutrition"].get("Serving Size", "Unknown") #this is a subcategory as seen on the website
        calories = food["nutrition"].get("Calories", "Unknown")
        print(f"{i+1}. {name} (Brand: {brand}, Serving Size: {serving_size}, Calories: {calories})")
    
    #this code is responsible for selecting the specific output (1-20) which is output from the API
    while True:
        try:
            choice = int(input("\nEnter the number of the food you want to log (or 0 to skip): "))
            if 0 <= choice <= len(food_data):
                if choice > 0:
                    return choice - 1
                else:
                    return None
            else:
                print("Invalid choice. Please select a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    #gets the daily goals for each macronutrient and has input validation
    while True:
        calorie_goal = float(input("Enter your daily calorie goal: "))
        if calorie_goal <= 0:
            print("\nEnter a calorie goal greater than 0\n")
            continue
        else:
            break
    
    while True:
        protein_goal = float(input("Enter your daily protein goal (g): "))
        if protein_goal <= 0:
            print("\nEnter a protein goal greater than 0\n")
            continue
        else:
            break

    while True:
        carb_goal = float(input("Enter your daily carbohydrate goal (g): "))
        if carb_goal <= 0:
            print("\nEnter a carb goal greater than 0\n")
            continue
        else:
            break
    
    while True:
        fat_goal = float(input("Enter your daily fat goal (g): "))
        if fat_goal <= 0:
            print("\nEnter a fat goal greater than 0\n")
            continue
        else:
            break
    
    #intializes the starting values of the total calories consumed
    foods = user_foods()
    total_calories = 0
    total_protein = 0
    total_fats = 0
    total_carbs = 0

    for food in foods: #iterates through each element within the user input list
        food_data = get_food_data(food)
        if food_data:
            choice_index = display_food_choices(food_data)
            if choice_index is not None: #takes out every single one of the 20 elements and is able to extract the name, brand, nutrition, calories, protein, fat, and carbs, where these values are assigned to variables
                chosen_food = food_data[choice_index]
                name = chosen_food.get("name", "Unknown")
                brand = chosen_food.get("brand", "Generic")
                nutrition = chosen_food.get("nutrition", {})
                calories = float(nutrition.get("Calories", 0))
                protein = float(nutrition.get("Protein", 0).replace("g", "") if "g" in nutrition.get("Protein", "0") else nutrition.get("Protein", 0))
                fats = float(nutrition.get("Fat", 0).replace("g", "") if "g" in nutrition.get("Fat", "0") else nutrition.get("Fat", 0))
                carbs = float(nutrition.get("Carbs", 0).replace("g", "") if "g" in nutrition.get("Carbs", "0") else nutrition.get("Carbs", 0))
                #these statements above remove the word 'grams' represented as 'g' into a blank space to extract the values, replaces values w/ 0 if not present
                total_calories += calories #adds the corresponding macronutrients to their previous values
                total_protein += protein
                total_fats += fats
                total_carbs += carbs

                print(f"Logged: {name} (Brand: {brand}, Calories: {calories}, Protein: {protein}g, Fat: {fats}g, Carbs: {carbs}g)")
            else:
                print(f"Skipped logging for '{food}'.")
        else:
            print(f"Skipping '{food}' due to missing data.")

    print("\n--- Summary ---")
    print(f"Total Calories Consumed: {total_calories}")
    print(f"Total Protein Consumed: {total_protein}g")
    print(f"Total Fat Consumed: {total_fats}g")
    print(f"Total Carbohydrates Consumed: {total_carbs}g")
    print(f"Daily Calorie Goal: {calorie_goal}")
    print(f"Calories Remaining: {max(0, calorie_goal - total_calories)}\n")
    #calling the graphing function
    visualize_nutritional_progress(total_calories, calorie_goal, total_protein, protein_goal, total_carbs, carb_goal, total_fats, fat_goal)

if __name__ == "__main__":
    main()
