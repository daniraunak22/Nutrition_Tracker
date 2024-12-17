"""
Course Number: ENGR 13300
Semester: Fall 2024

Description: The purpose of this UDF is to plot all of the various macronutrients that are consumed.
This function creates a total of 4 graphs, plotting the calories, protein, carbs, and fats consumed.

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

import matplotlib.pyplot as plt

def visualize_nutritional_progress(total_calories, calorie_goal, total_protein, protein_goal, total_carbs, carb_goal, total_fats, fat_goal):
    """Visualizes calories, protein, carbs, and fats consumption vs goals using pie charts."""
    plt.figure(figsize=(12, 12))

    # Calories
    plt.subplot(2, 2, 1)
    consumed = total_calories
    remaining = max(0, calorie_goal - total_calories)
    #The autopct helps display the percentage on the chart
    plt.pie([consumed, remaining], labels=["Consumed", "Remaining"], autopct='%1.1f%%', colors=['green', 'blue'])
    plt.title("Calories")

    # Protein
    plt.subplot(2, 2, 2)
    consumed = total_protein
    remaining = max(0, protein_goal - total_protein)
    plt.pie([consumed, remaining], labels=["Consumed", "Remaining"], autopct='%1.1f%%', colors=['purple', 'lightblue'])
    plt.title("Protein (g)")

    # Carbs
    plt.subplot(2, 2, 3)
    consumed = total_carbs
    remaining = max(0, carb_goal - total_carbs)
    plt.pie([consumed, remaining], labels=["Consumed", "Remaining"], autopct='%1.1f%%', colors=['orange', 'yellow'])
    plt.title("Carbs (g)")

    # Fats
    plt.subplot(2, 2, 4)
    consumed = total_fats
    remaining = max(0, fat_goal - total_fats)
    plt.pie([consumed, remaining], labels=["Consumed", "Remaining"], autopct='%1.1f%%', colors=['red', 'pink'])
    plt.title("Fats (g)")

    plt.tight_layout()
    plt.show()