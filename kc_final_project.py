import tkinter as tk
from tkinter import Label, Entry, Button, StringVar

# Missing functions from original code
def calculate_ideal_weight(height_cm, gender):
    if gender == "male":
        ideal_weight_kg = (height_cm - 100) * 0.9
    elif gender == "female":
        ideal_weight_kg = (height_cm - 100) * 0.85
    else:
        print(f"Sorry {name_entry.get()} invalid gender.")
        return None
    return ideal_weight_kg
#weight defference culculater
def calculate_weight_difference(current_weight_kg, ideal_weight_kg):
    return current_weight_kg - ideal_weight_kg
#calories calculater
def calculate_calories_needed(weight_kg, height_cm, age, gender, activity_level, goal):
    if gender == "male":
        bmr = 88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * age)
    elif gender == "female":
        bmr = 447.593 + (9.247 * weight_kg) + (3.098 * height_cm) - (4.330 * age)
    else:
        print(f"Sorry {name_entry.get()} invalid gender.")
        return None
#activaty equations
    activity_multipliers = {
        "sedentary": 1.2,
        "moderate": 1.55,
        "active": 1.725
    }
    #goal choices
    if goal == "maintain weight":
        calories_needed = bmr * activity_multipliers.get(activity_level, 1.2)
    elif goal == "gain weight":
        calories_needed = bmr * activity_multipliers.get(activity_level, 1.2) + 500
    elif goal == "lose weight":
        calories_needed = bmr * activity_multipliers.get(activity_level, 1.2) - 500
    else:
        print(f"Sorry {name_entry.get()} invalid goal input.")
        return None

    return calories_needed
#daily water needes
def calculate_daily_water_intake(weight_kg):
    water_intake_liters = weight_kg * 0.033
    return water_intake_liters

# perform calculations
#inputs
def calculate():
    name = name_entry.get()
    height_cm = float(height_entry.get())
    current_weight_kg = float(weight_entry.get())
    age = int(age_entry.get())
    gender = gender_var.get()
    activity_level = activity_var.get()
    goal = goal_var.get()

#ideal weight calculation
    ideal_weight = calculate_ideal_weight(height_cm, gender)
    calories_needed = calculate_calories_needed(current_weight_kg, height_cm, age, gender, activity_level, goal)

    if calories_needed:
        result_label.config(text=f"Your Calories needed per day is {calories_needed:.2f} kcal")

    water_intake = calculate_daily_water_intake(current_weight_kg)
    water_label.config(text=f"Your Daily water intake is {water_intake:.2f} liters")

    height_in_meter = (height_cm / 100)
    height_measure = (height_in_meter * height_in_meter)
    bmi = (current_weight_kg / height_measure)
    print(bmi)
    needed_weight_limit1 = (25 - bmi)
    weight_need_to_lose_gain1 = abs(needed_weight_limit1 * height_measure)

    needed_weight_limit2 = (18.5 - bmi)
    weight_need_to_lose_gain2 = abs(needed_weight_limit2 * height_measure)
#bmi calculation
    if bmi < 16:
        bmi_result_label.config(text=f"You are so thin you need to gain ({weight_need_to_lose_gain1:.2f}) to ({weight_need_to_lose_gain2:.2f}) kg")
    elif bmi >= 16 and bmi<= 17:
        bmi_result_label.config(text=f'You are Normal thin you need to gain ({weight_need_to_lose_gain1:.2f}) to ({weight_need_to_lose_gain2:.2f}) kg')
    elif bmi >= 17 and bmi<= 18.5:
        bmi_result_label.config(text=f'You are Little thin you need to gain ({weight_need_to_lose_gain1:.2f}) to ({weight_need_to_lose_gain2:.2f}) kg')
    elif bmi >= 18.5 and bmi<= 25:
        bmi_result_label.config(text=f'You have a perfect weight. Good job {name}!')
    elif bmi >= 25 and bmi<= 30:
        bmi_result_label.config(text=f'You are fat you need to lose ({weight_need_to_lose_gain1:.2f}) to ({weight_need_to_lose_gain2:.2f}) kg')
    elif bmi > 30:
        bmi_result_label.config(text=f'You are overweight you need to lose ({weight_need_to_lose_gain1:.2f}) to ({weight_need_to_lose_gain2:.2f}) kg')

# main Tkinter window
root = tk.Tk()
root.geometry("800x500")
root.title("Bfit")

# labels and entry fields
Label(root, text="Welcome to Bfit").pack()

Label(root, text="Enter your name").pack()
name_entry = Entry(root)
name_entry.pack()

Label(root, text="Enter your height in cm").pack()
height_entry = Entry(root)
height_entry.pack()

Label(root, text="Enter your current weight in kg").pack()
weight_entry = Entry(root)
weight_entry.pack()

Label(root, text="Enter your age").pack()
age_entry = Entry(root)
age_entry.pack()

Label(root, text="Enter your gender (male/female)").pack()
gender_var = StringVar()
gender_var.set("male")
gender_entry = Entry(root, textvariable=gender_var)
gender_entry.pack()

Label(root, text="Enter your activity level (sedentary/moderate/active)").pack()
activity_var = StringVar()
activity_var.set("sedentary")
activity_entry = Entry(root, textvariable=activity_var)
activity_entry.pack()

Label(root, text="Enter your goal (maintain weight/gain weight/lose weight)").pack()
goal_var = StringVar()
goal_var.set("maintain weight")
goal_entry = Entry(root, textvariable=goal_var)
goal_entry.pack()

# result label
result_label = Label(root, text="")
result_label.pack()

# water label
water_label = Label(root, text="")
water_label.pack()

# BMI result label
bmi_result_label = Label(root, text="")
bmi_result_label.pack()

#calculate button
calculate_button = Button(root, text="Calculate", command=calculate)
calculate_button.pack()

root.mainloop()
